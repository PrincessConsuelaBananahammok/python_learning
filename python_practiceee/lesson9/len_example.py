class User(object):
    # constructor
    def __init__(self, name, password, site_url):
        self.name = name
        self.password = password
        self.url = site_url
        self.finished_courses = []

    def __len__(self):
        return len(self.finished_courses)



user = User("Alex", "password", "google.com")
user.finished_courses.append("math")
user.finished_courses.append("physics")
print(len(user))