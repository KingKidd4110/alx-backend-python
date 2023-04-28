#!/usr/bin/env python3
""" add type annotations to the function """
from typing import Any, Union, Mapping, Optional, TypeVar


T = TypeVar('T')


def safety_get_value(dct: Mapping, key: Any,
                     default: Optional(T) = None) Union[Any, T]:
    """ return values """
    if key in dct:
        return dct[key]
    else:
        return default
