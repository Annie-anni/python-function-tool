class User:
    def __init__(self,first_name,last_name,gender,age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(f"Name:{self.first_name.title()} {self.last_name}\nGender:{self.gender}\nAge:{self.age}")
    def greet_user(self):
        print(f"Hey {self.first_name.title()} {self.last_name}!")
    def read_login_attempts(self):
        print(f"Login attempts:{self.login_attempts}")
    def set_login_attempts(self,login_attempts):
        self.login_attempts = login_attempts
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
user = User('liu','dan','female',20)
user.describe_user()
user.greet_user()
user.login_attempts = 1
user.read_login_attempts()
user.set_login_attempts(2)
user.increment_login_attempts()
user.read_login_attempts()
user.reset_login_attempts()
user.read_login_attempts()

