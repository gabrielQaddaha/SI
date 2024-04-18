from abc import ABC, abstractmethod


class honkBehavior(ABC):

    @abstractmethod
    def honk(self):
        pass

class Honkable(honkBehavior):
    def honk(self) -> None:
        print("Honk Honk")

class NotHonkable(honkBehavior):
    def honk(self) -> None:
        print("I can't honk because i'm not a goose")


class Goose(ABC):

    def __init__(self, name="undefined", honkBehavior=None) -> None:
        self.__name = name
        self.__honkBehavior = honkBehavior

    @property
    def name(self):
        return self.__name

    @property
    def honkBehavior(self) -> honkBehavior:
        return self.__honkBehavior

    @honkBehavior.setter
    def honkBehavior(self, value):
        if isinstance(value, honkBehavior):
            self.__honkBehavior = value
        else:
            raise ValueError("The value is not an instance of honkBehavior")

    def honk(self):
        self.honkBehavior.honk()


class WhiteGoose(Goose):

    def __init__(self, name) -> None:
        super().__init__(name, Honkable())
