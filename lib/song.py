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
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists(self.artist)
    
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
    def add_to_genre_count(cls, new_genre):
        if new_genre in cls.genres:
            cls.genre_count[new_genre] += 1
        

    @classmethod
    def add_to_artist_count(cls, artist):
        pass


if __name__ == '__main__':
    violet_hill = Song("Violet Hill", "Coldplay", "Pop")
    paper_cut = Song("Paper Cut", "Linkin Park", "Pop")
    holiday = Song("Holiday", "Green Day","Pop")
    print(Song.genre_count)