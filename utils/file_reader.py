import os
from typing import Iterable

DATA_DIR = './data'


def get_file_path(file_name: str) -> str:
    return os.path.join(DATA_DIR, file_name)


def read_file(file_path: str) -> Iterable[str]:
    with open(file_path) as f:
        return f.readlines()
