class Laptop:
    processor=None
    ram=None
    color=None
    screen_size=None
    graphics_card=None
    def get_specs(self):
        if self.ram:
            print(f"Ram: {self.ram}")
        if self.processor:
            print(f"Processor: {self.processor}")
        if self.graphics_card:
            print(f"Graphics Card: {self.graphics_card}")
        if self.color:
            print(f"Color: {self.color}")
        if self.screen_size:
            print(f"Screen Size: {self.screen_size}")
class LaptopBuilder:
    def __init__(self):
        self.__laptop=Laptop()
    def setColor(self,color):
        self.__laptop.color=color
        return self
    def setScreenSize(self,screen_size):
        self.__laptop.screen_size=screen_size
        return self
    def setProcessor(self,processor):
        self.__laptop.processor=processor
        return self
    def setRam(self,ram):
        self.__laptop.ram=ram
        return self
    def setGraphicsCard(self,graphics_card):
            self.__laptop.graphics_card=graphics_card
            return self
    def build(self):
        return self.__laptop

l=LaptopBuilder().setRam("16 GB").setProcessor("i5 Turbo").setScreenSize("22 inches").setGraphicsCard("16 GB").build()
l.get_specs()