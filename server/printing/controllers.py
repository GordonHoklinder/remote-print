from django.core.files.storage import default_storage
import datetime

GCODE_FOLDER_PREFIX = '/gcode-files/'
TSV_PATH = GCODE_FOLDER_PREFIX + 'in-queue.tsv'
LOG_PATH = 'logs/runtime-log.txt'

def save_file(file) -> str:
    time_stamp = '-' + datetime.datetime.now().strftime('%d-%m-%y-%H-%M') + '.'
    filepath = GCODE_FOLDER_PREFIX  +  time_stamp.join(file.name.rsplit('.', 1))
    return default_storage.save(filepath, file)

def add_file_path(file_path):
    with default_storage.open(TSV_PATH, 'a') as f:
        f.write(file_path + '\n')

def store_file(file):
    file_path = save_file(file)
    add_file_path(file_path)

def log(message):
    with default_storage.open(LOG_PATH, 'a') as f:
        f.write(message + '\n')
    
