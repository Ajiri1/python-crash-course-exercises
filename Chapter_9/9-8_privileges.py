# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

class User:
    def __init__(self, username):
        self.username = username

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.privileges = Privileges()

admin = Admin("favour")
print(f"Admin: {admin.username}")
admin.privileges.show_privileges()
