import pytest
from src.main import add

# -- without parameterization


def test_add_single():
    for x, y, expected_result in [(3, 2, 5), (-3, -2, -5), (-3, 2, -1)]:
        result = add(x, y)

        assert expected_result == result


# With parameterization
@pytest.mark.parametrize("x, y, ex_result", [(3, 2, 5), (-3, -2, -5), (-3, 2, -1)])
def test_add_parametrize(x, y, ex_result):
    result = add(x, y)
    assert ex_result == result
