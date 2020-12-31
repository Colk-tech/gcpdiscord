from typing import Optional

from src.operations.help import Help
from src.operations.status import Status


def get_operation(key: str) -> Optional[type]:
    operations = [Help, Status]

    for operation in operations:
        if operation.MY_INDEX == key:
            return operation

    return None
