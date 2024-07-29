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
msg.attach(MIMEText(mensagem, 'plain', 'utf-8'))

conexao = smtplib.SMTP(servidor_smtp, porta_smtp)
conexao.starttls()
conexao.login(email, senha)
conexao.sendmail(remetente, destinatario, msg.as_string())
conexao.quit()

print("E-mail enviado com sucesso.")