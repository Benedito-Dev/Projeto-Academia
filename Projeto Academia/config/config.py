import os

class Config:
    # Definir a URI de conexão com o banco PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/features')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
