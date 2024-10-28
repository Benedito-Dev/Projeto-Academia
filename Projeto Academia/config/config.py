import os

class Config:
    # Definir a URI de conexão com o banco PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@26.224.231.118:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
