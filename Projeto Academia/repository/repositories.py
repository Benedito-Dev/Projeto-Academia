from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from model.models import Base, Cliente, Instrutores
from config.config import Config

class ClienteRepository():
    def __init__(self):
        # Conectar ao banco de dados PostgreSQL
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    # Função para inicializar o banco de dados
    def init_db(self):
        Base.metadata.create_all(self.engine)

    # Função para cadastrar um novo cliente
    def cadastrar_cliente(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        novo_cliente = Cliente(
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            endereco=endereco,
            cpf=cpf,
            data_de_nascimento=data_de_nascimento
        )
        self.session.add(novo_cliente)
        self.session.commit()
        return True

    def validar_login(self, nome, senha):
        try:
            # Busca o cliente com o nome e senha fornecidos
            cliente = self.session.query(Cliente).filter_by(nome=nome, senha=senha).one_or_none()
            instrutor = self.session.query(Instrutores).filter_by(nome=nome, senha=senha).one_or_none()
            if cliente:
                return 'cliente'
            elif instrutor:
                return 'instrutor'
            else:
                return False
        except NoResultFound:
            return False 

    # Função para obter todos os clientes
    def obter_usuarios(self):
        return self.session.query(Cliente).all()
    
    # Buscar instrutores
    def obter_instrutores(self):
        return self.session.query(Instrutores).all()

    def obter_usuario(self, nome):
        try:
             return self.session.query(Cliente).filter_by(nome=nome).first()
        except SQLAlchemyError as e:
            print(f"Erro ao buscar usuário: {e}")

    def registros_musculatura(self, nome):
        # Fazendo a consulta para obter as colunas de musculatura do primeiro cliente como exemplo
        cliente = self.session.query(Cliente).filter_by(nome=nome).first()
        
        # Obter apenas as colunas de musculatura
        if cliente:
            lista_musculos = [
                Cliente.braco_direito,
                Cliente.braco_esquerdo,
                Cliente.peitoral,
                Cliente.cintura,
                Cliente.quadril,
                Cliente.coxa_direita,
                Cliente.coxa_esquerda,
                Cliente.panturrilha_direita,
                Cliente.panturrilha_esquerda
            ]
            return lista_musculos
        else:
            return []
    
       

    # Função para atualizar um cliente
    def atualizar_cliente(self, cliente_id, nome, email, senha, telefone, endereco, data_de_nascimento):
        cliente = self.session.query(Cliente).get(cliente_id)
        if cliente:
            cliente.nome = nome
            cliente.email = email
            cliente.senha = senha
            cliente.telefone = telefone
            cliente.endereco = endereco
            if not data_de_nascimento:
                raise ValueError("Data de nascimento não pode estar vazia")
            cliente.data_de_nascimento = data_de_nascimento

    def atualizar_medidas_repository(self, cliente_id, braco_direito, braco_esquerda, peitoral, quadril, cintura, coxa_direita, coxa_esquerda, panturrilha_direita, panturrilha_esquerda):
        cliente = self.session.query(Cliente).filter_by(cliente_id).first()
        if cliente:
            cliente.braco_direito = braco_direito
            cliente.braco_esquerdo = braco_esquerda
            cliente.peitoral = peitoral
            cliente.quadril = quadril
            cliente.cintura = cintura
            cliente.coxa_direita = coxa_direita
            cliente.coxa_esquerda = coxa_esquerda
            cliente.panturrilha_direita = panturrilha_direita
            cliente.panturrilha_esquerda = panturrilha_esquerda
    # Função para deletar um cliente
    def deletar_cliente(self, cliente_id):
        cliente = self.session.query(Cliente).get(cliente_id)
        if cliente:
            self.session.delete(cliente)
            self.session.commit()

    def consultar_cpf(self, cpf):
        cliente = self.session.query(Cliente).filter_by(cpf=cpf).first()
        return cliente  # Retorna o cliente ou None
    
    def consultar_email(self,email):
        cliente = self.session.query(Cliente).filter_by(email=email).first()
        return cliente
    