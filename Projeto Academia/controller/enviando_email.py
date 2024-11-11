# email_sender.py
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.config import EMAIL_PASS, EMAIL_USER

class EnviandoEmail():
    def __init__(self):
        """Inicializa a classe e carrega as credenciais do usuário diretamente de variáveis de ambiente."""
        # Carrega as credenciais do Gmail
        self.usuario = EMAIL_USER
        self.senha = EMAIL_PASS

        # Verificar se as credenciais estão configuradas
        if not self.usuario or not self.senha:
            raise ValueError("Credenciais de e-mail não encontradas. Certifique-se de definir as variáveis de ambiente EMAIL_USER e EMAIL_PASSWORD.")

    def enviar_email(self, destinatario, nome):
        """Envia um e-mail com um título chamativo verde e uma mensagem de agradecimento."""

        # Definir título e mensagem
        assunto = "Obrigado por logar conosco novamente!"
        mensagem_html = f"""
        <html>
            <body>
                <h1 style="color: #7fd350;">Obrigado por Escolher nossa rede de Academias, {nome}!</h1>
                <p>Estamos felizes por tê-lo conosco. Se precisar de qualquer ajuda, nossa equipe está à disposição.</p>
            </body>
        </html>
        """

        # Configuração do e-mail
        msg = MIMEMultipart()
        msg['From'] = self.usuario
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem_html, 'html'))

        try:
            # Conecta ao servidor SMTP do Gmail usando SSL
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
                servidor.login(self.usuario, self.senha)
                servidor.sendmail(self.usuario, destinatario, msg.as_string())
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print("Erro ao enviar o e-mail:", e)
