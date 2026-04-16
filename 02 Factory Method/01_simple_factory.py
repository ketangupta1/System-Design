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


class BurgerFactory:
    def create_burger(self, burger_type: str) -> Burger:
        burger_type = burger_type.lower()

        if burger_type == "basic":
            return BasicBurger()
        elif burger_type == "standard":
            return StandardBurger()
        elif burger_type == "premium":
            return PremiumBurger()
        else:
            raise ValueError(f"Unknown burger type: {burger_type}")


if __name__ == "__main__":
    factory = BurgerFactory()

    factory.create_burger("Basic").prepare()
    factory.create_burger("Premium").prepare()
    factory.create_burger("Standard").prepare()
