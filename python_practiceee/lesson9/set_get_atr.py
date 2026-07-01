# class Person:
#     pass
#
# person = Person()

class User:
    # constructor
    def __init__(self, name, score):
        self.name = name
        self.score = score
        # if 100 >= self.score >= 0:
        #     self.score = score
        # else:
        #     print("score must be between 0 and 100. Set 0")
        #     self.score = 0

    def __str__(self):
        return f"User: {self.name}, score: {self.score}"

    def __setattr__(self, key, value):
        if key == "score":
            if not (100 >= value >= 0):
                print("score must be between 0 and 100. Set 0")
                value = 0
        super().__setattr__(key, value)


alex = User("Alex", 50)
alex.score = -50
print(alex)

# 20:39