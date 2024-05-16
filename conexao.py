import RPi.GPIO as GPIO
import time
    
# Substitua esses números pelos pinos GPIO que você está usando


# Configuração dos pinos do Raspberry Pi

# Configuração dos pinos do Raspberry Pi
def setup():
    pinos_saida = [29, 31, 33, 35]
    
    GPIO.setmode(GPIO.BOARD)
    for pino in pinos_saida:
        GPIO.setup(pino, GPIO.OUT)
    

# Função para converter decimal para binário
def decimal_para_binario(decimal):
    return bin(decimal)[2:].zfill(4)  # Garante que o número tenha 4 dígitos binários

# Função para ativar as saídas com base no número binário
def ativar_saidas(numero_binario):
    pinos_saida = [29, 31, 33, 35]
    for i, bit in enumerate(numero_binario):
        GPIO.output(pinos_saida[i], int(bit))

# Função principal
def main(decimal):
    #setup()
    try:
        #decimal = int(input("Digite um número decimal (0-15): "))
        if 0 <= decimal <= 15:
            binario = decimal_para_binario(decimal)
            print("Número em binário:", binario)
            ativar_saidas(binario)
            time.sleep(2)
            ativar_saidas(decimal_para_binario(0))
    except ValueError:
        print("Por favor, digite um número válido.")

def test(decimal):
    try:
        main(decimal)
    except KeyboardInterrupt:
        GPIO.cleanup()
