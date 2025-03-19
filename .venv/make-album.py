def make_album(album_name,band_name,quantity):
    print(f"\nWow the '{album_name.upper()}' album by {band_name.upper()} is very popular!")
    print(f"There are has {quantity} songs,that's very nice!")

while True:
    print(f"\nWhat is your favourite album?\n(enter 'q' anytime to quit)")
    album_name = input("Album name:")
    if album_name == 'q':
        break
    band_name = input("Band name:")
    if band_name == 'q':
        break
    quantity = int(input("How many songs are on this album?:"))
    if quantity == 'q':
        break

    make_album(album_name,band_name,quantity)



