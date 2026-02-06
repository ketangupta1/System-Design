from abc import ABC, abstractmethod


# ---------- Behavior Interfaces ----------

class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Talkable(ABC):
    @abstractmethod
    def talk(self):
        pass


# ---------- Walk Behaviors ----------

class NormalWalk(Walkable):
    def walk(self):
        print("Normal walking.")


class NoWalk(Walkable):
    def walk(self):
        print("No walking.")


# ---------- Fly Behaviors ----------

class NormalFly(Flyable):
    def fly(self):
        print("Normal flying.")


class NoFly(Flyable):
    def fly(self):
        print("No flying.")


# ---------- Talk Behaviors ----------

class NormalTalk(Talkable):
    def talk(self):
        print("Normal talking.")


class NoTalk(Talkable):
    def talk(self):
        print("No talking.")


# ---------- Robot Abstract Class ----------

class Robot(ABC):
    def __init__(
        self,
        talk_behavior: Talkable,
        fly_behavior: Flyable,
        walk_behavior: Walkable
    ):
        self.talk_behavior = talk_behavior
        self.fly_behavior = fly_behavior
        self.walk_behavior = walk_behavior

    def talk(self):
        self.talk_behavior.talk()

    def fly(self):
        self.fly_behavior.fly()

    def walk(self):
        self.walk_behavior.walk()

    @abstractmethod
    def projection(self):
        pass


# ---------- Concrete Robots ----------

class CompanionRobot(Robot):
    def projection(self):
        print("Companion robot projection.")


class GuardRobot(Robot):
    def projection(self):
        print("Guard robot projection.")


# ---------- Usage ----------

if __name__ == "__main__":
    robot1 = CompanionRobot(
        talk_behavior=NormalTalk(),
        fly_behavior=NoFly(),
        walk_behavior=NormalWalk()
    )

    robot1.talk()
    robot1.fly()
    robot1.walk()
    robot1.projection()

    print("---------------")

    robot2 = GuardRobot(
        talk_behavior=NoTalk(),
        fly_behavior=NormalFly(),
        walk_behavior=NoWalk()
    )

    robot2.talk()
    robot2.fly()
    robot2.walk()
    robot2.projection()
