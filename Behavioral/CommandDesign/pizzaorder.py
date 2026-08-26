from order import   Order
from chef import Chef
class PizzaOrder(Order):
    def __init__(self,chef:Chef):
        self.__chef=chef
    def process(self):
        self.__chef.prepare_pizza()
