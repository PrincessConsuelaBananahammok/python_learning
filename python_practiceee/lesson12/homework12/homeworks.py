def uniq_count(text):
    count = len(set(text))
    if count > 10:
        return True
    else:
        return False


def take_what_you_need(lst, typ):
    result = [el for el in lst if isinstance(el, typ)]
    return result


def sum_even_numbers(list_of_numbers):
    sum_of_numbers = 0
    for num in list_of_numbers:
        if num % 2 == 0:
            sum_of_numbers += num
    return sum_of_numbers


def wait_for_the_letter(letter, text):
    iteration = 1
    while len(text) >= iteration:
        if letter.lower() in text or letter.upper() in text:
            return True
        iteration += 1
    return False


def multiplication_table(number):
    multiplier = 1
    result_list = []
    if number <= 0:
        return result_list
    while multiplier * number <= 10:
        result = number * multiplier
        result_list.append(result)
        multiplier += 1
    return result_list
