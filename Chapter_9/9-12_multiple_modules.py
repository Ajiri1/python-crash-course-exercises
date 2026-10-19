# Demonstrates a simple module-style separation using classes in this file.
class User:
    def __init__(self, username):
        self.username = username

class Privileges:
    def __init__(self, privileges=None):
        self.privileges = privileges or ["can add post", "can delete post", "can ban user"]

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.privileges = Privileges()

if __name__ == "__main__":
    admin = Admin("favour")
    print(admin.username)
    for privilege in admin.privileges.privileges:
        print(privilege)
