import os
import re
import subprocess

from tamil_nlp_package_test import sent_tokenizer
from trankit import Pipeline

from fastapi import FastAPI, Form

from Morph.convertor import convert_tam_utf2wx, convert_tam_wx2utf
from Morph.get_conllu import process_text
from Morph.post_process import repair_rules

app = FastAPI()
p = Pipeline(lang='customized-mwt', cache_dir=r"Model-May-03")


def get_command_output(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print("Error executing command:", result.stderr)
    os.remove("data.conllu")
    return result.stdout


def is_go_installed():
    try:
        result = subprocess.run(["go", "version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Go is installed.")
            print("Version:", result.stdout)
            return True
        else:
            print("Go is not installed.")
            print("Error:", result.stderr)
            return False
    except FileNotFoundError:
        print("Go is not installed.")
        return False


@app.get("/api/tamilparser/server/")
async def main():
    return {"Message": "Server is listening..."}


@app.post("/api/tamilparser/server/visualizeGraph")
async def get_graph(data: str = Form('data')):
    with open('data.conllu', 'w') as f:
        f.write(data)

    return get_command_output('./bin/conllu2svg data.conllu')


def rule_pos(pos, morph_old):
    pos_string = ''
    lemma_result = {}
    morph_result = {}
    for index, data in enumerate(pos):
        pos_string += f"{index + 1}\t{convert_tam_utf2wx(data['token_text'])}\t{data['upos']}\n"
    rule_pos_dict = process_text(pos_string)
    for j, m in zip(pos, morph_old):
        i = convert_tam_utf2wx(j['token_text'])
        lemma_result[j['token_text']] = rule_pos_dict[i][0].split("\t")[2]
        lemma_text = rule_pos_dict[i][0].split("\t")[2].split("/")

        if len(lemma_text) > 1 and (j['upos'] == "VERB" or j['upos'] == "AUX") and ("Person=3" in m["feats"]):
            morph_text = lemma_text[1]
            pattern = r'<gen:(\w)>'
            match = re.search(pattern, morph_text)
            if match:
                gen_value = match.group(1)
                if gen_value == 'm':
                    m["feats"] = m["feats"].replace("Gender=Com", "Gender=Masc")
                elif gen_value == 'f':
                    m["feats"] = m["feats"].replace("Gender=Com", "Gender=Fem")

            morph_result[j['token_text']] = m["feats"]

        if (j['upos'] == "NOUN" or j['upos'] == "PROPN" or j['upos'] == "VERB" or j['upos'] == "AUX" or
                j['upos'] == "PRON" or j['upos'] == "NUM"):
            org_root_text = lemma_text[0]
            if len(lemma_text) > 1:
                if (j['upos'] == "NOUN" or j['upos'] == "PROPN") and len(lemma_text) > 1:
                    lemma_text = [s for s in lemma_text if 'noun' in s]

                elif j['upos'] == "VERB" or j['upos'] == "AUX" and len(lemma_text) > 1:
                    lemma_text = [s for s in lemma_text if 'verb' in s]

                elif j['upos'] == "PRON" and len(lemma_text) > 1:
                    lemma_text = [s for s in lemma_text if 'pronoun' in s]

                elif j['upos'] == "NUM" and len(lemma_text) > 1:
                    lemma_text = [s for s in lemma_text if 'num' in s]
                if len(lemma_text) == 0:
                    lemma_text = lemma_text
                else:
                    lemma_text = lemma_text[0]
            else:
                lemma_text = lemma_text[0]

            if len(lemma_text) > 0 and "<lcat" in lemma_text:
                split_text = lemma_text.split("<lcat")[0]
                if "rcat" in split_text:
                    split_text = re.sub(r'<.*?>', '', split_text)
                    lemma_result[j['token_text']] = convert_tam_wx2utf(split_text)
                else:
                    lemma_result[j['token_text']] = convert_tam_wx2utf(split_text)
            elif len(lemma_text) == 0:
                lemma_result[j['token_text']] = convert_tam_wx2utf(org_root_text.strip("^"))
            else:
                lemma_result[j['token_text']] = convert_tam_wx2utf(lemma_text)
        else:
            lemma_result[j['token_text']] = j['token_text']
    return lemma_result, morph_result


def print_conllu_format(data):
    result = {}
    for sentence_info in data['sentences']:
        tokens = sentence_info['tokens']

        conllu_text = ''
        pos = []
        morph_old = []
        morph = []

        for token_info in tokens:
            if type(token_info['id']) == int:
                token_text = token_info['text']
                upos = token_info['upos']
                pos.append({"token_text": token_text, "upos": upos})
                morph_old.append({"feats": token_info.get('feats', '_')})
            else:
                for token in token_info['expanded']:
                    pos.append({"token_text": token['text'], "upos": token['upos']})
                    morph_old.append({"feats": token.get('feats', '_')})
        lemma_result, morph_result = rule_pos(pos, morph_old)

        for token_info in tokens:
            if type(token_info['id']) == int:
                token_id = token_info['id']
                token_text = token_info['text']
                lemma = lemma_result[token_text]
                upos = token_info['upos']
                xpos = token_info.get('xpos', '_')
                feats = morph_result[token_text] if token_text in morph_result else token_info.get('feats', '_')
                # feats = token_info.get('feats', '_')
                head = token_info['head']
                deprel = token_info['deprel']
                deps = str(head) + ":" + str(deprel)
                conllu_text += f"{token_id}\t{token_text}\t{lemma}\t{upos}\t{xpos}\t{feats}\t{head}\t{deprel}\t{deps}\t_\n"
                morph.append({"token_text": token_info['text'], "feats": token_info.get('feats', '_'),
                              "upos": token_info['upos'],
                              "lemma": lemma})
            else:
                conllu_text += f"{token_info['id'][0]}-{token_info['id'][1]}\t{token_info['text']}\t_\t_\t_\t_\t_\t_\t_\t_\n"
                for token in token_info['expanded']:
                    head = token['head']
                    deprel = token['deprel']
                    deps = str(head) + ":" + str(deprel)
                    conllu_text += f"{token['id']}\t{token['text']}\t{lemma_result[token['text']]}\t{token['upos']}\t{token.get('xpos', '_')}\t{token.get('feats', '_')}\t{token['head']}\t{token['deprel']}\t{deps}\t_\n"
                    morph.append({"token_text": token['text'],
                                  "feats": morph_result[token['text']] if token['text'] in morph_result else token.get(
                                      'feats', '_'), "upos": token['upos'],
                                  "lemma": lemma_result[token['text']]})
        result['graph_feature'] = repair_rules(conllu_text) + "\n\n"
        result['pos'] = pos
        result['morph'] = morph
    return result


@app.post("/api/tamilparser/server/get_trankit_graph_data")
async def get_trankit_graph_data(data: str = Form('data')):
    data = data.replace("\n", " ")
    output = sent_tokenizer.tokenize(data.strip())
    texts = output.strip().split('\n')
    doc_texts = []
    for text in texts:
        if text != '':
            text = re.sub(r'^(\d+)\.\s*', r'\1', text)
            all_info = p(text)
            result = print_conllu_format(all_info)
            doc_texts.append(
                {"text": text, "feature": result['graph_feature'], "pos": result['pos'], "morph": result['morph']}
            )
    return doc_texts
