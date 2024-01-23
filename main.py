import json
import os
import re
import subprocess

from tamil_nlp_package_test import tamil_tokenizer as tt
from trankit import Pipeline

from tamil_parser_web.scripts.lt2ssf import lt2ssf
from tamil_parser_web.scripts.convert_ssf_UD import ssfToUD
from fastapi import FastAPI, Form

app = FastAPI()


def get_command_output(command):
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.returncode)
    if result.returncode == 0:
        # Print the output
        print("Command output:")
        # print(result.stdout)
    else:
        # Print the error message
        print("Error executing command:")
        print(result.stderr)

    os.remove("data.conllu")
    return result.stdout


def getAllData(text):
    proc = subprocess.run(
        ["php", f'{os.path.dirname(__file__)}/tamil_parser_web/scripts/annotate.php', text, 'null'],
        capture_output=True, text=True)

    if proc.stderr:
        print("ERR - ", proc.stderr)
    else:
        print("RES - ", proc.stdout)

    return proc.stdout


def get_first_word_after_split(input_string):
    if input_string.startswith('^'):
        cleaned_string = input_string.replace('^', '')
        split_result = cleaned_string.split('/')
        if split_result:
            return split_result[0]
        else:
            return '-'


def process_string(array):
    result_array = []
    for parts in array:
        last_part = parts[-1]
        start_index = last_part.find("af='") + len("af='")
        end_index = last_part.find(",", start_index)
        extracted_value = last_part[start_index:end_index]
        parts.insert(2, extracted_value)
        result_array.append('\t'.join(parts))
    return result_array


def get_graph_2(data):
    with open('data.conllu', 'w') as f:
        f.write(data)

    return get_command_output('./bin/conllu2svg data.conllu')


@app.post("/")
async def root(text: str = Form('text')):
    output = tt.tokenize(text)
    text = output.strip().split('</S><S> ')
    result = list(map(getAllData, text))

    data = json.loads(result[0])

    lt_array = []
    with open("output_graph.txt", "w") as file:
        for i in text:
            split_words = i.strip().split(' ')
            for index, word in enumerate(split_words, start=1):
                if index <= len(data['pos_annotations']['Model1']):
                    feature1 = data['pos_annotations']['Model1'][index - 1]["feature"]
                if index <= len(data['morph']):
                    feature2 = data['morph'][index - 1]["feature"]
                    lemma = get_first_word_after_split(feature2[0].strip().split('<')[0])

                file.write(f"{index}\t{lemma}\t{feature1.strip()}\t{feature2[0].strip()}\n")
                lt_array.append(f"{index}\t{lemma}\t{feature1.strip()}\t{feature2[0].strip()}\n")
            file.write("\n\n")

    ssf_array = lt2ssf(lt_array)
    updated_ssf_array = []
    for i in ssf_array:
        i = i.strip().split("\t")
        i[len(i) - 1] = i[len(i) - 1].strip().split("|")[0]
        updated_ssf_array.append("\t".join(i))

    ud_array = ssfToUD(updated_ssf_array)

    result_array = []

    for ssf, ud in zip(ssf_array, ud_array):
        ssf2 = ssf.strip().split('\t')
        ud2 = ud.strip().split('\t')

        if ssf2[:3] == ud2[:3]:
            new_array = ssf2[:3]
            new_array.extend(ud2[3:])
            result_array.append(new_array)

    result_array = process_string(result_array)

    with open("ud_output.txt", "w") as file:
        for i in result_array:
            if i.startswith("1\t"):
                file.write("\n\n")
            file.write(i + "\n")
    print("Process Completed.")

    return result


@app.post("/visualizeGraph")
async def get_graph(data: str = Form('data')):
    with open('data.conllu', 'w') as f:
        f.write(data)

    return get_command_output('./bin/conllu2svg data.conllu')


def print_conllu_format(data):
    conllu_text = ''
    result = {}
    pos = []
    morph = []
    for sentence_info in data['sentences']:
        sentence_id = sentence_info['id']
        sentence_text = sentence_info['text']
        tokens = sentence_info['tokens']

        print(f"# sent_id = {sentence_id}")
        print(f"# text = {sentence_text}")
        conllu_text = ''
        pos = []
        morph = []
        for token_info in tokens:
            token_id = token_info['id']
            token_text = token_info['text']
            lemma = token_info['lemma']
            upos = token_info['upos']
            xpos = token_info.get('xpos', '_')
            feats = token_info.get('feats', '_')
            head = token_info['head']
            deprel = token_info['deprel']
            # deps = token_info.get('deps', '_')
            # misc = token_info.get('misc', '_')

            conllu_text += f"{token_id}\t{token_text}\t{lemma}\t{upos}\t{xpos}\t{feats}\t{head}\t{deprel}\t_\t_\n"
            pos.append({"token_text": token_text, "upos": upos})
            morph.append({"token_text": token_text, "feats": feats})
        conllu_text += "\n\n"
        result['graph_feature'] = conllu_text
        result['pos'] = pos
        result['morph'] = morph
        print(conllu_text)
    return result


@app.post("/get_trankit_graph_data")
async def get_trankit_graph_data(data: str = Form('data')):
    p = Pipeline(lang='customized',
                 cache_dir=rf"{os.getenv('saved_model')}")
    output = tt.tokenize(data)
    texts = output.strip().split('</S><S> ')

    doc_texts = []
    for text in texts:
        if text != '':
            text = re.sub(r'^(\d+)\.\s*', r'\1', text)
            all_info = p(text)
            result = print_conllu_format(all_info)
            doc_texts.append(
                {"text": text, "feature": result['graph_feature'], "pos": result['pos'], "morph": result['morph']}
            )
    print(doc_texts)
    return doc_texts
