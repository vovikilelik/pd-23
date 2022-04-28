def unique(iterable):
    return set(iterable)


def limit(iterable, length):
    inc = 0
    for item in iterable:
        inc += 1
        if length < inc:
            return

        yield item


def search_by_text(iterable, text):
    return filter(lambda e: text in e, iterable)


def extract_column(text, column_index):
    return text.split(' ')[column_index]


def get_column(iterable, column_index):
    return map(lambda e: extract_column(e, column_index), iterable)


def sort_text(iterable, direction):
    reverse = direction == 'desc'
    return sorted(iterable, reverse=reverse)
