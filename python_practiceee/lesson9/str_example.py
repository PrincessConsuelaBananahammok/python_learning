class User(object):
    # constructor
    def __init__(self, name, password, site_url):
        self.name = name
        self.password = password
        self.url = site_url

    def __str__(self):
        return f'{self.name}, {self.password}, {self.url}'

    def __repr__(self):
        return f'User: (name={self.name}, password={self.password}, url={self.url})'


user = User("Alex", "password", "google.com")
# print(user)


print(repr(user))

import logging
logging.error(repr(user))