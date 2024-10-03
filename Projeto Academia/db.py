from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select, func, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Criando Classe do Banco de Dados
class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        self.metadata = MetaData()
        self.connection = self.engine.connect()

# Crindo Tabela ( cajo não exista uma)
    def create_table(self):
        self.usuarios_table = Table('clientes', self.metadata,
                                    Column('id', Integer, primary_key=True, autoincrement=True),
                                    Column('nome', String(100)),
                                    Column('email', String(100)),
                                    Column('senha', String(50)),
                                    Column('telefone', String(50)),
                                    Column('endereco', String(100)),
                                    Column('CPF', String(50)),
                                    Column('Data_de_Nascimento', Date))
        self.metadata.create_all(self.engine)


# Inserir Novo Usuario no Banco de Dados
    def insert_user(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento):
        try:
            insert_stmt = self.usuarios_table.insert().values(nome=nome, email=email, senha=senha, telefone=telefone, endereco=endereco, CPF=cpf, Data_de_Nascimento=data_de_nascimento)
            with self.Session() as session:
                session.execute(insert_stmt)
                session.commit()
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            raise e
        

#verificando se o usuario esta na tabela(usado para o login)
    def verificando_usuario(self, nome_login, senha_login):
        try:
            with self.Session() as session:
                # Consulta para verificar se o usuário existe com nome e senha
                query = select(self.usuarios_table.c.id, self.usuarios_table.c.nome).where(
                    self.usuarios_table.c.nome == nome_login,
                    self.usuarios_table.c.senha == senha_login
                )
                resultado = session.execute(query).first()  # Executa a consulta e pega o primeiro resultado

                if resultado:
                    print("Usuário encontrado:", resultado.nome)
                    return True
                else:
                    print("Usuário não encontrado.")
                    return False
        except SQLAlchemyError as e:
            print("Erro ao verificar usuário:", e)
            return False   


# Deletando algum usuario
    def delete_user(self, user_id):
        try:
            delete_stmt = self.usuarios_table.delete().where(self.usuarios_table.c.id == user_id)
            with self.Session() as session:
                session.execute(delete_stmt)
                session.commit()
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            raise e

# Obter Todos os Usuarios do Banco de Dados
    def get_all_users(self):
        try:
            query = self.usuarios_table.select()
            with self.Session() as session:
                result = session.execute(query)
                users = result.fetchall()
            return users
        except SQLAlchemyError as e:
            raise e
    

    def get_user_by_name(self, nome):
        """Busca o usuário no banco de dados pelo nome"""
        session = self.Session()
        try:
            user = session.query(self.usuarios_table).filter_by(nome=nome).first()
            return user
        except SQLAlchemyError as e:
            print(f"Erro ao buscar usuário: {e}")
        finally:
            session.close()


# Fechar Banco de Dados
    def close(self):
        self.connection.close()