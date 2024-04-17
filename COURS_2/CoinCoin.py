from abc import ABC
from abc import abstractmethod

class Canard(ABC) :

    def __init__(self, name = 'undefined'):
        self.__name = name


    @property
    def name(self) :
        return self.__name

    @abstractmethod
    def voler(self) :
        pass

    @abstractmethod
    def nager(self) :
        pass


class Colvert(Canard) :

    def __init__(self, name) :
        super().__init__(name)
    
    def voler (self) :
        print(f"{self.name} vole comme un canard")

    def nager (self) :
        print("Je nage comme un canard de compet")


class CouRouge(Canard) :

    def __init__(self) :
        super().__init__()
    
    def voler (self) :
        print("Je vole comme un canard avec un cou rouge")

    def nager (self) :
        print("Je nage comme un canard de compet")


if __name__ == '__main__' :
    colvert = Colvert("coucou")
    colvert.voler()
    couRouge = CouRouge()

