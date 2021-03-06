import fabric
from typing import List

SERVER_GCODE_LOCATION = 'remote-print/server/gcode-files/'

FILE_QUEUE_PATH = 'in-queue.tsv'
STATE_PATH = 'state.txt'




def get_ssh_server_address() -> str:
    with open('server_address', 'r') as address_file:
        return address_file.read().strip()


ssh_server_address = get_ssh_server_address()


def ssh_execute_command(command: str):
    with fabric.Connection(ssh_server_address) as connection:
        return connection.run(command)


def read_file(filepath: str) -> str:
    command = f'cat {SERVER_GCODE_LOCATION}{filepath}'
    return ssh_execute_command(command).stdout

def write_file(filepath: str, text: str, append: str = False):
    command = f'printf "{text}" >{">" if append else ""} {SERVER_GCODE_LOCATION}{filepath}'
    ssh_execute_command(command)

def init_server_files():
    write_file(FILE_QUEUE_PATH, '', True)
    write_file(STATE_PATH, '', True)


def get_queue_files() -> List[List[str]]:
    file = read_file(FILE_QUEUE_PATH)
    return [line.split('\t') for line in file.split('\n') if line]


def get_state() -> str:
    return read_file(STATE_PATH).strip() or 'idle'


def set_state(state: str):
    write_file(STATE_PATH, state)


def rewrite_ith_state(i: int, new_state: str):
    files = get_queue_files()
    files[i][1] = new_state
    files = '\n'.join(['\t'.join(file) for file in files]) + '\n'
    write_file(FILE_QUEUE_PATH, files)

