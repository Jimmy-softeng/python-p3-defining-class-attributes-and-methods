class Album:
    GENRES=["Hip-Hop", "Pop", "Jazz"]
    album_count=0

    def __init__(self,genre,date):
      if self.check_genre(genre): 
        self.increase_album_count()
        self.release_date=date
        self.genre=genre

    
    @classmethod
    def check_genre(cls,genre):
       return genre in cls.GENRES
    
    @classmethod
    def increase_album_count(cls,increment=1):
        cls.album_count+=increment

