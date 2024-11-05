from abc import ABC, abstractmethod

# Componente abstrato
class elements(ABC):
    @abstractmethod
    def calulate_price(self):
        pass

    @abstractmethod
    def showContent(self):
        pass


