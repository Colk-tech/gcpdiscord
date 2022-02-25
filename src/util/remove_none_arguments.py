from typing import Tuple, List, Dict

import copy


def remove_none_arguments(*args, **kwargs) -> Tuple[Tuple, Dict]:
    positional_args: List = list(copy.copy(args))
    keyword_args: Dict = kwargs.copy()

    for i, positional_arg in enumerate(positional_args):
        if positional_arg is None:
            positional_args.pop(i)

    for key, value in kwargs.items():
        if value is None:
            del keyword_args[key]

    return tuple(positional_args), keyword_args
