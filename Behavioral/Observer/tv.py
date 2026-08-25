from Observer import Observer
class TV(Observer):
    def update(self,temp):
        self.__temp=temp
        print(f"TV Temp={self.__temp}C")
