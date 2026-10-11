# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

def make_album(artist, title, songs=None):
    album = {"artist": artist.title(), "title": title.title()}
    if songs is not None:
        album["songs"] = songs
    return album

print(make_album("burna boy", "love damini"))
print(make_album("tems", "born in the wild"))
print(make_album("wizkid", "made in lagos", 12))
