import unittest

from functions import generate_random_list, multiply, even_odd, string_concat, element_in_list, factorial, count_evens

LIST_LENGTH = 10000

class TestGenerateRandomList(unittest.TestCase):
    def test_length(self):
        """Test if the list has the correct length."""
        result = generate_random_list(LIST_LENGTH)
        self.assertEqual(len(result), LIST_LENGTH)

    def test_randomness(self):
        """Test if the list contains random values."""
        result1 = generate_random_list(LIST_LENGTH)
        result2 = generate_random_list(LIST_LENGTH)
        self.assertNotEqual(result1, result2, "Two generated lists are unexpectedly identical.")

    def test_value_range(self):
        """Test if the list values are within the expected range."""
        result = generate_random_list(LIST_LENGTH)
        for value in result:
            self.assertTrue(-100 <= value <= 100, "Value out of range -100-100.")

    def test_empty_list(self):
        """Test if an empty list is returned for length 0."""
        result = generate_random_list(0)
        self.assertEqual(result, [], "List is not empty for length 0.")

class TestMultiplyFunction(unittest.TestCase):
    def test_result_length(self):
        """Test if the result list length is less than or equal to the input list."""
        result = multiply(LIST_LENGTH)
        self.assertLessEqual(len(result), LIST_LENGTH)

    def test_multiplication(self):
        """Test if the elements are correctly multiplied by 2."""
        result = multiply(LIST_LENGTH)
        for item in result:
            self.assertTrue(item % 2 == 0, "Element is not a multiple of 2.")

    def test_positive_numbers(self):
        """Test if the result only contains positive numbers."""
        result = multiply(LIST_LENGTH)
        for item in result:
            self.assertGreater(item, 0, "Element is not positive.")


class TestEvenOddFunction(unittest.TestCase):
    def test_even_odd_counts(self):
        """Test if the counts of even and odd numbers add up to the list length."""
        odd_count, even_count = even_odd(LIST_LENGTH)
        self.assertEqual(odd_count + even_count, LIST_LENGTH)

    def test_negative_length(self):
        """Test function behavior for a negative length."""
        odd_count, even_count = even_odd(-5)
        self.assertEqual((odd_count, even_count), (0, 0), "Counts should be zero for negative length.")

    def test_zero_length(self):
        """Test function behavior for zero length."""
        odd_count, even_count = even_odd(0)
        self.assertEqual((odd_count, even_count), (0, 0), "Counts should be zero for zero length.")

class TestStringConcatFunction(unittest.TestCase):
    def test_string_length(self):
        """Test if the string length is correct."""
        result = string_concat(LIST_LENGTH)
        expected_length = sum(len(str(i)) for i in range(LIST_LENGTH))
        self.assertEqual(len(result), expected_length)

    def test_string_content(self):
        """Test if the string content is as expected."""
        result = string_concat(LIST_LENGTH)
        expected_string = ''.join(str(i) for i in range(LIST_LENGTH))
        self.assertEqual(result, expected_string)

    def test_negative_length(self):
        """Test function behavior for a negative length."""
        result = string_concat(-5)
        self.assertEqual(result, "", "String should be empty for negative length.")

    def test_zero_length(self):
        """Test function behavior for zero length."""
        result = string_concat(0)
        self.assertEqual(result, "", "String should be empty for zero length.")


class TestElementInListFunction(unittest.TestCase):
    def test_element_presence(self):
        """Test if the function returns True when length is greater than 1."""
        result = element_in_list(LIST_LENGTH)
        self.assertTrue(result, "Function should return True for length > 1.")

    def test_length_one(self):
        """Test function behavior for a list of length one."""
        result = element_in_list(1)
        self.assertFalse(result, "Function should return False for length 1.")

    def test_zero_length(self):
        """Test function behavior for zero length."""
        result = element_in_list(0)
        self.assertFalse(result, "Function should return False for zero length.")

    def test_negative_length(self):
        """Test function behavior for a negative length."""
        result = element_in_list(-5)
        self.assertFalse(result, "Function should return False for negative length.")

class TestFactorialFunction(unittest.TestCase):
    def test_known_values(self):
        """Test factorial for known values."""
        known_values = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
        for n, expected in known_values.items():
            result = factorial(n)
            self.assertEqual(result, expected, f"Factorial of {n} should be {expected}.")
    def test_large_number(self):
        result = factorial(1000-100)
        self.assertGreater(result, 0)

    def test_negative_input(self):
        """Test factorial for a negative input."""
        with self.assertRaises(RecursionError):
            factorial(-1)

class TestCountEvensFunction(unittest.TestCase):
    def test_even_numbers(self):
        """Test with a list of even numbers."""
        self.assertEqual(count_evens([2, 4, 6, 8]), 4)

    def test_odd_numbers(self):
        """Test with a list of odd numbers."""
        self.assertEqual(count_evens([1, 3, 5, 7]), 0)

    def test_mixed_numbers(self):
        """Test with a mix of even and odd numbers."""
        self.assertEqual(count_evens([1, 2, 3, 4, 5, 6]), 3)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(count_evens([]), 0)

    def test_long_list(self):
        """Test with an empty list."""
        list = generate_random_list(LIST_LENGTH)
        self.assertTrue(count_evens(list) > 0)


# Run the tests
if __name__ == '__main__':
    unittest.main()
