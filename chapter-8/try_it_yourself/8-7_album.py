def make_album(artist_name, album_title, num_songs=None):
    album = {}
    album["artist"] = artist_name
    album["title"] = album_title
    if num_songs:
        album["tracks"] = num_songs
    return album

print(make_album("Drake", "Views"))
print(make_album("Eminem", "Recovery"))
print(make_album("Deftones", "Change", 3))

