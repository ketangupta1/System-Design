from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b

class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b
    
class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b
    
class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy
    
    def execute_strategy(self, a: int, b: int):
        return self.strategy.execute(a, b)


if __name__ == "__main__":
    contextObj = Context(ConcreteStrategyAdd())
    add = contextObj.execute_strategy(3, 8)
    print(f"Addition is: {add}")

    # Update the Strategy acc to needs
    contextObj.set_strategy(ConcreteStrategyMultiply())
    mul = contextObj.execute_strategy(5, 7)
    print(f"Multiplication is: {mul}")
