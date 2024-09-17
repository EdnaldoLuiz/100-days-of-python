import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 100, "Relatório Automatizado")

    c.setFont("Helvetica", 18)
    c.drawString(100, height - 150, "Este é um exemplo de relatório gerado com ReportLab.")

    c.setFont("Helvetica", 12)
    text = ("ReportLab é uma biblioteca Python que permite a criação de documentos PDF de maneira programática. "
            "Com ReportLab, você pode adicionar texto, imagens, gráficos e muito mais aos seus documentos PDF.")
    c.drawString(100, height - 200, text)

    c.line(100, height - 220, 500, height - 220)

    img_path = os.path.join(assets_dir, 'gato.jpg')
    if os.path.exists(img_path):
        c.drawImage(img_path, 100, height - 400, width=200, height=150)
    else:
        print(f"Imagem não encontrada: {img_path}")

    c.save()

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
pdf_path = os.path.join(assets_dir, 'relatorio.pdf')

create_pdf(pdf_path)
print(f"PDF gerado em: {pdf_path}")