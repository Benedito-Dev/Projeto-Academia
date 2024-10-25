from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

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
    instrutor_id = Column(Integer, ForeignKey('Instrutores.id'))  # Chave estrangeira para o instrutor

    # Relacionamento com a tabela Instrutores
    instrutor = relationship("Instrutores", back_populates="clientes")

    def __repr__(self):
        return f'<Cliente {self.nome}>'

# Instrutores
class Instrutores(Base):
    __tablename__ = 'instrutores'
    
    # Campos da tabela 'Instrutores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    telefone = Column(String)
    endereco = Column(String)
    cpf = Column(String)
    data_de_nascimento = Column(Date)

    def __repr__(self):
        return f'<Cliente {self.nome}>'
