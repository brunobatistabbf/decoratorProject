from decorator.ServicoDecorator import ServicoDecorator

class Pacote5(ServicoDecorator):
    def descricao(self) -> str:
        return  self.assinatura.descricao() + ("\nPacote 5: CashBack")

    def preco(self) -> float:
        return  self.assinatura.preco() + 19.99

