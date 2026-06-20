# def sum_all_elements(list_elements):
#     return sum(list_elements)
# print(sum_all_elements([1, 2, 3, 4, 5]))

# def sum_all_elements(number1, number2, number3, number4):
#     return sum([number1, number2, number3, number4])
# print(sum_all_elements(1, 2, 3, 4))

# *args
# kwargs
def sum_all_elements(double_arg, *args, ignor_arg=5, **kwargs):
    print("double_arg: ", double_arg)
    print("Numbers: ", args)
    print("Ignor arg: ", ignor_arg)
    print("kwargs: ", kwargs)
    numbers = [k for k in args if k != ignor_arg]
    # result = sum(numbers) + double_arg * 2
    # if kwargs.get("double_all") == True:
    #     result = result * 2
    # return result
    return sum(numbers) + double_arg * 2

my_arguments = {"arg1": "value", "double_all": True, "additional_li": [1,2,3]}
print(sum_all_elements(**my_arguments))
# print(sum_all_elements(1, 2, 3, 4, 5, * [23, 3, 4], ignor_arg=5))
print(sum_all_elements(1, 2, 3, 4, 5, *[23, 3, 4], 5))
# print(sum_all_elements(1, 2, 3, 4, 5, *[23, 3, 4], ignor_arg=5, double_all=True))

my_arguments = {"arg1": "value", "double_all": True, "additional_li": [1,2,3]}
print(sum_all_elements(1, 2, 3, 4, 5, *[23, 3, 4], ignor_arg=5, **my_arguments))
