from base.assinatura_base import AssinaturaBase


class ServicoDecorator(AssinaturaBase):
    def __init__(self, assinatura: AssinaturaBase):
        self.assinatura = assinatura

    def descricao(self) -> str:
        return self.assinatura.descricao()

    def preco(self) -> float:
        return self.assinatura.preco()
