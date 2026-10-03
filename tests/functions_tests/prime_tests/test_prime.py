# щоб запусти pytest, файл, клас та функція мають містити test в назві
import os

import allure
import pytest

from constants import BASE_PROJECT_PATH
from python_practiceee.lesson22 import test_functions

# class TestPrimePositive:
#     def test_prime(self):
#         primes_list = test_functions.find_primes(3)
#         assert primes_list == [2, 3]
#
# def test_prime_second():
#     primes_list = test_functions.find_primes(10)
#     assert primes_list == [2, 3, 5, 7]

#
@pytest.mark.prime
class TestPrimePositive:

    @allure.epic("Unit")
    @pytest.mark.parametrize("input_value,expected_result", [
        (3, [2, 3]),
        (10, [2, 3, 5, 7]),
        (11, [2, 3, 5, 7, 11]),
        (5, [2, 3, 5])
    ])
    def test_prime(self, input_value, expected_result):
        with open(f"{os.path.join(BASE_PROJECT_PATH, 'results', str(input_value))}.txt", "w") as f:
            f.write("test results")
        primes_list = test_functions.find_primes(input_value)
        assert primes_list == expected_result