#!/usr/bin/env python3
""" Duck typing """
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ correct duck-typed annotations: """
    if lst:
        return lst[0]
    else:
        return None
