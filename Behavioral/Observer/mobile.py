from Observer import Observer
class Mobile(Observer):
    def update(self,temp):
        self.__temp=temp
        print(f"Mobile Temp={self.__temp}C")
        