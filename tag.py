#Programa: Controle de Acesso RFID com Raspberry Pi

#!/usr/bin/env python
import conexao
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

def ler():
    conexao.setup()
    leitorRfid = SimpleMFRC522()

    print("Aproxime o cartao da leitora...")

    id, text = leitorRfid.read()
    print("ID do cartao: ", id)
    if id == 195891355494:
        print("Acesso permitido")
        conexao.main(3)
        
    elif id == 962984414085:
        print("Bem vindo Gustavo!")
        conexao.main(2)

    elif id == 469611175908:
        print("Acesso permitido")
        conexao.main(3)

    elif id == 840363089663:
        print("Acesso permitido")
        conexao.main(3)
    else:
        print("Acesso negado!")
        conexao.main(5)