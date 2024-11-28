import os


class Song:
    """Class represents a song
    Attributes:
        title (str): The title
        duration (int): The duration
    """

    def __init__(self, title, duration=0):
        """Song init method

        :param title: The title
        :param duration: Initial value for duration
        :return:
        """
        self.title = title
        if duration > 0:
            self._duration = duration
        else:
            self._duration = 0

    def get_title(self):
        return self.title

    name = property(get_title)

    def _get_duration(self):
        return self._duration

    def _set_duration(self, duration):
        if duration > 0:
            self._duration = duration

    duration = property(_get_duration, _set_duration)

    def __str__(self):
        return "Title: {0.name}, Duration: {0.duration}".format(self)


class Album:
    """Class represents an album

    Attributes:
        name (str): The name
        year (int): The year of publishing
        tracks (List[Song]): The songs list

    Methods:
        add_song: used to add a song
    """

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.tracks = []

    def add_song(self, song, duration=0, position=None):
        """Add a song

        Args:
            song (Song): A song to be added
            position (Optional[int]): position
            duration (int): duration of the song
        """
        new_song = find_object(song, self.tracks)
        if new_song is None:
            new_song = Song(song)
            new_song.duration = duration
            if position is None:
                self.tracks.append(new_song)
            else:
                self.tracks.insert(position, song)


class Artist:
    """Basic artist info

    Attributes:
        name (str): The name
        albums (List[Album)] A list of albums by this artist
    Methods:
        add_album: used to add album
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Adds an album
        Args:
            album (Album): the album object
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Add a new song"""
        new_album = find_object(name, self.albums)
        if new_album is None:
            new_album = Album(name, year)
            self.add_album(new_album)
        new_album.add_song(title)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    print(f"Current dir: {os.getcwd()}")

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print(f"{artist_field}, {album_field}, {year_field}, {song_field}")

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

        return artist_list


def create_check_file(artist_list):
    with open("checkfile.txt", "w") as check_file:
        for artist in artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(artist, album, song), file=check_file)


if __name__ == "__main__":
    a_list = load_data()
    print(len(a_list))
    create_check_file(a_list)
