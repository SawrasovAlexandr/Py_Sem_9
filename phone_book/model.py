import csv

def load(path_file: str) -> list:
    with open(path_file, 'r', newline='', encoding = 'utf-8') as data:
        database = list(csv.DictReader(data, delimiter=';'))
    return database

def show(data_base: list) -> str:
    id = 'ID'
    ph_db = ''
    for i, item in enumerate(data_base):
        ph_db += f'______\n<b>{id}:</b> {i}\n'
        for k in item.items():
            ph_db += f'<b>{k[0]}:</b> {k[1]}\n'
    return ph_db


def find(data_base: list, find_str: str) -> None:
    find_data = []
    if find_str:
        for item in data_base:
            if find_str.lower() in ' '.join(item.values()).lower():
                find_data.append(item)
    else: find_data = data_base
    id = 'ID'
    find_db = ''
    for item in find_data:
        i = data_base.index(item)
        find_db += f'______\n<b>{id}:</b> {i}\n'
        for k in item.items():
            find_db += f'<b>{k[0]}:</b> {k[1]}\n'
    return find_db
        