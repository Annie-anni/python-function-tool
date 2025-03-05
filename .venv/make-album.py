def make_album(album_name,band_name):
    print(f"The '{album_name}' album by {band_name} is very popular!")
while True:
    print(f"\nWhat is your favourite album?\n(enter 'q' anytime to quit)")
    album_name = input("Album name:")
    if album_name == 'q':
        break
    band_name = input("Band name:")
    if band_name == 'q':
        break
    make_album(album_name,band_name)
