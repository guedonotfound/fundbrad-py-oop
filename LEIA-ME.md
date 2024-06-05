# Projeto de Conta Bancária

Este é um projeto Python desenvolvido como parte de um curso sobre Programação Orientada a Objetos (POO). O objetivo deste projeto é criar uma simulação de um sistema bancário simples, com classes representando clientes, contas bancárias e operações básicas como depósito, saque e exibição de extrato.

## Estrutura do Projeto

O projeto é composto por três arquivos principais:

- `main.py`: Este arquivo contém o código principal do programa. Ele instancia objetos de cliente e conta bancária, realiza operações de depósito, saque e exibição de extrato.
- `conta.py`: Contém a definição da classe `Conta`, que representa uma conta bancária. Ele possui métodos para realizar operações como saque, depósito e exibição de extrato.
- `cliente.py`: Este arquivo define a classe `Cliente`, que representa um cliente do banco. Ele contém métodos para obter e definir o nome do cliente.

## Como Usar

1. Clone o repositório para sua máquina local.
2. Certifique-se de ter Python instalado.
3. Execute o arquivo `main.py` em seu terminal Python.

## Exemplo de Uso

```python
# Importe as classes necessárias
from cliente import Cliente
from conta import Conta

# Crie um objeto Cliente
c1 = Cliente('Gabriel', '(12)3456-7890')

# Crie uma conta bancária para o cliente
conta = Conta(c1.get_nome(), 6565)

# Realize operações de depósito e saque
conta.deposita(1000)
conta.saque(50)

# Exiba o extrato da conta
conta.extrato()
