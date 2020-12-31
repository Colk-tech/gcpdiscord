from typing import Optional

from src.operations.help import Help


def get_operation(key: str) -> Optional[type]:
    operations = [Help]

    for operation in operations:
        if operation.MY_INDEX == key:
            return operation

    return None
