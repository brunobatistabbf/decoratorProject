from decorator.ServicoDecorator import ServicoDecorator


class Pacote3(ServicoDecorator):
    def descricao(self) -> str:
        return self.assinatura.descricao() + ("\nPacote 3: Caixa Surpresa de Produtos")

    def preco(self) -> float:
        return self.assinatura.preco() + 29.99

