import unittest

from src.calc import MathematicalError, multiply


class TestMultiplicationTestCase(unittest.TestCase):
    def test_mul_two_numbers(self):
        # Arrange
        x = 4
        y = 3
        expected_result = 12

        # Act
        result = multiply(x, y)

        # Assert
        # Later, we will use unittest methods to assert
        assert (
            result == expected_result
        ), f"Expected {expected_result}, but got {result}"

    def test_mul_with_str_numbers(self):
        # Arrange
        x = "4"
        y = "2"
        expected_result = 8

        # Act
        result = multiply(x, y)

        # if expected_result != result:
        #     self.fail('This has failed')
        # else:
        #     pass

        # assert
        self.assertEqual(
            result, expected_result, f"Expected {expected_result}, but got {result}"
        )

        # self.assertTrue(result == expected_result, f"Expected {expected_result}, but got {result}")
        # assert (
        #     result == expected_result
        # ), f"Expected {expected_result}, but got {result}"

    def test_mul_raises_mathematicalError(self):
        # Arrange
        x = "4a"
        y = 5
        expected_error_msg = "Not supported types or values"

        # Act
        with self.assertRaises(MathematicalError) as ex:
            multiply(x, y)

        # Test the error message
        # ex.args[0] -> try-except
        # ex.exception.args[0] -> with self.assertRaises
        self.assertEqual(expected_error_msg, ex.exception.args[0])


if __name__ == "__main__":
    unittest.main()
