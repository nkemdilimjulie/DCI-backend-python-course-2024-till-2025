import unittest

from text import to_upper


class TestConvention(unittest.TestCase):
    def test_to_upper_return_all_uppercase(self):
        # Arrange
        x = "abcde"
        expected_result = "ABCDE"

        # Act
        result = to_upper(x)

        # assert
        self.assertEqual(expected_result, result)
