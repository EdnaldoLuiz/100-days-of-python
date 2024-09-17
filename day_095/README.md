# Desafio 95

Criando relatórios automatizados em PDF com ReportLab

## Explicação

### Ferramentas Utilizadas

- `reportlab`: Biblioteca para criação de documentos PDF.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `canvas.Canvas()`: Cria um objeto canvas para desenhar no PDF.
- `c.setFont()`: Define a fonte do texto.
- `c.drawString()`: Desenha uma string no PDF.
- `c.save()`: Salva o documento PDF.

## Resultado

```python
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)
pdf_path = os.path.join(assets_dir, 'relatorio.pdf')

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 100, "Relatório Automatizado")

    c.setFont("Helvetica", 18)
    c.drawString(100, height - 150, "Este é um exemplo de relatório gerado com ReportLab.")

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 200, "Você pode adicionar mais conteúdo aqui conforme necessário.")

    c.save()

if __name__ == "__main__":
    create_pdf(pdf_path)
    print(f"Relatório salvo em: {pdf_path}")
```