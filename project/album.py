from project import song


class Album:

    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = []

    def add_songs(self, current_song):
        if current_song.single:
            return f"Cannot add {current_song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        try:
            current_s = next(filter(lambda s: s.name == current_song.name, self.songs))
            return "Song is already in the album."

        except StopIteration:
            self.songs.append(current_song)
            return f"Song {current_song.name} has been added to the album {self.name}."

    def remove_song(self, current_song):
        pass

    def publish(self):
        pass

    def details(self):
        pass
