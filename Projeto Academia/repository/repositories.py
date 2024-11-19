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
    
    def pre_cadastrar_administrador(self):
        try:
            # Verifica se já existe um administrador com nome 'admin' e senha 'admin'
            administrador_existe = self.session.query(
                self.session.query(Administradores).filter_by(nome='ADMIN', senha='admin').exists()
            ).scalar()

            if not administrador_existe:
                # Se não existir, cria o pré-cadastro do administrador
                novo_administrador = Administradores(
                    nome='ADMIN',
                    email='admin@exemplo.com',
                    senha='admin',
                    telefone='0000-0000',
                    endereco='Endereço padrão',
                    cpf='000.000.000-00',
                    data_de_nascimento=None
                )
                self.session.add(novo_administrador)
                self.session.commit()
                print("Administrador pré-cadastrado com sucesso!")
            else:
                print("Administrador já existe. Nenhum novo cadastro foi feito.")
        except Exception as e:
            print(f"Erro ao tentar pré-cadastrar administrador: {e}")


    # Função para cadastrar um novo cliente
    def cadastrar_cliente(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento, atual_data_ficha, renovacao_data_ficha, objetivo, codigo_adm, tabela):
        try:
            if tabela == 'usuario':
                try:
                    novo_cliente = Cliente(
                        nome=nome,
                        email=email,
                        senha=senha,
                        telefone=telefone,
                        endereco=endereco,
                        cpf=cpf,
                        objetivo=objetivo,
                        atual_data_ficha=atual_data_ficha,
                        renovacao_data_ficha=renovacao_data_ficha,
                        data_de_nascimento=data_de_nascimento,
                        instrutor_id=codigo_adm
                    )
                    self.session.add(novo_cliente)
                    self.session.commit()
                    return novo_cliente.id
                except Exception as e:
                    self.session.rollback()  # Reverte qualquer alteração pendente
                    print(f"Erro ao cadastrar usuário: {e}")
                    raise

            elif tabela == 'instrutor':
                try:
                    novo_cliente = Instrutores(
                        nome=nome,
                        email=email,
                        senha=senha,
                        telefone=telefone,
                        endereco=endereco,
                        cpf=cpf,
                        data_de_nascimento=data_de_nascimento,
                        administrador_id=codigo_adm
                    )
                    self.session.add(novo_cliente)
                    self.session.commit()
                    return novo_cliente.id
                except Exception as e:
                    self.session.rollback()
                    print(f"Erro ao cadastrar instrutor: {e}")
                    raise

            elif tabela == 'administrador':
                try:
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
                except Exception as e:
                    self.session.rollback()
                    print(f"Erro ao cadastrar administrador: {e}")
                    raise

            else:
                print("Tabela inválida. Não foi possível cadastrar.")
                return None

        except Exception as e:
            print(f"Erro inesperado durante o cadastro: {e}")
            raise

    def validar_login(self, email, senha):
        try:
            # Busca o cliente com o nome e senha fornecidos
            cliente = self.session.query(Cliente).filter_by(email=email, senha=senha).one_or_none()
            instrutor = self.session.query(Instrutores).filter_by(email=email, senha=senha).one_or_none()
            administrador = self.session.query(Administradores).filter_by(email=email, senha=senha).one_or_none()
            cliente = self.session.query(Cliente).filter_by(email=email, senha=senha).one_or_none()
            instrutor = self.session.query(Instrutores).filter_by(email=email, senha=senha).one_or_none()
            administrador = self.session.query(Administradores).filter_by(email=email, senha=senha).one_or_none()
            if cliente:
                return 'cliente'
            elif instrutor:
                return 'instrutor'
            elif administrador:
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

    def obter_usuario(self, email):
        try:
            cliente = self.session.query(Cliente).filter_by(email=email).one_or_none()
            instrutor = self.session.query(Instrutores).filter_by(email=email).one_or_none()
            administrador = self.session.query(Administradores).filter_by(email=email).one_or_none()
            if cliente:
                return cliente
            elif instrutor:
                return instrutor
            elif administrador:
                return administrador
            else:
                return False
        except SQLAlchemyError as e:
            print(f"Erro ao buscar usuário: {e}")
    
    def obter_aluno(self, nome):
        try:
            cliente = self.session.query(Cliente).filter_by(nome=nome).one_or_none()
            if cliente:
                return cliente
            else:
                return False
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

    def atualizar_notas_instrutor(self, cliente_id, objetivo, atual_data_ficha, renovacao, notas):
        cliente = self.session.query(Cliente).get(cliente_id)
        if cliente:
            cliente.objetivo = objetivo
            cliente.atual_data_ficha = atual_data_ficha
            cliente.renovacao_data_ficha = renovacao
            cliente.notas = notas
            self.session.commit()  # Confirma as alterações no banco
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
        # Buscar o CPF nas três tabelas
        # Buscar o CPF nas três tabelas
        cliente = self.session.query(Cliente).filter_by(cpf=cpf).first()
        if cliente:
            return cliente  # Retorna o cliente se encontrado

        instrutor = self.session.query(Instrutores).filter_by(cpf=cpf).first()
        if instrutor:
            return instrutor  # Retorna o instrutor se encontrado

        administrador = self.session.query(Administradores).filter_by(cpf=cpf).first()
        if administrador:
            return administrador  # Retorna o administrador se encontrado

        return None  # Se não encontrar em nenhuma tabela, retorna None
        if cliente:
            return cliente  # Retorna o cliente se encontrado

        instrutor = self.session.query(Instrutores).filter_by(cpf=cpf).first()
        if instrutor:
            return instrutor  # Retorna o instrutor se encontrado

        administrador = self.session.query(Administradores).filter_by(cpf=cpf).first()
        if administrador:
            return administrador  # Retorna o administrador se encontrado

        return None  # Se não encontrar em nenhuma tabela, retorna None
    
    def consultar_email(self, email):
        # Buscar o e-mail nas três tabelas
        cliente = self.session.query(Cliente).filter_by(email=email).first()
        if cliente:
            return cliente  # Retorna o cliente se encontrado

        instrutor = self.session.query(Instrutores).filter_by(email=email).first()
        if instrutor:
            return instrutor  # Retorna o instrutor se encontrado

        administrador = self.session.query(Administradores).filter_by(email=email).first()
        if administrador:
            return administrador  # Retorna o administrador se encontrado

        return None  # Se não encontrar em nenhuma tabela, retorna None
       