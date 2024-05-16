# Reconhecimento Facial com Python e Raspberry Pi

Este projeto implementa um sistema de reconhecimento facial utilizando Python e um Raspberry Pi. A biblioteca principal utilizada é a **Face Recognition**, que utiliza conceitos de deep learning e tem uma precisão aproximada de 98%. Com ela, é possível comparar duas fotos e determinar se a pessoa nas imagens é a mesma.

## Funcionamento

### 1. Cadastro de Novos Rostos

- Quando o pino GPIO do Raspberry é acionado, inicia-se o cadastro de um novo rosto.
- A câmera acoplada tira uma foto e o dispositivo verifica se há um rosto na imagem.
- Se não houver, a foto não é salva e uma mensagem informa que não foi possível identificar um rosto.
- Se for detectado um rosto, a foto é salva em formato TXT com um nome composto por "cadastro + data + hora".

### 2. Acesso por Reconhecimento Facial

- Quando solicitado na IHM (Interface Homem-Máquina), o ESP32 recebe a solicitação.
- Através de um pino GPIO do Raspberry, o código entra em processo de verificação.
- A câmera é ativada e tira uma foto.
- O código transforma a foto em um "Encoding" (código em formato hexadecimal).
- Esse código é comparado com os das fotos das faces cadastradas anteriormente.
- O Raspberry transforma todas as fotos em vetores (matrizes) para a comparação.
- Ao final da comparação, é acrescentado o valor numérico "1" ao código.
- Se o resultado da comparação for verdadeiro, o Raspberry libera o acesso para a pessoa identificada.
- Caso contrário, o acesso é negado.

### 3. Comunicação e Monitoramento

- A comunicação entre os dispositivos ocorre por protocolo SSH, permitindo autenticação e criptografia.
- O baixo nível de transferência e a ausência de interface gráfica facilitam o monitoramento via celular.
- Conectando o Raspberry e o celular na mesma rede Wi-Fi, é possível monitorar o acesso via reconhecimento facial.

## Requisitos

- Python
- Raspberry Pi
- Biblioteca Face Recognition
- Câmera acoplada
- ESP32 (para controle do acesso)
- Rede Wi-Fi

## Como Usar

1. Clone este repositório.
2. Instale as dependências (incluindo a biblioteca Face Recognition).
3. Execute o código no Raspberry Pi.
4. Acesse a IHM para cadastrar novos rostos ou permitir o acesso.
