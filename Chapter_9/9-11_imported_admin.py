# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

# In a multi-file project, place User and Admin in a separate module and import them.
class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.privileges = ["can add post", "can delete post", "can ban user"]

if __name__ == "__main__":
    admin = Admin("favour")
    print(admin.username)
    print(", ".join(admin.privileges))
