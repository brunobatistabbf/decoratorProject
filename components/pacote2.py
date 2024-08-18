from decorator.ServicoDecorator import ServicoDecorator


class Pacote2(ServicoDecorator):
    def descricao(self) -> str:
        return self.assinatura.descricao() + ("\nPacote 2: Frete Grátis em Produtos")

    def preco(self) -> float:
        return self.assinatura.preco() + 9.99

