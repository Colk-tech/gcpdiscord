from typing import List

from src.discord.operations.help import Help
from src.discord.operations.list import StatusList
from src.discord.operations.status import Status
from src.discord.operations.start import Start
from src.discord.operations.stop import Stop

# Real Signature: List[class extends src.discord.operations.abs.AbstractOperation]
OPERATIONS: List[type] = [
    Help,
    StatusList,
    Status,
    Start,
    Stop
]
