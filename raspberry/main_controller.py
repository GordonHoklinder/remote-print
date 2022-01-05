from file_loader import *
from gcode_sender import GcodeSender
from enum import Enum
from time import sleep

class PrinterState(str, Enum):
    Printing = 'printing',
    Idle = 'idle',


class FileState(str, Enum):
    Done = 'done'
    Running = 'running'
    Waiting = 'waiting'



class MainController:
    def __init__(self):
        self.gcode_sender = GcodeSender()
        init_server_files()

    def check_for_new_prints(self):
        files_in_queue = get_queue_files()
        for i in range(len(files_in_queue)):
            filename, file_state = files_in_queue[i]
            if file_state == FileState.Waiting:
                set_state(PrinterState.Printing)
                rewrite_ith_state(i, FileState.Running)
                self.gcode_sender.print_file(read_file(filename))
                set_state(PrinterState.Idle)
                rewrite_ith_state(i, FileState.Done)
                return

    def run(self):
        while True:
            self.check_for_new_prints()
            sleep(10)


if __name__ == "__main__":
    MainController().run()
