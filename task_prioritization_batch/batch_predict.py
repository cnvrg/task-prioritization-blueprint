import json
import csv
import os
import argparse
import pathlib
import sys

scripts_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(scripts_dir))
cnvrg_workdir = os.environ.get('CNVRG_WORKDIR', '/cnvrg')
import predict


def batch_predict(input_file):
    f = open(input_file)
    texts = json.load(f)
    preds = []
    for t in texts:
        id = ""
        if type(t) is dict:
            id = t["id"]
            t = t["text"]

        text = {'input_text': t}
        pred = predict.predict(text)
        row = {}
        if id:
            row["id"] = id
        row["text"] = t
        row.update(pred)
        preds.append(row)
    with open(cnvrg_workdir+'/batch.csv', 'w', encoding='utf8', newline='') as output_file:
        dw = csv.DictWriter(output_file,
                            fieldnames=preds[0].keys(),

                            )
        dw.writeheader()
        dw.writerows(preds)


# f = open(os.environ.get('batch_input','texts.json'))
parser = argparse.ArgumentParser(description="""Preprocessor""")

parser.add_argument('--batch_input', action='store', dest='batch_input', required=True,
                    help="""string. json file name for input texts""")

args = parser.parse_args()
batch_input = args.batch_input
batch_input_path = os.path.join(cnvrg_workdir, batch_input)

data = []
if batch_input.endswith('.csv'):
    with open(batch_input_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            text = rows['texts']
            data.append(text)

    batch_input_path = batch_input.replace('.csv', '.json')
    with open(batch_input_path, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))


batch_predict(batch_input_path)