from .file_loader import *
from gcode_sender import print_file, is_printing
from enum import Enum

class PrinterState(str, Enum):
    Printing = 'printing',
    Idle = 'idle',
    Error = 'error'


class FileState(str, Enum):
    Done = 'done'
    Running = 'running'
    Waiting = 'waiting'
    Error = 'error'


last_file_index = None


def check_for_new_prints():
    files_in_queue = get_queue_files()
    for i in range(len(files_in_queue)):
        filename, file_state = files_in_queue[i]
        if file_state == FileState.waiting:
            last_file_index = i
            rewrite_ith_state(last_file_index, FileState.Running)
            print_file(read_file(filename), filename)
            set_state(PrinterState.Printing)
            return


def update_printer_state():
    if not is_printing():
        set_state(PrinterState.Idle)



def check_for_changes():
    state = get_state()
    if state == PrinterState.Idle:
        check_for_new_prints()
    elif state == PrinterState.Printing:
        update_printer_state()

