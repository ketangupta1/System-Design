# Cheking burger_type with if else is parametrized

from abc import ABC, abstractmethod

class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass


class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")

class StandardBurger(Burger):
    def prepare(self):
        print("Preparing Standard Burger with bun, patty, cheese, and lettuce!")

class PremiumBurger(Burger):
    def prepare(self):
        print("Preparing Premium Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")


class BasicWheatBurger(Burger):
    def prepare(self):
        print("Preparing Basic Wheat Burger with bun, patty, and ketchup!")

class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Preparing Premium Wheat Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")

class StandardWheatBurger(Burger):
    def prepare(self):
        print("Preparing Standard Wheat Burger with bun, patty, cheese, and lettuce!")



class BurgerFactory(ABC):
    @abstractmethod
    def createBurger(self, burger_type: str) -> Burger:
        pass

class SinghBurger(BurgerFactory):
    def createBurger(self, burger_type: str):
        burger_type = burger_type.lower()
        if burger_type == "basic":
            return BasicBurger()
        elif burger_type == "standard":
            return StandardBurger()
        elif burger_type == "premium":
            return PremiumBurger()
        else:
            raise ValueError(f"Unknown burger type: {burger_type}")
        
class KingBurger(BurgerFactory):
    def createBurger(self, burger_type: str):
        burger_type = burger_type.lower()
        if burger_type == "basic":
            return BasicWheatBurger()
        elif burger_type == "standard":
            return StandardWheatBurger()
        elif burger_type == "premium":
            return PremiumWheatBurger()
        else:
            raise ValueError(f"Unknown burger type: {burger_type}")
        

if __name__ == "__main__":
    king_burger_factory = KingBurger()
    burger = king_burger_factory.createBurger("Standard")
    burger.prepare()

    singh_burger_factory = SinghBurger()
    burger = singh_burger_factory.createBurger("Premium")
    burger.prepare()