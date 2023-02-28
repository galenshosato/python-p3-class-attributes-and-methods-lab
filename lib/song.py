class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        self.__class__.add_to_genre_count([self])
        self.__class__.add_to_artist_count([self])
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, songs):
        for song in songs:
            if song.genre in cls.genre_count:
                cls.genre_count[song.genre] += 1
            else:
                cls.genre_count[song.genre] = 1
        

    @classmethod
    def add_to_artist_count(cls, singers):
        for singer in singers:
            if singer.artist in cls.artist_count:
                cls.artist_count[singer.artist] += 1
            else:
                cls.artist_count[singer.artist] = 1


if __name__ == '__main__':
    violet_hill = Song("Violet Hill", "Coldplay", "Pop")
    paper_cut = Song("Paper Cut", "Linkin Park", "Pop")
    holiday = Song("Holiday", "Green Day","Pop")
    print(Song.artists)