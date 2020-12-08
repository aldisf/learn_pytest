import pytest
import src.module
import platform
from src.module import (
    is_even_number,
    are_three_numbers_all_even,
    multiply_by_five,
    read_string_from_test_file,
    echo_variable,
)

# General
def test_is_even_number():
    assert not is_even_number(3), "3 is not an even number"
    assert not is_even_number(5), "5 is not an even number"


# Fixture
@pytest.fixture
def fixture_number():
    return 50


def test_is_multiply_by_five_fixture(fixture_number):
    # Remember to put the fixture inside the
    # test function call
    assert multiply_by_five(10) == fixture_number, "wrong multiplication"


@pytest.fixture
def fixture_input_1():
    return 5


@pytest.fixture
def fixture_input_2():
    return 10


# Test multiple fixtures in one test call
def test_multiply_two_fixtures(fixture_input_1, fixture_input_2):
    assert (
        multiply_by_five(10) == fixture_input_1 * fixture_input_2
    ), "something wrong happened"


# Parametrize
@pytest.mark.parametrize(
    "num1,num2,num3", [(2, 4, 6), (10, 16, 70), (2, 4, 6)],
)
def test_all_even_numbers_param_1(num1, num2, num3):
    assert are_three_numbers_all_even(num1, num2, num3), "something wrong happened"


# Mocking

# Variable / Constant
def test_big_odd_constant():
    assert not is_even_number(
        src.module.SOME_BIG_ODD_NUMBER
    ), "constant is not an even number"


def test_mock_constant(mocker):
    mocker.patch.object(src.module, "SOME_BIG_ODD_NUMBER", 256)
    assert is_even_number(
        src.module.SOME_BIG_ODD_NUMBER
    ), "constant is now mocked as an even number"


# Function
def test_original_unmocked_function():
    # Running with --durations --vv option should
    # return test running for 5s
    assert echo_variable(5) == 5, "function should return the same supplied value"


def test_mock_function(mocker):
    # Running with --durations --vv option should
    # return a very fast test instead of waiting for 100 seconds
    n = 5
    mocker.patch("src.module.some_long_waiting_function", return_value=n)
    assert echo_variable(n) == n, "function should return the same supplied value"


# Xfail
@pytest.mark.xfail(strict=True)
def test_should_fail():
    assert is_even_number(3)


# Skip
@pytest.mark.skip(reason="no way of testing this currently")
def test_should_skip():
    pass


# Skipif
@pytest.mark.skipif(
    platform.system() not in ("Darwin", "Linux"), reason="requires posix path structure"
)
def test_text_output():
    assert (
        read_string_from_test_file("/workspaces/learn_pytest/test_open_file.txt")
        == "this is a test file to be opened"
    ), "wrong file content"


@pytest.mark.skipif(platform.system() != "Darwin", reason="must be run in macOS")
def test_ismacos():
    assert 1 + 1 == 2
