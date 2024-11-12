from sqlalchemy import Column, Integer, Numeric, String, Float, Date, ForeignKey
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
    peso = Column(Numeric(precision=5,scale=2))
    altura = Column(Numeric(precision=3,scale=2))
    braco_direito = Column(Numeric(precision=4, scale=1))  # Ex.: 40.5 cm
    braco_esquerdo = Column(Numeric(precision=4, scale=1))
    peitoral = Column(Numeric(precision=5, scale=1))  # Ex.: 120.0 cm
    cintura = Column(Numeric(precision=4, scale=1))  # Ex.: 90.0 cm
    quadril = Column(Numeric(precision=4, scale=1))  # Ex.: 100.5 cm
    coxa_direita = Column(Numeric(precision=4, scale=1))  # Ex.: 60.0 cm
    coxa_esquerda = Column(Numeric(precision=4, scale=1))
    panturrilha_direita = Column(Numeric(precision=4, scale=1))  # Ex.: 40.0 cm
    panturrilha_esquerda = Column(Numeric(precision=4, scale=1))

    # Chave estrangeira que referencia a tabela instrutores
    instrutor_id = Column(Integer, ForeignKey('instrutores.id'))
    
    # Relacionamento entre cliente e instrutor
    instrutor = relationship('Instrutores', backref='clientes')

    def __repr__(self):
        return f'<Cliente {self.nome}>'