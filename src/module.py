from src.constants import SOME_BIG_ODD_NUMBER
import time


def is_even_number(num: int) -> bool:
    """
    Will be used in demonstrating:
    - Test in general
    - mock (change SOME_BIG_ODD_NUMBER)
    """
    if num % 2 == 0:
        return True
    return False


def multiply_by_five(num: int) -> int:
    return num * 5


def are_three_numbers_all_even(num1: int, num2: int, num3: int) -> bool:
    """
    Will be used in demonstrating:
    - Parametrize
    """
    if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
        return True
    return False


def read_string_from_test_file(filepath):
    """
    Will be used in demonstrating:
    - skipif
    """
    try:
        f = open(filepath, "r")
        return f.read()
    except Exception:
        return "file cannot be opened"


def some_long_waiting_function(n):
    """
    Will be used in demonstrating:
    - mock
    """
    time.sleep(n)
    return n


def echo_variable(n):
    """
    Will be used in demonstrating:
    - mock
    """
    output = some_long_waiting_function(n)
    return output
