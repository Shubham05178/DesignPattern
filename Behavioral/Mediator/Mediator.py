from abc import  ABC, abstractmethod
from typing import List
class AirTraffic(ABC):
    @abstractmethod
    def register(self):
        pass
    def send_message(self):
        pass
class Airplane:
    def __init__(self,name):
        self.__flight_name=name
    def get_flight_name(self):
        return self.__flight_name
    def send_message(self,message,flight:Airplane):
        print(f"{self.__flight_name} is sending message to {flight.get_flight_name()} Message:{message}")
class TowerController(AirTraffic):
    def __init__(self):
        self.__flights:List[Airplane]=[]
    def register(self,flight:Airplane):
        self.__flights.append(flight)
    def send_message(self,airplane:Airplane,message):
        for flight in self.__flights:
            if flight!=airplane:
                airplane.send_message(message,flight)
        
sj=Airplane("SpiceJet-SJ4567")
sa=Airplane("Singapore Airlines-SA567")
ai=Airplane("AirIndia-AI6789")
t=TowerController()
t.register(sj)
t.register(sa)
t.register(ai)
t.send_message(sa,"Landing")