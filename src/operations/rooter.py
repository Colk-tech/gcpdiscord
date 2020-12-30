from typing import Optional


def get_operation(key: str) -> Optional[type]:
    operations = []

    for operation in operations:
        if operation.MY_INDEX == key:
            return operation

    return None
