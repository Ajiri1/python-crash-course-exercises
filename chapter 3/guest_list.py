guest_list = ['naza', 'jerry', 'meso']
print("I'm inviting you " + guest_list[0].title() + " to a dinner at my place tonight")
print("I'm inviting you " + guest_list[1].title() + " to a dinner at my place tonight")
print("I'm inviting you " + guest_list[2].title() + " to a dinner at my place tonight")

print(guest_list[1].title() + " can't make it to the dinner")

guest_list[1] = 'Ovy'
print("I'm inviting you " + guest_list[0].title() + " to a dinner at my place tonight")
print("I'm inviting you " + guest_list[1].title() + " to a dinner at my place tonight")
print("I'm inviting you " + guest_list[2].title() + " to a dinner at my place tonight")

print("I have found a bigger table")
guest_list.insert(0, 'fav')
guest_list.insert(0, 'daniel')
guest_list.append('junior')

print(guest_list)

print("I can invite only two people for dinner")

guest_list = ['naza', 'meso', 'jerry', 'ajiri', 'ovy']

while len(guest_list) > 2:
    popped_guest = guest_list.pop()
    print("sorry " + popped_guest.title() + " I can't invite you")

print(guest_list)
for guest in guest_list:
    print(guest + ", you are still invited")


print(len(guest_list))