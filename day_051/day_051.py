import qrcode
import qrcode.constants
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
    return img

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_path, 'assets')
    criar_diretorio(assets_dir)
    qr_code_path = os.path.join(assets_dir, 'qr_code.png')

    url = 'https://github.com/EdnaldoLuiz'
    img = gerar_qr_code(url, qr_code_path)

    img.show()

if __name__ == '__main__':
    main()