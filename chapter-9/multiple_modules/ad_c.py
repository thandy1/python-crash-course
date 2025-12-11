from priv_c import Privileges
from user_c import User
class Admin(User):
    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)
        self.privileges = Privileges()