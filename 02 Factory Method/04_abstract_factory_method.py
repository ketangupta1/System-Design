from abc import ABC, abstractmethod


# Product Interfaces
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass


class GarlicBread(ABC):
    @abstractmethod
    def prepare(self):
        pass


# Concrete Burger Products
class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")


class PremiumBurger(Burger):
    def prepare(self):
        print("Preparing Premium Burger with gourmet bun, premium patty, and secret sauce!")


class BasicWheatBurger(Burger):
    def prepare(self):
        print("Preparing Basic Wheat Burger with bun, patty, and ketchup!")


class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Preparing Premium Wheat Burger with gourmet bun, premium patty, and secret sauce!")



# Concrete Garlic Bread Products
class NormalGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Normal Garlic Bread with butter and garlic!")


class WheatGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Wheat Garlic Bread with butter and garlic!")


# Abstract Factory
class FoodFactory(ABC):
    @abstractmethod
    def createBurger(self) -> Burger:
        pass

    @abstractmethod
    def createGarlicBread(self) -> GarlicBread:
        pass


# Concrete Factories
class SinghFoodFactory(FoodFactory):
    def createBurger(self):
        return PremiumBurger()

    def createGarlicBread(self):
        return NormalGarlicBread()


class KingFoodFactory(FoodFactory):
    def createBurger(self):
        return PremiumWheatBurger()

    def createGarlicBread(self):
        return WheatGarlicBread()


# Client Code
if __name__ == "__main__":
    factory: FoodFactory = KingFoodFactory()

    burger = factory.createBurger()
    garlic_bread = factory.createGarlicBread()

    burger.prepare()
    garlic_bread.prepare()


    factory = SinghFoodFactory()
    burger = factory.createBurger()
    garlic_bread = factory.createGarlicBread()

    burger.prepare()
    garlic_bread.prepare()
