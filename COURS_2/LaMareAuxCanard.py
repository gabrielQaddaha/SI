from KOINKOIN import Canard, Colvert
from GoosyGoosa import Goose, WhiteGoose

class DuckSimulator:

    def __init__(self, canard: Canard , goose: Goose) -> None:
        self.__canard = canard
        self.__goose = goose

    def simulate(self) -> None:
        for _ in range (2):
            self.__canard.voler()

        self.__canard.cancaner()

        for _ in range (3):
            self.__canard.voler()

        for _ in range (2):
            self.__goose.honk()

        

if __name__ == '__main__':
    MyLittleSwaggyGoose = WhiteGoose("yo soy una goose de qualidad ")
    CocoLeColvert = Colvert("Colvert")
    simulator = DuckSimulator(CocoLeColvert,  MyLittleSwaggyGoose)
    simulator.simulate()
    
    
    