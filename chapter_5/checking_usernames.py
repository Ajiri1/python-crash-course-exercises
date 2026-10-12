current_users = ['admin', 'ajiri', 'michael', 'john', 'sarah']
new_users = ['ADMIN', 'john', 'Sarah', 'david', 'carolina']

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print("Sorry, the username '" + new_user + "' has already been used.")
    else:
        print("The username '" + new_user + "' is available.")