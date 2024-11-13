from repository.repositories import ClienteRepository
from tkinter import messagebox
from datetime import datetime

class UsuarioController:
    def __init__(self):
        self.repository = ClienteRepository()  # Instancia o repositório de clientes

    def iniciar_banco(self):
        self.repository.init_db()
    
    def pre_cadastrando_admin(self):
        self.repository.pre_cadastrar_administrador()

    # Controlador responsável por criar um produto
    def adicionar_usuario(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento, codigo_adm, tabela):
        # Convertendo data de nascimento para formato Correto
        data_de_nascimento = datetime.strptime(data_de_nascimento, '%d/%m/%Y').date()
        try:
            # Mudado de self.db para self.controler
            id = self.repository.cadastrar_cliente(nome, email, senha, telefone, endereco, cpf, data_de_nascimento, codigo_adm, tabela)

            if id > 0:
                if tabela == 'instrutor':
                    messagebox.showinfo("Sucesso",  f"Cadastro realizado com sucesso!, O Codigo Adm do seu intrutor é {id}")
                elif tabela == "administrador":
                    messagebox.showinfo("Sucesso", f"Cadastro realizado! O seu código adm é {id}")
                else:
                    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
                return True
                
            else:
                messagebox.showerror("Erro", "Erro ao cadastrar usuário: ID retornado é inválido.")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar-se usuário: {e}")

    def fazer_login(self, email, senha):
        # Chama a função validar_login do repository
            try:
                if self.repository.validar_login(email, senha) == 'cliente':
                    messagebox.showinfo("Sucesso", "Login Efetuado")
                    return 'cliente'
                
                elif self.repository.validar_login(email, senha) == 'instrutor':
                    messagebox.showinfo("Sucesso", "Login Efetuado")
                    return 'instrutor'

                elif self.repository.validar_login(email, senha) == 'administrador':
                    messagebox.showinfo("Sucesso", "Login Efetuado")
                    return 'administrador'
                else :
                    messagebox.showerror("Erro", "Login Não encontrado")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro em nosso sistema, aguarde... {e}")
            
    # Controlador responsável por obter os produtos para exibir na interface
    def listar_usuarios(self):
        return self.repository.obter_usuarios()
    
    # listar Instrutores
    def listar_instrutores(self):
        return self.repository.obter_instrutores()

    def obter_usuario_por_email(self, email):
        return self.repository.obter_usuario(email)

    # Controlador responsável por atualizar um produto
    def atualizar_usuario(self, id, nome, data_de_nascimento, endereco, telefone, email, senha):
        try:
            nome = nome
            data_de_nascimento = data_de_nascimento
            endereco = endereco
            telefone = telefone
            email = email
            senha = senha
            self.repository.atualizar_cliente(id, nome=nome, email=email, senha=senha, telefone=telefone, endereco=endereco, data_de_nascimento=data_de_nascimento)
            messagebox.showinfo("Sucesso", "Informações Alteradas com sucesso")

        except Exception as e:
            raise Exception(f"Erro ao atualizar usuário: {e}")

    # Controlador responsável por deletar um produto
    def deletar_usuario(self, usuario_id):
        self.repository.deletar_cliente(usuario_id)

    def validar_cpf(self, cpf):
        # Consultar CPF nas três tabelas
        if self.repository.consultar_cpf(cpf):
            return False  # CPF já está cadastrado em alguma tabela
        
        return True  # CPF não cadastrado, pode prosseguir
    
    def validar_email(self, email):
        # Consultar email nas três tabelas
        if self.repository.consultar_email(email):
            return False  # E-mail já está cadastrado em alguma tabela
        
        return True  # E-mail não cadastrado, pode prosseguir
    
    from datetime import datetime

class CalendarioController:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.ano_atual = datetime.now().year
        self.mes_atual = datetime.now().month

    def adicionar_evento(self, data, descricao):
        evento = Evento(data, descricao)
        self.repositorio.adicionar_evento(evento)

    def listar_eventos_mes(self):
        return self.repositorio.listar_eventos_mes(self.ano_atual, self.mes_atual)

    def proximo_mes(self):
        if self.mes_atual == 12:
            self.mes_atual = 1
            self.ano_atual += 1
        else:
            self.mes_atual += 1

    def mes_anterior(self):
        if self.mes_atual == 1:
            self.mes_atual = 12
            self.ano_atual -= 1
        else:
            self.mes_atual -= 1

