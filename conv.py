import json


with open('output.json') as in_fp:
    data = json.load(in_fp)

    with open('output2.json', 'w', encoding='utf-8') as out_fp:
        json.dump(data, out_fp, ensure_ascii=False)
