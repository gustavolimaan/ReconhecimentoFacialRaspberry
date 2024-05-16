import face_recognition
import cv2
import conexao
from datetime import datetime

def cad():

    conexao.setup()
    print("Cadastrando...\nOlhe para a camera!")

    diretorio = "/home/gustavo/face-recognition-examples/img/Cadastro/"
    agora = datetime.now()
    data_format = agora.strftime("%d.%m.%Y_%H:%M:%S")
    nome_arquivo = f"cadastro_{data_format}.jpg"
    caminho = diretorio + nome_arquivo

    cam = cv2.VideoCapture(0)

    if cam.isOpened():
        resultado, frame = cam.read()
        
        while resultado:
            resultado, frame = cam.read()
            cv2.imwrite(caminho, frame)
            break

    cam.release()

    teste1_image = face_recognition.load_image_file(caminho)

    teste1 = face_recognition.face_locations(teste1_image)

    if teste1!=[]:
        cod_rostos = face_recognition.face_encodings(teste1_image)[0]

        with open(diretorio + "acessos.txt", "a") as arquivo:
            arquivo.write("\n" + nome_arquivo)
            print("Cadastro realizado com sucesso!")
            conexao.main(4)
        
    else:
        print("Rosto não detectado!")
        conexao.main(6)