banned_users = ['andrew', 'carolina', 'david']
users = ['marie', 'david', 'carolina', 'andrew', 'michael']

for user in users:
    if user not in banned_users:
        print(user.title() + ", you can post a response if you wish.\n")
    else:
        print(user.title() + ", you are banned from posting a response.\n")