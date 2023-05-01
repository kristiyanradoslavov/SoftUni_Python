class PhotoAlbum:
    MAX_PAGE_COUNT = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count)


photo = PhotoAlbum.from_photos_count(4)

print(photo.photos)
