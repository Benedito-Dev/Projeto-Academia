from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from model.models import Base, Cliente, Instrutores, Administradores
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
    def cadastrar_usuario(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento, codigo_adm, tabela):
        if tabela == 'usuario':
            novo_cliente = Cliente(
                nome=nome,
                email=email,
                senha=senha,
                telefone=telefone,
                endereco=endereco,
                cpf=cpf,
                data_de_nascimento=data_de_nascimento,
                instrutor_id = codigo_adm
            )
            self.session.add(novo_cliente)
            self.session.commit()
        if tabela == 'instrutor':
            novo_cliente = Instrutores(
                nome=nome,
                email=email,
                senha=senha,
                telefone=telefone,
                endereco=endereco,
                cpf=cpf,
                data_de_nascimento=data_de_nascimento,
                administrador_id = codigo_adm
            )
            self.session.add(novo_cliente)
            self.session.commit()
        if tabela == 'administrador':
            novo_cliente = Administradores(
                nome=nome,
                email=email,
                senha=senha,
                telefone=telefone,
                endereco=endereco,
                cpf=cpf,
                data_de_nascimento=data_de_nascimento,
            )
            self.session.add(novo_cliente)
            self.session.commit()

        return novo_cliente.id

    def validar_login(self, nome, senha):
        try:
            # Busca o cliente com o nome e senha fornecidos
            cliente = self.session.query(Cliente).filter_by(nome=nome, senha=senha).one_or_none()
            instrutor = self.session.query(Instrutores).filter_by(nome=nome, senha=senha).one_or_none()
            admin = self.session.query(Administradores).filter_by(nome=nome, senha=senha).one_or_none()
            if cliente:
                return 'cliente'
            elif instrutor:
                return 'instrutor'
            elif admin:
                return 'administrador'
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
    def obter_administradores(self):
        return self.session.query(Administradores).all()

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

    def enviando_medidas(self, id, musculo, medida):
        cliente = self.session.query(Cliente).filter_by(id=id).first()
        if cliente:
            try:
                # Use setattr para atualizar o atributo dinamicamente
                setattr(cliente, musculo, medida)
                self.session.commit()  # Salvar as alterações no banco de dados
                return True
            except Exception as e:
                self.session.rollback()  # Reverter em caso de erro
                print(f"Erro: {e}")
        else:
            print("Cliente não encontrado")
            

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
    