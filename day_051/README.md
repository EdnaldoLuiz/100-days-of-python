# Desafio 51

Gerando códigos QR com a biblioteca `qrcode`

## Explicação

### Ferramentas Utilizadas

- `qrcode`: Biblioteca para gerar códigos QR.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `qrcode.QRCode()`: Cria um objeto QRCode.
- `qr.add_data()`: Adiciona dados ao código QR.
- `qr.make()`: Gera o código QR.
- `qr.make_image()`: Cria uma imagem do código QR.
- `os.makedirs()`: Cria diretórios recursivamente.

## Resultado

```py
import qrcode
import os

def criar_diretorio(diretorio):
    """
    Cria o diretório se ele não existir.
    """
    os.makedirs(diretorio, exist_ok=True)

def gerar_qr_code(url, caminho_arquivo, fill_color='black', back_color='white'):
    """
    Gera um código QR a partir de uma URL e salva em um arquivo.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(caminho_arquivo)

if __name__ == "__main__":
    diretorio = 'assets'
    criar_diretorio(diretorio)
    caminho_arquivo = os.path.join(diretorio, 'qrcode.png')
    url = 'https://www.example.com'
    gerar_qr_code(url, caminho_arquivo)
    print(f"QR Code gerado e salvo em {caminho_arquivo}")