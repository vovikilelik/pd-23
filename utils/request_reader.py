from utils.methods import unique, limit, search_by_text, get_column, sort_text

METHODS_MAP = {
    'filter': lambda arg: lambda iterable: search_by_text(iterable, arg),
    'map': lambda arg: lambda iterable: get_column(iterable, int(arg)),
    'unique': lambda arg: lambda iterable: unique(iterable),
    'sort': lambda arg: lambda iterable: sort_text(iterable, bool(arg)),
    'limit': lambda arg: lambda iterable: limit(iterable, int(arg))
}


def read_value(data, name):
    if name in data:
        return data[name]


def parse_request(data):
    inc = 1
    while f'cmd{inc}' in data:
        yield data[f'cmd{inc}'], read_value(data, f'value{inc}')
        inc += 1


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
