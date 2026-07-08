users = [
    {"name": "Alex", "scores": {"math": 0, "philosophy": 33}},
    {"name": "Bob", "scores": {"math": 0, "philosophy": 77}},
    {"name": "Cathy", "scores": {"math": 0, "philosophy": 55, "literature": None}},
    {"name": "Daniel", "scores": {}}
]

def get_user_score(user):
    scores = user.get("scores")
    sum_ = 0
    for s in scores:
        try:
            sum_ += scores[s]
        except TypeError:
            print(f"Get None for {s}")
    try:
        result = sum_ / len(scores)
    except ZeroDivisionError:
        print(f"No data for user {user['name']}")
        return 0
    finally:
        print(f"Finally: user has score: {sum_}")
    return result

for user in users:
    print(f"User name is {user['name']}")
    print(f"User score is {get_user_score(user)}")
    print("-" * 80)