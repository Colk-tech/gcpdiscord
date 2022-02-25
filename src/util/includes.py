from typing import List


def includes(search_from: List[iter], query: List[iter]):
    for elem in search_from:
        if elem in query:
            return True

    return False
