from abc import ABC, abstractmethod


# =======================
# Product Interface
# =======================
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass


# =======================
# Concrete Products
# =======================
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


class StandardWheatBurger(Burger):
    def prepare(self):
        print("Preparing Standard Wheat Burger with bun, patty, cheese, and lettuce!")


class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Preparing Premium Wheat Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")


# =======================
# Creator (Factory Interface)
# =======================
class BurgerFactory(ABC):
    @abstractmethod
    def createBurger(self) -> Burger:
        pass


# =======================
# Concrete Factories (Factory Method)
# =======================
class SinghBasicBurgerFactory(BurgerFactory):
    def createBurger(self):
        return BasicBurger()


class SinghStandardBurgerFactory(BurgerFactory):
    def createBurger(self):
        return StandardBurger()


class SinghPremiumBurgerFactory(BurgerFactory):
    def createBurger(self):
        return PremiumBurger()


class KingBasicBurgerFactory(BurgerFactory):
    def createBurger(self):
        return BasicWheatBurger()


class KingStandardBurgerFactory(BurgerFactory):
    def createBurger(self):
        return StandardWheatBurger()


class KingPremiumBurgerFactory(BurgerFactory):
    def createBurger(self):
        return PremiumWheatBurger()


# =======================
# Client Code
# =======================
if __name__ == "__main__":
    factory = KingPremiumBurgerFactory()
    burger = factory.createBurger()
    burger.prepare()

    factory = SinghStandardBurgerFactory()
    burger = factory.createBurger()
    burger.prepare()
