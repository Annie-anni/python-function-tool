class User:
    def __init__(self,first_name,last_name,gender,age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(f"\nName:{self.first_name.title()} {self.last_name.title()}\nGender:{self.gender}\nAge:{self.age}")

    def greet_user(self):
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}!")

    def read_login_attempts(self):
        print(f"Login attempts:{self.login_attempts}")

    def set_login_attempts(self,login_attempts):
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f'-{privilege}')

class Admin(User):
    def __init__(self,first_name,last_name,gender,age):
        super().__init__(first_name,last_name,gender,age)
        self.privileges =Privileges(['can add post','can delete post','can ban user'])

    def greet_user(self):
        print(f"\nHello MR Admin ! :D {self.first_name.title()} {self.last_name.title()}!")


user = User('liu','dan','female',20)
user.describe_user()
user.greet_user()
user.login_attempts = 1
user.read_login_attempts()
user.set_login_attempts(2)
user.increment_login_attempts()
user.read_login_attempts()
user.reset_login_attempts()

admin = Admin('liu','dan','female',27)
admin.greet_user()
admin.describe_user()
admin.privileges.show_privileges()
