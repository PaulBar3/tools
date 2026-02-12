"""
Описание предназначения модуля.

Нюансы.

Информация
"""

from tools import *
import time
    """_summary_
    """

def is_palindrome(text: str) -> bool:
    """_summary_

    Args:
        text (str): _description_

    Returns:
        bool: _description_
    """
    return text == text[::-1]


print(is_palindrome.__doc__)
