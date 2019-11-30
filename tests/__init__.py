import json


def load_fixture(name):
    path = f'tests/fixtures/{name}'
    with open(path, encoding='utf-8') as fp:
        return json.load(fp)


def load__document(name):
    path = f'tests/fixtures/{name}'
    with open(path, encoding='utf-8') as fp:
        return fp.read()
