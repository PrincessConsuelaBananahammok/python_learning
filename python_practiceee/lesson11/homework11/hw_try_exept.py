
new_item = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def sum_of_elements(some_list):
    for element in some_list:
        element = element.split(',')
        total = 0
        try:
            for item in element:
                total += int(item)
            print(total)
        except ValueError:
            print("Can`t add those elements")



sum_of_elements(new_item)

