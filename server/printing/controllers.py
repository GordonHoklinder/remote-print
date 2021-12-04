from django.core.files.storage import default_storage
import datetime

def save_file(file) -> str:
    time_stamp = '-' + datetime.datetime.now().strftime('%d-%m-%y-%H-%M') + '.'
    filename = time_stamp.join(file.name.rsplit('.', 1))
    return default_storage.save(filename, file)

def add_file_path(file_path):
    tsv_path = 'in-queue.tsv'
    with default_storage.open(tsv_path, 'a') as f:
        f.write(file_path + '\n')

def store_file(file):
    file_path = save_file(file)
    add_file_path(file_path)
