import json


def load_json(path):
    with open(path, encoding='utf-8') as fp:
        return json.load(fp)


def load_file(path):
    with open(path, encoding='utf-8') as fp:
        return fp.read()
