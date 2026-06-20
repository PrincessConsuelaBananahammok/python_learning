def greeting(first_name: str, second_name: str) -> None:
    print("Hello " + first_name + " " + second_name)

# for full_name in [("Oleg", "Rudyk"), ("John", "Dow")]:
#     greeting(full_name[0], full_name[1])

for full_name in [("Oleg", "Rudyk"), ("John", "Dow")]:
    greeting(first_name=full_name[0], second_name=full_name[1])


def get_greeting(first_name: str, second_name: str) -> str:
    """
    This is DOC string example
    :param first_name: user firts name
    :param second_name: user second name
    :return: full greeting
    """
    return f"Hello {first_name}, {second_name}"