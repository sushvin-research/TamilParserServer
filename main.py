import os
import re
import subprocess

from tamil_nlp_package_test import sent_tokenizer as tt
from trankit import Pipeline

from fastapi import FastAPI, Form

app = FastAPI()
p = Pipeline(lang='customized-mwt', cache_dir=r"save_dir")


def get_command_output(command):
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.returncode)
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


@app.get("/")
async def main():
    return {"Message": "Server is listening..."}


@app.post("/visualizeGraph")
async def get_graph(data: str = Form('data')):
    with open('data.conllu', 'w') as f:
        f.write(data)

    return get_command_output('./bin/conllu2svg data.conllu')


def print_conllu_format(data):
    result = {}
    for sentence_info in data['sentences']:
        tokens = sentence_info['tokens']

        conllu_text = ''
        pos = []
        morph = []
        for token_info in tokens:
            if type(token_info['id']) == int:
                token_id = token_info['id']
                token_text = token_info['text']
                lemma = token_info['lemma']
                upos = token_info['upos']
                xpos = token_info.get('xpos', '_')
                feats = token_info.get('feats', '_')
                head = token_info['head']
                deprel = token_info['deprel']
                deps = str(head) + ":" + str(deprel)
                conllu_text += f"{token_id}\t{token_text}\t{lemma}\t{upos}\t{xpos}\t{feats}\t{head}\t{deprel}\t{deps}\t_\n"
                pos.append({"token_text": token_text, "upos": upos})
                morph.append({"token_text": token_info['text'], "feats": token_info.get('feats', '_'),
                              "upos": token_info['upos'],
                              "lemma": token_info['lemma']})
            else:
                conllu_text += f"{token_info['id'][0]}-{token_info['id'][1]}\t{token_info['text']}\t_\t_\t_\t_\t_\t_\t_\t_\n"
                for token in token_info['expanded']:
                    head = token['head']
                    deprel = token['deprel']
                    deps = str(head) + ":" + str(deprel)
                    conllu_text += f"{token['id']}\t{token['text']}\t{token['lemma']}\t{token['upos']}\t{token.get('xpos', '_')}\t{token.get('feats', '_')}\t{token['head']}\t{token['deprel']}\t{deps}\t_\n"
                    pos.append({"token_text": token['text'], "upos": token['upos']})
                    morph.append({"token_text": token['text'], "feats": token.get('feats', '_'), "upos": token['upos'],
                                  "lemma": token['lemma']})
        conllu_text += "\n\n"
        result['graph_feature'] = conllu_text
        result['pos'] = pos
        result['morph'] = morph
        print(conllu_text)
    return result


@app.post("/get_trankit_graph_data")
async def get_trankit_graph_data(data: str = Form('data')):
    output = tt.tokenize(data.strip())
    print(output)
    texts = output.strip().split('\n')
    print(texts)
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
