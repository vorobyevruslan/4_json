import json
import pprint

def load_data(filepath):
    strin = ''
    with open(filepath, encoding='utf8') as iner:
        for line in iner:
            strin += line
    return strin


def pretty_print_json(data):
    pprint.pprint(data)


if __name__ == '__main__':
    filepath = input()
    strin = load_data(filepath)
    data = json.loads(strin)
    pretty_print_json(data)
