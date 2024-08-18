from decorator.ServicoDecorator import ServicoDecorator


class Pacote4(ServicoDecorator):
    def descricao(self) -> str:
        return self.assinatura.descricao() + ("\nPacote 4: Cartão de Crédito Premium")

    def preco(self) -> float:
        return self.assinatura.preco() + 49.99

