import json
from pprint import pprint


with open('operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    pprint(data)


