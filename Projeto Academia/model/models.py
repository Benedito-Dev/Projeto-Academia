from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Administradores(Base):
    __tablename__ = 'administradores'  # Alterado para minúsculas
    
    # Campos da tabela 'administrador'
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

    # Chave estrangeira que referencia a tabela instrutores
    administrador_id = Column(Integer, ForeignKey('administradores.id'))
    
    # Relacionamento entre cliente e instrutor
    administrador = relationship('Administradores', backref='instrutores')

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
    
    # Chave estrangeira que referencia a tabela instrutores
    instrutor_id = Column(Integer, ForeignKey('instrutores.id'))
    
    # Relacionamento entre cliente e instrutor
    instrutor = relationship('Instrutores', backref='clientes')

    def __repr__(self):
        return f'<Cliente {self.nome}>'
class Evento:
    def __init__(self, data, descricao):
        self.data = data
        self.descricao = descricao
