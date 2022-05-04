import re
from re import Pattern
from typing import Iterable, Optional, Callable, Literal


def unique(iterable: Iterable) -> Iterable:
    return set(iterable)


def limit(iterable: Iterable[str], length: int) -> Iterable[str]:
    inc = 0
    for item in iterable:
        inc += 1
        if length < inc:
            return

        yield item


def search_by_text(iterable: Iterable[str], text: str) -> Iterable[str]:
    return filter(lambda e: text in e, iterable)


def extract_column(text: str, column_index: int) -> str:
    return text.split(' ')[column_index]


def get_column(iterable: Iterable[str], column_index: int) -> Iterable[str]:
    return map(lambda e: extract_column(e, column_index), iterable)


def sort_text(iterable: Iterable[str], direction: str) -> Iterable[str]:
    reverse = direction == 'desc'
    return sorted(iterable, reverse=reverse)


def match_pattern(text: str, expression: Pattern) -> Optional[str]:
    result = expression.search(text)
    return result.group(0) if result else None


def filter_map(iterable: Iterable[str], func: Callable[[str], str | None | Literal[False]]) -> Iterable[str]:
    for item in iterable:
        result = func(item)

        if not result:
            continue

        yield str(result)


def regexp(iterable: Iterable[str], expression: Pattern) -> Iterable[str]:
    return filter_map(iterable, lambda text: match_pattern(text, expression))
