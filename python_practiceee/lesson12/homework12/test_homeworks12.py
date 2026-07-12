import unittest
from python_practiceee.lesson12.homework12.homeworks import (uniq_count, take_what_you_need, sum_even_numbers,
                                                             wait_for_the_letter, multiplication_table)

class FunctionTests(unittest.TestCase):

    def test_uniq_count_positive(self):
        test_data = "Would you tell me, please, which way I ought to go from here?"
        actual_result = uniq_count(test_data)
        self.assertTrue(actual_result)

    def test_uniq_count_negative(self):
        test_data = "Hello world!"
        actual_result = uniq_count(test_data)
        self.assertFalse(actual_result)

    def test_take_what_you_need_string(self):
        test_list = ["hello", False, "world", 88]
        test_type = str
        actual_result = take_what_you_need(test_list, test_type)
        expected_result = ["hello", "world"]
        self.assertEqual(expected_result, actual_result)

    def test_take_what_you_need_string_negative(self):
        test_list = [11, False, 0.2, 88]
        test_type = str
        actual_result = take_what_you_need(test_list, test_type)
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    #   в функції take_what_you_need є бага, вона повертає True та False як 1 і 0, тест буде падати
    def test_take_what_you_need_int(self):
        test_list = ["hello", False, "world", 88]
        test_type = int
        actual_result = take_what_you_need(test_list, test_type)
        expected_result = [88]
        self.assertEqual(expected_result, actual_result)

    def test_take_what_you_need_bool(self):
        test_list = ["hello", False, "world", 88]
        test_type = bool
        actual_result = take_what_you_need(test_list, test_type)
        expected_result = [False]
        self.assertEqual(expected_result, actual_result)

    def test_take_what_you_need_bool_negative(self):
        test_list = ["hello", "world", 88]
        test_type = bool
        actual_result = take_what_you_need(test_list, test_type)
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    def test_sum_even_numbers(self):
        test_list = [88, 12, 11]
        actual_result = sum_even_numbers(test_list)
        expected_result = 100
        self.assertEqual(expected_result, actual_result)

    def test_sum_even_numbers_odd(self):
        test_list = [89, 13, 11]
        actual_result = sum_even_numbers(test_list)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_sum_even_numbers_negative(self):
        test_list = [89, -12, 10]
        actual_result = sum_even_numbers(test_list)
        expected_result = -2
        self.assertEqual(expected_result, actual_result)

    def test_sum_even_numbers_negative_text(self):
        test_list = [89, 13, 11, "hello"]
        with self.assertRaises(TypeError):
            sum_even_numbers(test_list)

    def test_wait_for_the_letter(self):
        test_letter = "w"
        test_text = "Would you tell me, please, which way I ought to go from here?"
        actual_result = wait_for_the_letter(test_letter, test_text)
        expected_result = True
        self.assertEqual(expected_result, actual_result)

    def test_wait_for_the_letter_negative(self):
        test_letter = "j"
        test_text = "Would you tell me, please, which way I ought to go from here?"
        actual_result = wait_for_the_letter(test_letter, test_text)
        expected_result = False
        self.assertEqual(expected_result, actual_result)

    def test_multiplication_table(self):
        test_number = 2
        actual_result = multiplication_table(test_number)
        expected_result = [2, 4, 6, 8, 10]
        self.assertEqual(expected_result, actual_result)

    def test_multiplication_table_high_value(self):
        test_number = 11
        actual_result = multiplication_table(test_number)
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    def test_multiplication_table_negative_value(self):
        test_number = -2
        actual_result = multiplication_table(test_number)
        expected_result = []
        self.assertEqual(expected_result, actual_result)