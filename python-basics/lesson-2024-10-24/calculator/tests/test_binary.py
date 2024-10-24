# TODO: Put your test here
import unittest

from src.calc import BinaryConverter, NotBinaryError


class TestBinaryConverter(unittest.TestCase):
    def setUp(self) -> None:
        print("\nsetUp running...")
        self.binary_converter_obj = BinaryConverter()

    def test_convert_to_binary_return_correct_result(self):
        # Arrange
        binary = "101"
        expected_decimal = 5

        # Act
        result = self.binary_converter_obj.convert_to_decimal(binary)

        # Assert
        self.assertEqual(
            expected_decimal, result, f"Expected {expected_decimal}, but got {result}"
        )

    def test_convert_to_binary_raise_error_for_non_binary(self):
        # Arrange
        binary = "01a"

        # Act
        with self.assertRaises(NotBinaryError):
            self.binary_converter_obj.convert_to_decimal(binary)

        print("test done")

    def tearDown(self) -> None:
        print("Cleaning up.....")
