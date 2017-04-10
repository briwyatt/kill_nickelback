songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}


good_songs = {artist for artist in songs if 'Nickelback' not in artist}
print(str(good_songs))