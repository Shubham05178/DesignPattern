from chef import Chef
from burgerorder import  BurgerOrder
from pizzaorder import  PizzaOrder
from waiter import Waiter
c=Chef()
w=Waiter()
w.take_order(PizzaOrder(c))
w.take_order(BurgerOrder(c))