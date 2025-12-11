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

# Instances
user1 = User("john", "doe", 24, "workout")
user2 = User("jane", "doe", 21, "sing")
user3 = User("bob", "little", 39, "golf")

if __name__ == "__main__":
    # User 1 
    user1.greet_user()
    user1.describe_user()

    # User 2 
    user2.greet_user()
    user2.describe_user()

    # User 3
    user3.greet_user()
    user3.describe_user()