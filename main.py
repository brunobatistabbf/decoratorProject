from base.assinatura_base import AssinaturaBase
from components.pacote5 import Pacote5
from components.pacote1 import Pacote1
from components.pacote2 import Pacote2
from components.pacote3 import Pacote3
from components.pacote4 import Pacote4

#Assinatura basica
assinatura = AssinaturaBase()


#Adicionando servicos extras
assinatura = Pacote1(assinatura)
assinatura = Pacote3(assinatura)
assinatura = Pacote2(assinatura)

print(assinatura.descricao())
print(f"R$ {assinatura.preco()}")


