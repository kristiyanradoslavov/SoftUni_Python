import math


class PhotoAlbum:
    MAX_PAGE_COUNT = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        number_of_pages = math.ceil(photos_count / cls.MAX_PAGE_COUNT)

        return cls(number_of_pages)

    def add_photo(self, label):
        for current_index, current_photo in enumerate(self.photos):
            if len(current_photo) < self.MAX_PAGE_COUNT:
                current_photo.append(label)
                return f"{label} photo added successfully on page {current_index + 1} slot {len(current_photo)}"
        else:
            return "No more free slots"

    def display(self):
        result = []
        for current_index, current_photo in enumerate(self.photos):
            if current_index == 0:
                result.append("-----------")

            txt = "[] " * len(current_photo)
            result.append(txt.rstrip())
            result.append("-----------")

        return "\n".join(result)


album = PhotoAlbum(2)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
print(album.display())