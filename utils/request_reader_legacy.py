from typing import Iterable, Tuple

from utils.request_reader import Command


def read_value(data: dict[str, str], name: str) -> str | None:
    if name in data:
        return data[name]

    return None


def parse_request_legacy(data: dict[str, str]) -> Iterable[Command]:
    inc = 1
    while f'cmd{inc}' in data:
        yield data[f'cmd{inc}'], read_value(data, f'value{inc}')
        inc += 1
