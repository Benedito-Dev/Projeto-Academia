from repository.repositories import ClienteRepository
from tkinter import messagebox
from datetime import datetime

class UsuarioController:
    def __init__(self):
        self.repository = ClienteRepository()  # Instancia o repositório de clientes

    def inicar_banco(self):
        self.repository.init_db()

    # Controlador responsável por criar um produto
    def adicionar_usuario(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento, tabela):
        # Convertendo data de nascimento para formato Correto
        data_de_nascimento = datetime.strptime(data_de_nascimento, '%d/%m/%Y').date()
        try:
            # Mudado de self.db para self.controler
            if self.repository.cadastrar_cliente(nome, email, senha, telefone, endereco, cpf, data_de_nascimento, tabela):
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
                return True
            else:
                messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

    def fazer_login(self, nome, senha):
        # Chama a função validar_login do repository
            try:
                if self.repository.validar_login(nome, senha) == 'cliente':
                    messagebox.showinfo("Sucesso", "Login Efetuado")
                    return 'cliente'
                
                elif self.repository.validar_login(nome, senha) == 'instrutor':
                    messagebox.showinfo("Sucesso", "Login Efetuado")
                    return 'instrutor'
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

    def obter_usuario_por_nome(self, nome):
        return self.repository.obter_usuario(nome)

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
        cliente = self.repository.consultar_cpf(cpf)
        if cliente:
            return False  # CPF já está cadastrado
        return True  # CPF não cadastrado, pode prosseguir
    
    def validar_email(self,email):
        cliente = self.repository.consultar_email(email)
        if cliente:
            return False # Email já está cadastrado
        return True # Email não cadastrado, pode prosseguir
        
