from django.core.files.storage import default_storage
import datetime
import re
from typing import List
import os.path

GCODE_FOLDER_PREFIX = 'gcode-files/'
TSV_PATH = GCODE_FOLDER_PREFIX + 'in-queue.tsv'
LOG_PATH = 'logs/runtime-log.txt'
STATE_PATH = GCODE_FOLDER_PREFIX + 'state.txt'


def clear_file_name(file_name: str) -> str:
    time_stamp = '_' + datetime.datetime.now().strftime('%d-%m-%y-%H-%M') + '.'
    file_name = re.sub(r'[=\\\s/]+', '=', file_name)
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


def read_file(file_path):
    if not os.path.exists(file_path): return None
    with open(file_path, 'r') as f:
        return f.read()


def load_print_history():
    history = read_file(TSV_PATH)
    if history is None: return []
    return [re.split(r'[\t=]', line) for line in history.split('\n')]


def get_printing_state() -> str:
    return read_file(STATE_PATH) or 'idle'


def log(message):
    with default_storage.open(LOG_PATH, 'a') as f:
        f.write(message + '\n')

