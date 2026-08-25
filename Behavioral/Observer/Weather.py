from Observer import Observer
from typing import List
class Weather:
    def __init__(self):
        self.__temp=0
        self.__subscribers: List[Observer]=[]
    def subscribe(self,observer:Observer):
        self.__subscribers.append(observer)
    def unsubscribe(self,obeserver:Observer):
        for i in range(len(self.__subscribers)):
            if self.__subscribers[i]==obeserver:
                self.__subscribers.pop(i)
                break
    def notifyallsub(self):
            for i in self.__subscribers:
                i.update(self.__temp)
    def update(self,temp):
        self.__temp=temp
        self.notifyallsub()
    

