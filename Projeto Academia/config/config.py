import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
class Config:
    # Definir a URI de conexão com o banco PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
