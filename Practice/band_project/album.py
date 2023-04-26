class Album:

    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = [*self.args]

    def add_song(self, current_song):
        if current_song.single:
            return f"Cannot add {current_song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        try:
            next(filter(lambda s: s.name == current_song.name, self.songs))
            return "Song is already in the album."

        except StopIteration:
            self.songs.append(current_song)
            return f"Song {current_song.name} has been added to the album {self.name}."

    def remove_song(self, current_song):
        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            found_song = next(filter(lambda s: s.name == current_song, self.songs))
            self.songs.remove(found_song)
            return f"Removed song {current_song} from album {self.name}."

        except StopIteration:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        for current_song in self.songs:
            result.append(f"== {current_song.get_info()}")

        return "\n".join(result)



