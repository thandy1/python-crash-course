def make_album(artist_name, album_title, num_songs=None):
    album = {}
    album["artist"] = artist_name
    album["title"] = album_title
    if num_songs is not None:
        album["tracks"] = int(num_songs)
    return album

while True:
    artist_name = input("Enter the name of the artist ('q' to quit): ")
    if artist_name.lower() == 'q':
        break

    album_title = input("Enter the name of the artist's album title ('q' to quit): ")
    if album_title.lower() == 'q':
        break

    num_songs = input("Enter a number of tracks ('q' to quit or 'Enter' for None): ")
    if num_songs.lower() == 'q':
        break

    if num_songs == "":
        num_songs = None

    print(make_album(artist_name, album_title, num_songs))
    