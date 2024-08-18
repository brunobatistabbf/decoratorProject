from abc import ABC, abstractmethod

class Assinatura(ABC):
    @abstractmethod
    def descricao(self) -> str:
        pass

    @abstractmethod
    def preco(self) -> float:
        pass