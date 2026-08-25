from abc import ABC,abstractmethod
from typing import List
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass
class Song:
    def __init__(self,title):
        self.__title=title
    def get_title(self):
        return self.__title
class PlaylistIterator(Iterator):
    def __init__(self,songs_list):
        self.__songs=songs_list
        self.__position=0
    def has_next(self):
        return self.__position<len(self.__songs)
    def next(self):
        while self.has_next():
            song=self.__songs[self.__position]
            self.__position+=1
            return song
        return None
class PlayList:
    def __init__(self):
        self.__songs:List[Song]=[]
    def add_song(self,song):
        self.__songs.append(song)
    def create_iterator(self):
        return PlaylistIterator(self.__songs)
p=PlayList()
for i in range(10):
    p.add_song(Song("song"+str(i)))
pi=p.create_iterator()
while pi.has_next():
    print(pi.next().get_title())