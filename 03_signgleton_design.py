import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    print("New instance of class has been created.")
        return cls._instance

if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()

    print(obj1 == obj2)