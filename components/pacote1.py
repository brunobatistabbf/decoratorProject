from decorator.ServicoDecorator import ServicoDecorator


class Pacote1(ServicoDecorator):
    def descricao(self) -> str:
        return self.assinatura.descricao() + ("\nPacote 1: Conectado a Vários Dispositivos")

    def preco(self) -> float:
        return self.assinatura.preco() + 19.99

