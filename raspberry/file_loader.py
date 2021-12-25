import fabric
from typing import List

FILE_QUEUE_PATH = 'remote-print/server/in-queue.tsv'

def get_ssh_server_address() -> str:
    with open('server_address', 'r') as address_file:
        return address_file.read().strip()


ssh_server_address = get_ssh_server_address()


def ssh_execute_command(command: str):
    connection = fabric.Connection(ssh_server_address)
    return connection.run(command)


def get_file(filepath: str) -> str:
    command = f'cat {filepath}'
    return ssh_execute_command(command).stdout


def get_queue_files() -> List[List[str]]:
    file = get_file(FILE_QUEUE_PATH)
    return [line.split('\t') for line in file.split('\n') if line]

