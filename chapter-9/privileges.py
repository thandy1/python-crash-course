class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "can add post",
                "can delete post",
                "can ban user"
                ]
        self.privileges = privileges

    def show_privileges(self):
        print("List of Administrator privileges:")
        for privilege in self.privileges:
            print("-", privilege)

# Refer to admin.py