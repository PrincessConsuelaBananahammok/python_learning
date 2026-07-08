user = [
    {"name": "Alex", "math": 22, "philosophy": 44},
    {"name": "Bob", "math": 25, "philosophy": 44},
    {"name": "Carol", "math": 25, "philosophy": None}
]

def test_count_score(user_list):
    for k in user_list:
        # if k["philosophy"] is None:
        #     continue
        try:
            assert k["math"] + k["philosophy"] > 0
            print(k["name"], k["math"] + k["philosophy"])
            print("Test passed")
        except TypeError as e:
            print(f"can`n get correct data for {k}")
            print(e)
        except KeyError as key:
            print(f"No key{k} in file. It`s a bug")
            print("Test failed")



test_count_score(user)

# assert 1==1
#  check True if not true raise AssertionError

# assert False