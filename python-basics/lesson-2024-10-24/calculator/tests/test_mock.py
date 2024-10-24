import unittest
from unittest.mock import patch

from src.calc import addition, ask_username, multiply_2


class MockingTestCase(unittest.TestCase):
    def test_addition_passed(self):
        # Arrange
        x = 1
        y = 4
        z = 2
        expected_result = 7

        # Act
        result = addition(x, y, z)

        # Assert
        self.assertEqual(
            expected_result, result, f"Expected {expected_result}, but got {result}"
        )

    def test_addition_incorrect_input(self):
        # Arrange
        x = []
        y = "4"

        with self.assertRaises(TypeError):
            addition(x, y)

    # Use `patch` as a decorator
    # Specify patch to the function to mock
    @patch("src.calc.addition")
    def test_multiply_2_passed(self, addition_mock):
        # Arrange
        x = 1
        y = 3
        expected_result = 3
        ## define the behavior of our mock
        ### Specify a return value for our mock
        # side_effect
        ## - When given an iterable, it will return each item each time it is called
        ## - When given a exception, it will raise that exception when it is called.
        addition_mock.side_effect = [1, 2, 3]
        # addition_mock.side_effect = TypeError
        # addition_mock.return_value = 2

        # Act
        result = multiply_2(x, y)

        # Assert
        self.assertEqual(
            expected_result, result, f"Expected {expected_result}, but got {result}"
        )

    # use patch with the `with statement`
    def test_multiply_2_with_incorrect_input(self):
        # Arrange
        x = "4"  # numb1
        y = 4  # numb2

        with patch("src.calc.addition") as addition_mock:
            addition_mock.side_effect = TypeError

            with self.assertRaises(TypeError):
                multiply_2(x, y)

    @patch("src.calc.input")
    def test_ask_username_passed(self, input_mock):
        # Arrange
        expected_name = "kevin"
        input_mock.return_value = "kevin"

        # Act
        result = ask_username()

        # Assert
        self.assertEqual(expected_name, result)

        # Check how many times the mock was called
        # Check with whom argument the mock was called
        input_mock.assert_called_once_with("Enter your name: ")
