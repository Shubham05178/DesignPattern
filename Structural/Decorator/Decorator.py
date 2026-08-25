from abc import ABC,abstractmethod
class Beverage(ABC):
    @abstractmethod
    def get_desc(self):
        pass
    @abstractmethod
    def getcost(self):
        pass
class Coffee(Beverage):
    def get_desc(self):
        return "A Plain Coffee"
    def getcost(self):
        return 40
class Decorator(Beverage):
    def __init__(self,coffee):
        self._coffee=coffee
    def get_desc(self):
        pass
    def getcost(self):
        pass
class Sugar(Decorator):
    def get_desc(self):
        return self._coffee.get_desc()+"+ Sugar"
    def getcost(self):
        return self._coffee.getcost()+5
class Milk(Decorator):
    def get_desc(self):
        return self._coffee.get_desc()+"+ Milk"
    def getcost(self):
        return self._coffee.getcost()+10
    
c=Coffee()
print(c.get_desc(),":",c.getcost())
c=Sugar(c)
print(c.get_desc(),":",c.getcost())
c=Milk(c)
print(c.get_desc(),":",c.getcost())