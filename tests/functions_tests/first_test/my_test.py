import unittest
from python_practiceee.lesson12.func import some_function

def sum_two_numbers(a, b):
    return a + b

class MyTest(unittest.TestCase):

    def test_example(self):
        actual_result = sum_two_numbers(1, 2)
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def test_example_second(self):
        actual_result = sum_two_numbers(1, 2)
        expected_result = 3
        self.assertEqual(expected_result, actual_result)
        # assert actual_result == expected_result

    def test_example_third(self):
        actual_result = [{"Name": "Alex", "Age": 18, "Position" : "QA"},
                         {"Name": "Den", "Age": 18, "Position" : "AQA"},
                         {"Name": "Alex", "Age": 99, "Position" : "Dev"}]
        expected_result = [{"Name": "Alex", "Age": 18, "Position" : "AQA"},
                         {"Name": "Den", "Age": 22, "Position" : "AQA"},
                         {"Name": "Den", "Age": 99, "Position" : "Dev"}]
        self.assertEqual(expected_result, actual_result)
        # assert actual_result == expected_result
#
# if __name__ == '__main__':
#     unittest.main(verbosity=0)