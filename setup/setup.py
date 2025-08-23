from rich import print
from rich.table import Table
from time import sleep
import os
from setup.logo import logo_Setup

text = ""

def cls():
    return os.system("cls")


# Setup do Sistema

print("Olá Usuário!")

for i in range(3):
    print(".")
    sleep(1)

sleep(2)

cls()

logo_Setup()

sleep(3)

for i in range(5):
    text = ""
    sleep(1)
    text = "Iniciando "
    print(text)
    sleep(1)
    cls()
    text = "Iniciando ."
    print(text)
    sleep(1)
    cls()
    text = "Iniciando .."
    print(text)
    sleep(1)
    cls()
    text = "Iniciando ..."
    print(text)
    sleep(1)


cls()

print("INICIADO!")