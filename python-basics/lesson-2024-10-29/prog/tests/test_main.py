import pytest
from src.main import add


@pytest.mark.skip("for no reason really")
def test_add():
    # Arrange
    x = 2
    y = 3
    expected_result = 5

    # Act
    result = add(x, y)

    # Assert
    assert result == expected_result


@pytest.mark.xfail(reason="for no reason")  # using key-word only argument.
def test_add_two_and_one_is_not_10():
    # Arrange
    x = 2
    y = 1

    unexpected_result = 3

    # Act
    result = add(x, y)

    # Assert
    assert unexpected_result == result
