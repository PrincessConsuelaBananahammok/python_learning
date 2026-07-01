class User(object):
    # constructor
    def __init__(self, name, password, site_url, height):
        self.name = name
        self.password = password
        self.url = site_url
        self.finished_courses = []
        self.height = height

    # def __len__(self):
    #     return len(self.finished_courses)

    def __len__(self):
        return self.height

    def __eq__(self, other):
        if isinstance(other, User):
            return self.height == other.height
        return False

    def __gt__(self, other):
        if isinstance(other, User):
            return self.height > other.height
        return False

    def __ge__(self, other):
        if isinstance(other, User):
            return self.height >= other.height
        return False



user = User("Alex", "password", "google.com", 150)
user2 = User("Dan", "password", "google.com", 188)
user.finished_courses.append("math")
user.finished_courses.append("physics")
# print(len(user))

print(len(user))
print(len(user2))
print(user == user2)

print(user > user)
print(user < user2)