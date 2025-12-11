from login_attempts import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)
        self.privileges = Privileges()

    # def show_privileges(self):
    #     print("List of Administrator privileges:")
    #     for privilege in self.privileges:
    #         print("-", privilege)

admin_user = Admin("John", "Doe", 24, "Coding")

# Test code
if __name__ == "__main__":
    admin_user.privileges.show_privileges() 