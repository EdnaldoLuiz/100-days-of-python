# Desafio 45

Enviando e-mails com a biblioteca `smtplib`

## Explicação

### Ferramentas Utilizadas

- `smtplib`: Biblioteca padrão do Python para envio de e-mails.
- `email.mime.text.MIMEText`: Classe para criar objetos de e-mail com texto.
- `email.mime.multipart.MIMEMultipart`: Classe para criar objetos de e-mail com múltiplas partes.

### Funções Principais

- `smtplib.SMTP()`: Cria um objeto de conexão SMTP.
- `starttls()`: Inicia a conexão TLS.
- `login()`: Faz login no servidor SMTP.
- `sendmail()`: Envia o e-mail.
- `quit()`: Encerra a conexão SMTP.

## Resultado

```py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

servidor_smtp = "smtp.gmail.com"
porta_smtp = 587
email = "teste@gmail.com"
senha = "senha"

remetente = email
destinatario = "contatoednaldoluiz@gmail.com"
assunto = "Teste de e-mail"
mensagem = "Olá, este é um teste de e-mail enviado com Python."

msg = MIMEMultipart()
msg['From'] = remetente
msg['To'] = destinatario
msg['Subject'] = assunto

msg.attach(MIMEText(mensagem, 'plain'))

try:
    servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
    servidor.starttls()
    servidor.login(email, senha)
    servidor.sendmail(remetente, destinatario, msg.as_string())
    servidor.quit()
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")