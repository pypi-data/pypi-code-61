from typing import List, Any
def pysum(*args: List[Any]) -> Any:
    """Takes numbers ad returns their sum.

    Returns:
        Any: total of all given numbers
    """
    total = 0

    for elem in args:
        total += elem
    
    return total