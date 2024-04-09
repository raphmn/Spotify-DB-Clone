from sqlite3 import *

connexion = connect('C:/Users/Raph/Documents/GitHub/Spotify-DB-Clone/database/sqlite.db')
request = connexion.cursor()


def search_from_nationality(nationality):
    return [artiste for artiste in
            request.execute(f"SELECT nomArtiste from Artiste where nationalite = '{nationality}'")]


def album_from_artist():
    return [album for album in request.execute("SELECT nomArtiste, nomAlbum from Artiste NATURAL JOIN Album")]


def album_from_style(style):
    return [album for album in
            request.execute(f"SELECT nomArtiste, nomAlbum from Artiste NATURAL JOIN Album WHERE style = '{style}'")]


def album_from_song(song):
    return (album for album in
            request.execute(f"SELECT nomAlbum from Album NATURAL JOIN Morceau WHERE nomMorceau = '{song}'"))


def update_artists(listeArtiste):
    request.execute('SELECT * from Artiste')
    for artiste in request:
        if artiste not in listeArtiste:
            listeArtiste[artiste[0]] = artiste[1:]
    return listeArtiste


def update_albums(listeAlbum):
    request.execute('SELECT * from Album')
    for album in request:
        if album not in listeAlbum:
            listeAlbum[album[0]] = album[1:]
    return listeAlbum


Artistes = {}
update_artists(Artistes)

Albums = {}
update_albums(Albums)

print(Artistes)
print(Albums)