from interface.assinatura import Assinatura

class AssinaturaBase(Assinatura):
    def descricao(self) -> str:
        return  "Assinatura Base - Plano Básico"

    def preco(self) -> float:
        return 9.99