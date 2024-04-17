from abc import ABC, abstractmethod


class FlyBehavior(ABC):

    @abstractmethod
    def voler(self):
        pass


class Flyable(FlyBehavior):
    def voler(self) -> None:
        print("I really can fly !!!")

class NotFlyable(FlyBehavior):
    def voler(self) -> None:
        print("I believe i can fly but not realy ...")

class BrokenWings(FlyBehavior):
    def voler(self) -> None:
        print("I can't fly, my wings are broken !!!!!!!")

# CANCANER
class QuackBehavior(ABC):
    @abstractmethod
    def cancaner(self):
        pass


class CanCan(QuackBehavior):
    def cancaner(self) -> None:
        print("\nCoin Coin")


class NotCanCan(QuackBehavior):
    def cancaner(self) -> None:
        print("\nI can't COIN COIN !!!!!!!!!!!!!!! ")


class Canard(ABC):

    def __init__(self, name="undefined", flyBehavior=None, quackBehavior=None):
        self.__name = name
        self.__flyBehavior = flyBehavior
        self.__quackBehavior = quackBehavior

    @property
    def name(self):
        return self.__name

    @property
    def flyBehavior(self) -> FlyBehavior:
        return self.__flyBehavior

    @flyBehavior.setter
    def flyBehavior(self, value):
        """
            Sets the fly behavior.

            Parameters:
            value (FlyBehavior): The new fly behavior to be set.

            Raises:
            ValueError: If the value is not an instance of FlyBehavior.

            """
        if isinstance(value, FlyBehavior):
            self.__flyBehavior = value
        else:
            raise ValueError("Unable to set a new value")

    @property
    def quackBehavior(self) -> QuackBehavior:
        return self.__quackBehavior
    
    
    def voler(self):
        self.flyBehavior.voler()

    def cancaner(self):
        self.quackBehavior.cancaner()


class Colvert(Canard):

    def __init__(self, name) -> None:
        super().__init__(name, Flyable(), CanCan())


class CouRouge(Canard):

    def __init__(self, name) -> None:
        super().__init__(name, NotFlyable(), NotCanCan())


if __name__ == "__main__":
    colvert = Colvert("coucou")
    colvert.voler()
    colvert.cancaner()
    couRouge = CouRouge("zoubi")
    couRouge.voler()
    couRouge.cancaner()
    couRouge.flyBehavior = BrokenWings()
    couRouge.voler()
