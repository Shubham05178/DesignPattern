from abc import ABC, abstractmethod


class TransportMode(ABC):
    @abstractmethod
    def eta(self):
        pass

    @abstractmethod
    def direction(self):
        pass


class Bicycle(TransportMode):
    def eta(self):
        print("Bicycle will take 30 mins")

    def direction(self):
        print("turn right then left then again right, then left")


class Bike(TransportMode):
    def eta(self):
        print("Bike will take 15 mins")

    def direction(self):
        print("go to flyover")


class Train(TransportMode):
    def eta(self):
        print("Train will take 5 mins")

    def direction(self):
        print("Sit in Train")


class TransportService:
    def __init__(self, transport_mode: TransportMode):
        self.__transport_mode = transport_mode

    def set_transport_mode(self, transport_mode: TransportMode):
        self.__transport_mode = transport_mode

    def get_eta(self):
        self.__transport_mode.eta()

    def get_direction(self):
        self.__transport_mode.direction()


t = TransportService(Bicycle())
t.get_eta()
t.get_direction()

t.set_transport_mode(Train())
t.get_eta()
t.get_direction()