import os
import re
import subprocess
from contextlib import asynccontextmanager
from tamil_nlp_package_test import sent_tokenizer
from trankit import Pipeline
from fastapi import FastAPI, Form
from processor import print_conllu_format

# p = Pipeline(lang='customized-mwt', cache_dir=r"Models/Model_v1.1")

model_checkpoints = [
    "Model_v1.1", "Model_v1.2", "Model_v1.3", "Model_v1.4"
]

model_vars = {}


def load_model(model_checkpoint):
    return Pipeline(lang='customized-mwt', cache_dir=f"Models/{model_checkpoint}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        for i, model_checkpoint in enumerate(model_checkpoints):
            model_vars[model_checkpoint] = load_model(model_checkpoint)
        yield model_vars
        model_vars.clear()
    except Exception as e:
        print(f"Startup: Error loading models: {e}")


app = FastAPI(lifespan=lifespan)


def get_command_output(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print("Error executing command:", result.stderr)
    os.remove("data.conllu")
    return result.stdout


@app.get("/")
async def main():
    return {"Message": "Server is listening..."}


@app.post("/visualizeGraph")
async def get_graph(data: str = Form('data')):
    with open('data.conllu', 'w') as f:
        f.write(data)

    return get_command_output('./bin/conllu2svg data.conllu')


@app.post("/get_trankit_graph_data")
async def get_trankit_graph_data(data: str = Form('data'), model_checkpoint: str = Form('model_checkpoint')):
    data = data.replace("\n", " ")
    output = sent_tokenizer.tokenize(data.strip())
    texts = output.strip().split('\n')
    doc_texts = []
    for text in texts:
        if text != '':
            text = re.sub(r'^(\d+)\.\s*', r'\1', text)
            all_info = model_vars[model_checkpoint](text)
            # all_info = p(text)
            result = print_conllu_format(all_info)
            doc_texts.append(
                {"text": text, "feature": result['graph_feature'], "pos": result['pos'], "morph": result['morph']}
            )
    return doc_texts
