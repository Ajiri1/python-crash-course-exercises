user_names = ['admin', 'ajiri', 'michael', 'john', 'sarah']

for user in user_names:
    if user == 'admin':
        print("Hello " + user.title() + ", would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thanks for logging in again")