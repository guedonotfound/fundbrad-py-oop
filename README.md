# Bank Account Project

This is a Python project developed as part of a course on Object-Oriented Programming (OOP). The aim of this project is to create a simple simulation of a banking system, with classes representing clients, bank accounts, and basic operations such as deposit, withdrawal, and statement display.

## Project Structure

The project consists of three main files:

- `main.py`: This file contains the main code of the program. It instantiates objects of client and bank account, performs operations such as deposit, withdrawal, and statement display.
- `conta.py`: Contains the definition of the `Conta` class, which represents a bank account. It has methods to perform operations such as withdrawal, deposit, and statement display.
- `cliente.py`: This file defines the `Cliente` class, which represents a bank client. It contains methods to get and set the client's name.

## How to Use

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Run the `main.py` file in your Python terminal.

## Example Usage

```python
# Import the necessary classes
from cliente import Cliente
from conta import Conta

# Create a Client object
c1 = Cliente('Gabriel', '(12)3456-7890')

# Create a bank account for the client
conta = Conta(c1.get_nome(), 6565)

# Perform deposit and withdrawal operations
conta.deposita(1000)
conta.saque(50)

# Display the account statement
conta.extrato()
