from abc import ABC, abstractmethod
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass   
class Pizza(Food):
    def prepare(self):
        return "Preparing Pizza"
class Burger(Food):
    def prepare(self):
        return "Preparing Burger"
class FoodFactory:
    @staticmethod
    def create_food(food_type):
        if food_type == "Pizza":
            return Pizza()
        elif food_type == "Burger":
            return Burger()
        else:
            return None
class Restaurant:
    
        
    def order_food(self, food_type):
        food = FoodFactory.create_food(food_type)
        if food:
            return food.prepare()
        else:
            return "Food type not available" 

restaurant = Restaurant()

print(restaurant.order_food("Pizza"))  # Output: Preparing Pizza    
print(restaurant.order_food("Burger"))  # Output: Preparing Burger  
print(restaurant.order_food("Pasta"))  # Output: Food type not available    

  