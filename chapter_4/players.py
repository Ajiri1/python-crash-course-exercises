players = ['ajiri', 'favour', 'jerry', 'naza', 'ovy']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])

print("Here are the first three players in my team")
for player in players[0:3]:
    print(player.title())