class User:
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}" 
              f" is {self.age} years old" 
              f" and likes to {self.hobby}. ")

    def greet_user(self):
        print(f"Hey {self.first_name.title()}, how are you?")