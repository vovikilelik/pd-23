import re
from typing import Iterable, Callable, Tuple

from utils.methods import unique, limit, search_by_text, get_column, sort_text, regexp

Factory_type = Callable[[Iterable[str]], Iterable[str]]
Method_type = Callable[[str | None], Factory_type]
Command = Tuple[str, str | None]

METHODS_MAP: dict[str, Method_type] = {
    'filter': lambda arg: lambda iterable: search_by_text(iterable, arg or ''),
    'map': lambda arg: lambda iterable: get_column(iterable, int(arg or '0')),
    'unique': lambda arg: lambda iterable: unique(iterable),
    'sort': lambda arg: lambda iterable: sort_text(iterable, arg or ''),
    'limit': lambda arg: lambda iterable: limit(iterable, int(arg or '0')),
    'regex': lambda arg: lambda iterable: regexp(iterable, re.compile(arg or ''))
}


def parse_request(query_string: str) -> Iterable[Command]:
    cmd_list = query_string.split('|')

    for e in cmd_list:
        cmd = e.split(':')
        yield cmd[0], cmd[1] if len(cmd) > 1 else None


def get_method(method: str) -> Method_type:
    if method in METHODS_MAP:
        return METHODS_MAP[method]

    raise KeyError(f'Method {method} not found')


def methods_iterator(cmd_list: Iterable[Command]) -> Iterable[Factory_type]:
    for cmd, arg in cmd_list:
        yield get_method(cmd)(arg)


def compile_cmd(cmd_list: Iterable[Command], data: Iterable[str]) -> Iterable[str]:
    for method in methods_iterator(cmd_list):
        data = method(data)

    return data
