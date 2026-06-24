class User(object):
    # constructor
    def __init__(self, name, password, site_url):
        self.name = name
        self.password = password
        self.url = site_url

    def login(self):
        print(f"User {self.name} was logged in {self.url}")

    def logout(self):
        print(f"User {self.name} was logged out {self.url}")

# instance creation
dev_user = User("dev_user", "dev_password", "http://dev.localhost:8080")

# atribute
print(dev_user.name)

# method
dev_user.login()
# method
dev_user.logout()

stage_user = User("stage_user", "stage_password", "http://stage.localhost:8080")
prod_user = User("prod_user", "prod_password", "http://prod.localhost:8080")

