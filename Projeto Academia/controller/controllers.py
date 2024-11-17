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
    
    def pre_cadastrando_admin(self):
        self.repository.pre_cadastrar_administrador()

    # Controlador responsável por criar um produto
    def adicionar_usuario(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento, atual_data_ficha, renovacao_data_ficha, objetivo, codigo_adm, tabela):
        # Convertendo data de nascimento para formato Correto
        data_de_nascimento = datetime.strptime(data_de_nascimento, '%d/%m/%Y').date()
        try:
            # Mudado de self.db para self.controler
            id = self.repository.cadastrar_cliente(nome, email, senha, telefone, endereco, cpf, data_de_nascimento, atual_data_ficha, renovacao_data_ficha, objetivo, codigo_adm, tabela)

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

    def obter_aluno_por_nome(self, nome):
        return self.repository.obter_aluno(nome)

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
        
    def atualizar_medidas(self, id, musculo_selecionado, medida):
        try:
            if self.repository.enviando_medidas(id=id, musculo=musculo_selecionado, medida=medida):
                messagebox.showinfo("Sucesso", f"Medida atualizada com sucesso")
        except Exception as e:
            messagebox.showerror("Erro", f"O erro e {e}")

    def atualizar_notas_instrutor(self, id, objetivo, atual_data_ficha, renovacao, notas):
        try:
            self.repository.atualizar_notas_instrutor(cliente_id=id, objetivo=objetivo, atual_data_ficha=atual_data_ficha, renovacao=renovacao, notas=notas)
            messagebox.showinfo("Sucesso", "Notas atualizadas com sucesso")
        except Exception as e:
            messagebox.showerror("Erro Controler", f"O erro e {e}")

    # Controlador responsável por deletar um produto
    def deletar_usuario(self, usuario_id):
        self.repository.deletar_cliente(usuario_id)

    def validar_cpf(self, cpf):
        # Consultar CPF nas três tabelas
        if self.repository.consultar_cpf(cpf):
            return False  # CPF já está cadastrado em alguma tabela
        
        # Consultar CPF nas três tabelas
        if self.repository.consultar_cpf(cpf):
            return False  # CPF já está cadastrado em alguma tabela
        
        return True  # CPF não cadastrado, pode prosseguir
    
    def validar_email(self, email):
        # Consultar email nas três tabelas
        if self.repository.consultar_email(email):
            return False  # E-mail já está cadastrado em alguma tabela
        
        return True  # E-mail não cadastrado, pode prosseguir
