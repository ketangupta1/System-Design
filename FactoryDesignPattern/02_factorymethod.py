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

class BasicWheatBurger(Burger):
    def prepare(self):
        print(f"Basic wheat burger is preparing!!")

class StandardWheatBurger(Burger):
    def prepare(self):
        print(f"Standard wheat burger is preparing!!")

class PremiumWheatBurger(Burger):
    def prepare(self):
        print(f"Premium wheat burger is preparing!!")


class BurgerFactory(ABC):
    @abstractmethod
    def create_burger(self, type: str) -> Burger:
        pass

class SinghBurgerBurgerFactory(BurgerFactory):
    def create_burger(self, type: str) -> Burger:
        if type.lower() == 'basic':
            return BasicBurger()
        elif type.lower() == 'standard':
            return StandardBurger()
        elif type.lower() == 'premium':
            return PremiumBurger()
        else:
            raise ValueError(f"Unknown Singh burger type: {type}")
        
class KingBurgerBurgerFactory(BurgerFactory):
    def create_burger(self, type: str) -> Burger:
        if type.lower() == 'basic':
            return BasicWheatBurger()
        elif type.lower() == 'standard':
            return StandardWheatBurger()
        elif type.lower() == 'premium':
            return PremiumWheatBurger()
        else:
            raise ValueError(f"Unknown King burger type: {type}")
        

if __name__ == '__main__':
    BurgerFactory = KingBurgerBurgerFactory()      # Create the BurgerFactory object
    king_BurgerFactory = BurgerFactory.create_burger("basic")      # Ask BurgerFactory to create a burger
    king_BurgerFactory.prepare()

    king_BurgerFactory = BurgerFactory.create_burger("Premium")
    king_BurgerFactory.prepare()


    BurgerFactory = SinghBurgerBurgerFactory()
    singh_BurgerFactory = BurgerFactory.create_burger("basic")
    singh_BurgerFactory.prepare()