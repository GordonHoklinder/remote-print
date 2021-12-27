from django.core.files.storage import default_storage
import datetime
import re
from typing import List

GCODE_FOLDER_PREFIX = '/gcode-files/'
TSV_PATH = GCODE_FOLDER_PREFIX + 'in-queue.tsv'
LOG_PATH = 'logs/runtime-log.txt'


def clear_file_name(file_name: str) -> str:
    time_stamp = '=' + datetime.datetime.now().strftime('%d-%m-%y-%H-%M') + '.'
    file_name = re.sub(r'[=\\\s/]+', '_', file_name)
    split_file_name = file_name.rsplit('.', 1)
    split_file_name[0] = split_file_name[0].replace('.', '_')
    return GCODE_FOLDER_PREFIX + time_stamp.join(split_file_name)


def save_file(file) -> str:
    return default_storage.save(clear_file_name(file.name), file)


def add_file_path(file_path):
    with default_storage.open(TSV_PATH, 'a') as f:
        f.write(file_path + '\n')


def store_file(file):
    file_path = save_file(file)
    add_file_path(file_path)


def load_print_history():
    with open(TSV_PATH, 'r') as f:
        return [re.split(r'[\t=]', line) for line in f.read().split('\n')]


def log(message):
    with default_storage.open(LOG_PATH, 'a') as f:
        f.write(message + '\n')

