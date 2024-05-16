import conexao
import tag
import CadastroFace
import face_recognition
import RPi.GPIO as GPIO
import cv2
import time
from datetime import datetime

def setup():
    pinos_entrada = [37, 38, 40]
    GPIO.setmode(GPIO.BOARD)
    for pino in pinos_entrada:
        GPIO.setup(pino, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def acesso():
    conexao.setup()

    print("Tirando uma Foto")

    diretorio = "/home/gustavo/face-recognition-examples/img/Acesso/"
    diretorio2 = "/home/gustavo/face-recognition-examples/img/Cadastro/"
    agora = datetime.now()
    data_format = agora.strftime("%d.%m.%Y_%H:%M:%S")
    nome_arquivo = f"acesso_{data_format}.jpg"
    caminho = diretorio + nome_arquivo

    verifica=0

    cam = cv2.VideoCapture(0)

    if cam.isOpened():
        resultado, frame = cam.read()
        
        while resultado:
            resultado, frame = cam.read()
            cv2.imwrite(caminho, frame)
            break

    cam.release()

    print("Analisando seu rosto")

    teste1_image = face_recognition.load_image_file(caminho)

    teste1 = face_recognition.face_locations(teste1_image)
    

    if teste1!=[]:

        cod_rostos = face_recognition.face_encodings(teste1_image)[0]

        with open(diretorio2 + "acessos.txt", "r") as file:
            linhas = file.readlines()
        
        tamanho = len(linhas)

        
        for x in range(0, tamanho):
            
            unknown_image = face_recognition.load_image_file(diretorio2 + linhas[x].strip())

            encoding1 = face_recognition.face_encodings(unknown_image)[0]

        # Compare faces
        
            results1 = face_recognition.compare_faces(
                [encoding1], cod_rostos, )
            print(results1)
            if (results1[0]):
                verifica = 1
                y=x+1


            
        if (verifica):
            if (y==1):
                print('Bem vindo Gustavo!')
                conexao.main(1)

            print('Bem vindo!')
            conexao.main(3)
            
        else:
            print('Acesso negado!')
            conexao.main(5)
            
    else:
        print("Rosto não detectado!")
        conexao.main(6)

setup()
num = 0

try:
    while True:

        #teste = int(input(print("\n0-encerrar\t1-Acesso\t2-Cadastro")))

        if GPIO.input(37) == GPIO.HIGH:
            acesso()
            time.sleep(1)
            num = 0

        elif GPIO.input(38) == GPIO.HIGH:
            CadastroFace.cad()
            time.sleep(1)
            num = 0

        elif GPIO.input(40) == GPIO.HIGH:
            tag.ler()
            time.sleep(1)
            num = 0

        else:
            if num == 0:
                print("aguardo...")
                num = 1
except KeyboardInterrupt:
    # Se o usuário pressionar Ctrl + C, encerre o programa
    GPIO.cleanup()
    print("Programa encerrado pelo usuário.")
