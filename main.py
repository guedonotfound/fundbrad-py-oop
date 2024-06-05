class Main:
    pass

from cliente import Cliente
from conta import Conta

c1 = Cliente('Gabriel', '(12)3456-7890')
conta = Conta(c1.get_nome(), 6565)

conta.deposita(1000)
conta.saque(50)
conta.extrato()