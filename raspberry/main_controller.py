from file_loader import *
from gcode_sender import GcodeSender
from enum import Enum
from time import sleep

class PrinterState(str, Enum):
    Printing = 'printing',
    Idle = 'idle',
    Error = 'error'


class FileState(str, Enum):
    Done = 'done'
    Running = 'running'
    Waiting = 'waiting'
    Error = 'error'



class MainController:
    def __init__(self):
        self.gcode_sender = GcodeSender()
        init_server_files()
        self.last_file_index = None

    def check_for_new_prints(self):
        files_in_queue = get_queue_files()
        for i in range(len(files_in_queue)):
            filename, file_state = files_in_queue[i]
            if file_state == FileState.Waiting:
                self.last_file_index = i
                rewrite_ith_state(self.last_file_index, FileState.Running)
                set_state(PrinterState.Printing)
                self.gcode_sender.print_file(read_file(filename))
                return


    def update_printer_state(self):
        if not self.gcode_sender.is_printing():
            set_state(PrinterState.Idle)
            if self.last_file_index is not None:
                rewrite_ith_state(self.last_file_index, FileState.Done)
                self.last_file_index = None



    def check_for_changes(self):
        state = get_state()
        if state == PrinterState.Idle:
            self.check_for_new_prints()
        elif state == PrinterState.Printing:
            self.update_printer_state()

    def run(self):
        while True:
            self.check_for_changes()
            sleep(10)


if __name__ == "__main__":
    MainController().run()
