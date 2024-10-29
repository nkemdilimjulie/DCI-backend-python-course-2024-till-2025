import pytest


# Fixture
@pytest.fixture()  # by default, the scope=function
def data_set():
    # Prepare data ready for testing
    print("\n setUp....")
    yield list(range(10))
    print("\n tearDown....")


# Test
# If a fixture exist with the same name as the paramter,
# pytest will evaluate it to the return value of the fixture function
def test_data_len(data_set):
    assert len(data_set) == 10
