from abc import ABC, abstractmethod
class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass
class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass
class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass 
class PannerTikka(Starter):
    def prepare(self):
        print("Starter: Panner TikkAa is preparing")
class ButterChicken(MainCourse):
    def prepare(self):
        print("Main Course: Chikken Tikka is preparing")
class GulabJamun(Dessert):
    def prepare(self):
        print("Dessert: Gulab Jamun is preparing")
class SpringRoll(Starter):
    def prepare(self):
        print("Starter: Spring Roll is preparing")
class HakkaNoddles(MainCourse):
    def prepare(self):
        print("Main Course: Hakka Noodle is preparing")
class Tangyuan(Dessert):
    def prepare(self):
        print("Dessert: Tangyuan is preparing")
class CuisnesFactory(ABC):
    @abstractmethod
    def getStarter(self):
        pass
    @abstractmethod
    def getmainCourse(self):
        pass
    @abstractmethod
    def getdessert(self):
        pass
class NorthIndiaCusine(CuisnesFactory):
    def getdessert(self):
        return GulabJamun()

    def getStarter(self):
        return PannerTikka()
    def getmainCourse(self):
        return ButterChicken()  
class ChineseCusine(CuisnesFactory):
    def getStarter(self):
        return SpringRoll()
    def getmainCourse(self):
        return HakkaNoddles()
    def getdessert(self):
        return Tangyuan()
class CuisneMake:
    @staticmethod
    def make_cuisne(type):
        n=None
        if type=="northindian":
            n=NorthIndiaCusine()
        elif type=="chinese":
            n=ChineseCusine()
        else:
            print(f"this {type} is not available")
            return None
        n.getStarter().prepare()
        n.getmainCourse().prepare()
        n.getdessert().prepare()
class Restaurant:
    def order(self,type):
        CuisneMake.make_cuisne(type)


r=Restaurant()
r.order("northindian")
r.order("chinese")
r.order("southindian")