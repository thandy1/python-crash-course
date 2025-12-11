from priv_class import Privileges
from user_class import User
class Admin(User):
    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)
        self.privileges = Privileges()