from utils.methods import unique, limit, search_by_text, get_column, sort_text

METHODS_MAP = {
    'filter': lambda arg: lambda iterable: search_by_text(iterable, arg),
    'map': lambda arg: lambda iterable: get_column(iterable, int(arg)),
    'unique': lambda arg: lambda iterable: unique(iterable),
    'sort': lambda arg: lambda iterable: sort_text(iterable, arg),
    'limit': lambda arg: lambda iterable: limit(iterable, int(arg))
}


def parse_request(query_string):
    cmd_list = query_string.split('|')

    for e in cmd_list:
        cmd = e.split(':')
        yield cmd[0], cmd[1] if len(cmd) > 1 else None


def get_method(method):
    if method in METHODS_MAP:
        return METHODS_MAP[method]

    raise KeyError(f'Method {method} not found')


def methods_iterator(cmd_list):
    for cmd, arg in cmd_list:
        yield get_method(cmd)(arg)


def compile_cmd(cmd_list, data):
    for method in methods_iterator(cmd_list):
        data = method(data)

    return data
