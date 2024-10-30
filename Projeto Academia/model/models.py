from sqlalchemy import Column, Integer, Numeric, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Instrutores(Base):
    __tablename__ = 'instrutores'  # Alterado para minúsculas
    
    # Campos da tabela 'instrutores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    telefone = Column(String)
    endereco = Column(String)
    cpf = Column(String)
    data_de_nascimento = Column(Date)

    def __repr__(self):
        return f'<Instrutor {self.nome}>'

class Cliente(Base):
    __tablename__ = 'clientes'
    
    # Campos da tabela 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    telefone = Column(String)
    endereco = Column(String)
    cpf = Column(String)
    data_de_nascimento = Column(Date)
    peso = Column(Numeric(precision=5,scale=2))
    altura = Column(Numeric(precision=3,scale=2))
    braco_direito = Column(Numeric(Float))
    braco_esquerdo = Column(Numeric(Float))
    peitoral = Column(Numeric(Float))
    cintura = Column(Numeric(Float))
    quadril = Column(Numeric(Float)) 
    coxa_direita = Column(Numeric(Float))
    coxa_esquerda = Column(Numeric(Float))
    panturrilha_direita = Column(Float)
    panturrilha_esquerda = Column(Float)


    

    
    # Chave estrangeira que referencia a tabela instrutores
    instrutor_id = Column(Integer, ForeignKey('instrutores.id'))
    
    # Relacionamento entre cliente e instrutor
    instrutor = relationship('Instrutores', backref='clientes')

    def __repr__(self):
        return f'<Cliente {self.nome}>'
