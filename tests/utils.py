import json


def load_fixture_rel(name):
    path = f'{name}'
    with open(path, encoding='utf-8') as fp:
        return json.load(fp)


def load_document_rel(name):
    path = f'{name}'
    with open(path, encoding='utf-8') as fp:
        return fp.read()