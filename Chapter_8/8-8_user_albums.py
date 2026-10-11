# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

def make_album(artist, title, songs=None):
    album = {"artist": artist.title(), "title": title.title()}
    if songs is not None:
        album["songs"] = songs
    return album

while True:
    print("\nEnter album details (or type q to quit).")
    artist = input("Artist: ")
    if artist.lower() == "q":
        break
    title = input("Album title: ")
    if title.lower() == "q":
        break
    count = input("Number of songs (optional): ")
    songs = int(count) if count.isdigit() else None
    print(make_album(artist, title, songs))
