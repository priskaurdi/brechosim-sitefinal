# Importa as bibliotecas necessárias
import smtplib
from email.mime.text import MIMEText

# Dados do formulário
nome = input("Nome: ")
email = input("E-mail: ")
telefone = input("Telefone: ")
data = input("Data: ")
hora = input("Hora: ")

# Mensagem de e-mail
mensagem = f"""
Nome: {nome}
E-mail: {email}
Telefone: {telefone}
Data: {data}
Hora: {hora}
"""

# Configurações do servidor de e-mail
smtp_server = "smtp.gmail.com"
porta = 587
login = "SEU_EMAIL_GMAIL@gmail.com"  # Substitua por seu e-mail
senha = "SUA_SENHA_GMAIL"  # Substitua por sua senha
ssl_context = ssl.create_default_context()

# Cria o objeto de mensagem
msg = MIMEText(mensagem)
msg['Subject'] = "Agendamento BrechóSim"  # Assunto do e-mail
msg['From'] = login  # Remetente do e-mail
msg['To'] = "contato@brechossim.com.br"  # Destinatário do e-mail

# Conecta-se ao servidor de e-mail
with smtplib.SMTP(smtp_server, porta, context=ssl_context) as server:
    server.starttls()
    server.login(login, senha)
    server.sendmail(msg['From'], msg['To'], msg.as_string())

# Mensagem de confirmação
print("Seu agendamento foi enviado com sucesso!")
