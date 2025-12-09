class User:
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}" 
              f" is {self.age} years old" 
              f" and likes to {self.hobby}. ")

    def greet_user(self):
        print(f"Hey {self.first_name.title()}, how are you?")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Instances
user1 = User("john", "doe", 24, "workout")

# Increment login_attempt 3 times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Display login_attempt
print(user1.login_attempts)

# Reset login_attempt
user1.reset_login_attempts()
print(user1.login_attempts)
