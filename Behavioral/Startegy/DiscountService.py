class DiscountService:
    def __init__(self,discountstrategy):
        self.__discountstrategy=discountstrategy
    def cal_dis(self,price):
        return price-(price*self.__discountstrategy.discount()/100)
