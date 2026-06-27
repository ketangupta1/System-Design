from abc import ABC, abstractmethod

class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

class BasicBurger(Burger):
    def prepare(self):
        print(f"Basic burger is preparing!!")

class StandardBurger(Burger):
    def prepare(self):
        print(f"Standard burger is preparing!!")

class PremiumBurger(Burger):
    def prepare(self):
        print(f"Premium burger is preparing!!")

class BurgerFactory:
    def create_burger(self, type: str) -> Burger:
        if type.lower() == 'basic':
            return BasicBurger()
        elif type.lower() == 'standard':
            return StandardBurger()
        elif type.lower() == 'premium':
            return PremiumBurger()
        else:
            raise ValueError(f"Unknown burger type: {type}")
    
if __name__ == '__main__':
    factory = BurgerFactory()
    basic_burger_obj = factory.create_burger("Basic")
    basic_burger_obj.prepare()

    Standard_burger_obj = factory.create_burger("Standard")
    Standard_burger_obj.prepare()

    premium_burger_obj  = factory.create_burger("Premium")
    premium_burger_obj.prepare()

