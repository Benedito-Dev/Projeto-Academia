import tkinter as tk
from time import sleep
import re
from tkinter import ttk
from customtkinter import CTkLabel, CTkButton, CTkFrame
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime, date
from controller.controllers import UsuarioController




class Funções():
    def __init__(self):
        self.controler = UsuarioController()

    def pre_cadastramento_administrador(self):
        self.controler.pre_cadastrando_admin()

    def Exibir_senha(self):
        if self.check_senha.get() == 1:
            self.entry_senha.configure(show="")
        else:
            self.entry_senha.configure(show="*")

    def limpar_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
    
    def submit_feedback(self):

        feedback = self.feedback_text.get("1.0", "end-1c")

        messagebox.showinfo("Sucesso", f"Feedback enviado: {feedback}.")

        self.feedback_text.delete("1.0", "end")


    def iniciar_carrossel_imagens(self, titulo, frame, exercicios, largura, altura):
        # Carrega as imagens e informações dos exercícios
        imagens_carregadas = [
            {
                "imagem": [ImageTk.PhotoImage(frame.copy().resize((largura, altura))) for frame in ImageSequence.Iterator(Image.open(ex["imagem"]))],
                "nome": ex["nome"],
                "series": ex["series"],
                "repeticoes": ex["repeticoes"]
            } for ex in exercicios
        ]
        index = 0
        frame_index = 0  # Índice do quadro atual do GIF

        # Variável de controle para a chamada do `after`
        atualizacao_id = None  # Esta variável irá armazenar o id da função `after` para cancelamento futuro

        #Label para exibir titulo do exericios
        label_titulo = CTkLabel(frame, text=titulo, text_color="white", font=("Arial", 22, 'bold'))
        label_titulo.grid(row=0, column=0, columnspan=3, pady=20)

        border_frame = CTkFrame(frame, fg_color="#7fd350", corner_radius=10)
        border_frame.grid(row=1, column=1)

        # Label para exibir o GIF no carrossel
        label_imagem = CTkLabel(border_frame, text="")
        label_imagem.grid(row=0, column=1, padx=10, pady=10)

        # Label para exibir o texto do exercício
        label_texto = CTkLabel(frame, text="", text_color="white", font=("Arial", 16, 'bold'))
        label_texto.grid(row=3, column=1, pady=10)

        # Função para atualizar o GIF
        def atualizar_gif():
            nonlocal frame_index, atualizacao_id
            exercicio_atual = imagens_carregadas[index]
            label_imagem.configure(image=exercicio_atual["imagem"][frame_index])
            frame_index = (frame_index + 1) % len(exercicio_atual["imagem"])
                
                # Cancelar a atualização anterior, se houver
            if atualizacao_id is not None:
                    self.after_cancel(atualizacao_id)

            # Agendar a próxima atualização
            atualizacao_id = self.after(200, atualizar_gif)  # Atualiza o GIF a cada 300ms (ajustado para mais devagar)

        # Função para exibir a imagem e o texto atual
        def exibir_imagem():
            nonlocal frame_index
            frame_index = 0  # Reseta o quadro ao mudar de exercício
            exercicio_atual = imagens_carregadas[index]
            label_texto.configure(text=f"{exercicio_atual['nome']}: {exercicio_atual['series']} séries de {exercicio_atual['repeticoes']} repetições")
            atualizar_gif()

        # Funções para controle do carrossel
        def mostrar_proximo():
            nonlocal index
            index = (index + 1) % len(imagens_carregadas)
            exibir_imagem()

        def mostrar_anterior():
            nonlocal index
            index = (index - 1) % len(imagens_carregadas)
            exibir_imagem()

        # Botões de controle
        btn_anterior = CTkButton(frame, text="⟵ Anterior", fg_color="#808080", hover_color="#A9A9A9", command=mostrar_anterior)
        btn_anterior.grid(row=1, column=0, padx=5, pady=5)

        btn_proximo = CTkButton(frame, text="Próximo ⟶", fg_color="#808080", hover_color="#A9A9A9", command=mostrar_proximo)
        btn_proximo.grid(row=1, column=2, padx=5, pady=5)

        # Exibe a primeira imagem e texto
        exibir_imagem()


    def mudar_exercicios(self, titulo, novos_exercicios, central_frame):

        """Muda os exercícios exibidos para o carrossel."""
        self.exercicios_atual = novos_exercicios
        self.indice_atual = 0
        # Limpa o frame central, exceto o botão finalizador
        for widget in central_frame.winfo_children():
            widget.destroy()

        # Reinicia o carrossel de imagens
        self.iniciar_carrossel_imagens(titulo, central_frame, self.exercicios_atual, 200, 200)

            
    def carregar_perfis(self):
        try:
            # Obtendo os dados da tabela através do controlador
            users = self.controler.listar_usuarios()

            instrutores = self.controler.listar_instrutores()

            # Inserindo os dados na ordem correta no TreeView
            for user in users:
                id = user.id  # Acessando o atributo 'id'
                nome = user.nome  # Acessando o atributo 'nome'
                email = user.email  # Acessando o atributo 'email'
                nome_instrutor = 'Teste'

                for instrutor in instrutores:
                    if instrutor.id == user.instrutor_id:
                        nome_instrutor = instrutor.nome
                self.tree.insert('', tk.END, values=(id, nome, email, nome_instrutor))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar perfis: {e}")

    
    def obter_alunos_por_instrutor(self):
        try:
            # Obtendo os dados da tabela através do controlador
            instrutores = self.controler.listar_instrutores()
            users = self.controler.listar_usuarios()
            alunos = []

            for instrutor in instrutores:
                if instrutor.nome.upper() == self.nome_usuario.upper():
                    instrutor_atual = instrutor.id
            
            for user in users:
                if user.instrutor_id == instrutor_atual:
                    alunos.append(user.nome)
            
            return alunos
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao Obter alunos: {e}")
    
    def obter_informacoes_aluno(self, nome):
        user_nome = nome

        try:
            user = self.controler.obter_aluno_por_nome(user_nome)
            if user:
                self.aluno = user
                return self.aluno
            else:
                messagebox.showinfo("Info", "Usuario não encontrado")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Ao buscar informações : {e}")

    def get_informacao_aluno(self, informacao):
        return getattr(self.aluno, informacao, None)


    def validar_dados(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()
        telefone = self.entry_telefone.get().strip()
        endereco = self.entry_endereco.get().strip()
        cpf = self.entry_cpf.get().strip()
        data_de_nascimento = self.entry_dataDeNascimento.get().strip()
        objetivo = self.menu_Objetivos.get().strip()
        data_ficha = datetime.now().strftime("%d-%m-%Y")
        codigo = self.entry_codigo_de_administrador.get().strip()
        tabela = self.tabela.get()

        # Validação do nome (mínimo de 3 letras, apenas caracteres alfabéticos)
        if len(nome) < 3 or not nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return

        # Validação de e-mail (usando expressão regular)
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, email):
            messagebox.showerror("Erro", "Por favor, insira um e-mail válido.")
            return
        
        if not self.controler.validar_email(email):
            messagebox.showerror("Erro", "Email já cadastrado no sistema. ")
            return

        # Validação de senha (mínimo de 8 caracteres, deve conter letras e números)
        if len(senha) < 8 or not any(char.isdigit() for char in senha) or not any(char.isalpha() for char in senha):
            messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres e conter letras e números.")
            return

        # Validação de telefone (deve conter apenas dígitos e ter 10 ou 11 números)
        if not telefone.isdigit() or not (10 <= len(telefone) <= 11):
            messagebox.showerror("Erro", "O telefone deve conter apenas números e ter 10 ou 11 dígitos.")
            return

        # Validação de endereço (mínimo de 5 caracteres, qualquer valor é permitido)
        if len(endereco) < 5:
            messagebox.showerror("Erro", "O endereço deve ter pelo menos 5 caracteres.")
            return

        if len(cpf) != 11:  # Corrigido para verificar se o CPF tem exatamente 11 dígitos
            messagebox.showerror("Erro", "O CPF deve ter exatamente 11 dígitos.")
            return
        
        # Verifica se o CPF já está cadastrado
        if not self.controler.validar_cpf(cpf):
            messagebox.showerror("Erro", "O CPF já está cadastrado no sistema.")
            return
        
        if self.validar_data(data_de_nascimento):
            messagebox.showerror("Erro", "Insira uma data valida por favor")
            return
        
        if tabela != "Administrador":
            if not codigo or codigo.isnumeric() == False:
                messagebox.showerror("Erro", "Digite o codigo de maneira correta")

        # Se todos os dados estiverem válidos, prosseguir com a lógica de envio
        self.enviar_dados(nome=nome, email=email, senha=senha, telefone=telefone, endereco=endereco, cpf=cpf, data_de_nascimento=data_de_nascimento, objetivo=objetivo, data_ficha=data_ficha, codigo_adm=codigo, tabela=tabela)

    # Função para validar a idade do novo usuário

    def enviar_dados(self, nome, email, senha, telefone, endereco, cpf, data_de_nascimento, objetivo, data_ficha, codigo_adm, tabela):
        if self.controler.adicionar_usuario(nome, email, senha, telefone, endereco, cpf, data_de_nascimento, data_ficha, objetivo, codigo_adm, tabela):
            self.after(500, self.Home)


    def validar_data(self, data_nascimento_str):
        try:
            if isinstance(data_nascimento_str, date):
                data_nascimento = data_nascimento_str
            
            else:
                data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()

            # Obtém a data atual
            data_atual = datetime.now().date()

            # Verifica se a data de nascimento é no futuro
            if data_nascimento > data_atual:
                return True

            # Calcula a diferença de anos
            idade = data_atual.year - data_nascimento.year

            # Ajusta a idade caso o aniversário ainda não tenha ocorrido este ano
            if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            # Verifica se a idade é menor que 12
            if idade >= 12:
                return False
            
            else :
                return True

        except ValueError as e:
                # Retorna False se o formato da data for inválido
                print(f"O erro é {e}")
                return False


    def abrir_calendario(self):
        janela_calendario = tk.Toplevel(self)
        janela_calendario.title("Selecione a data de nascimento")

        calendario = Calendar(janela_calendario, selectmode="day", year=2000, month=1, day=10)
        calendario.pack(pady=20)

        def pegar_data():
            data_selecionada = calendario.get_date()
            # Convertendo a data para o formato "YYYY-MM-DD"
            self.entry_dataDeNascimento.delete(0, tk.END)
            self.entry_dataDeNascimento.insert(0, data_selecionada)
            janela_calendario.destroy()

        btn_selecionar_data = ttk.Button(janela_calendario, text="Selecionar", command=pegar_data)
        btn_selecionar_data.pack(pady=10)

    def validando_login(self):
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()

        usuario = self.controler.fazer_login(email, senha)
        
        # Chama o método do controlador para validar o login
        if usuario == 'cliente':
            self.email = email
            self.senha_usuario = senha
            self.after(500, self.Home)
        
        elif usuario == 'instrutor':
            self.email = email
            self.senha_usuario = senha
            self.instrutor = True
            self.after(500, self.Home)

        elif usuario == 'administrador':
            self.email = email
            self.senha_usuario = senha.capitalize()
            self.administrador = True
            self.after(500, self.Home)
        else:
            pass
    
    def puxar_informacoes(self):
        user_email = self.email.strip()

        try:
            user = self.controler.obter_usuario_por_email(user_email)


            if user:
                self.informacoes = user

            else:
                messagebox.showinfo("Info", "Usuario não encontrado")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Ao buscar informações : {e}")

    def get_informacao(self, informacao):
        return getattr(self.informacoes, informacao, None)
    
    def enviar_medidas(self, musculo):
        id_cliente = self.get_informacao("id")
        nova_medida = self.entry_musculo.get() or self.get_informacao(musculo)
        self.controler.atualizar_medidas(id=id_cliente, musculo_selecionado=musculo, medida=nova_medida)
        
    
    def validar_alteracoes(self):
        id_cliente = self.get_informacao("id")  # Renomeado para id_cliente para maior clareza

        novo_nome = self.entry_novo_nome.get().strip().upper() or self.get_informacao("nome").upper()
        nova_data_de_nascimento = self.entry_dataDeNascimento.get().strip() or self.get_informacao("data_de_nascimento")
        novo_endereco = self.entry_novo_endereco.get() or self.get_informacao("endereco")
        novo_telefone = self.entry_novo_telefone.get().strip() or self.get_informacao("telefone")
        novo_email = self.entry_novo_email.get().strip() or self.get_informacao("email")
        nova_senha = self.entry_nova_senha.get().strip() or self.get_informacao("senha")

        # Validação do nome
        if len(novo_nome) < 3 or not novo_nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return

        # Validação de e-mail
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, novo_email):
            messagebox.showerror("Erro", "Por favor, insira um e-mail válido.")
            return

        # Validação de senha
        if len(nova_senha) < 8 or not any(char.isdigit() for char in nova_senha) or not any(char.isalpha() for char in nova_senha):
            messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres e conter letras e números.")
            return

        # Validação de telefone
        if not novo_telefone.isdigit() or not (10 <= len(novo_telefone) <= 11):
            messagebox.showerror("Erro", "O telefone deve conter apenas números e ter 10 ou 11 dígitos.")
            return

        # Validação de endereço
        if len(novo_endereco) < 5:
            messagebox.showerror("Erro", "O endereço deve ter pelo menos 5 caracteres.")
            return

         # Validação de data de nascimento
        if self.validar_data(nova_data_de_nascimento):
             messagebox.showerror("Erro", "Data de nascimento inválida ou você deve ter mais de 12 anos.")
             return

        # Chamada para salvar alterações
        self.salvar_alterações(id_cliente, novo_nome, novo_email, nova_senha, novo_telefone, novo_endereco, nova_data_de_nascimento)
    
    def salvar_alterações(self, id, nome, email, senha, telefone, endereco, data_de_nascimento):
        if not data_de_nascimento:
            messagebox.showerror("Erro", "Data de nascimento inválida")
            return

        try:
            self.controler.atualizar_usuario(id=id, nome=nome, data_de_nascimento=data_de_nascimento, endereco=endereco, telefone=telefone, email=email, senha=senha)
            self.after(500, self.Home)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar alterações: {e}")


    def deletar_perfil(self):
        # Verifica se há algum item selecionado
        if not (selected_item := self.tree.selection()):
            return messagebox.showwarning("Aviso", "Nenhum perfil selecionado.")

        user_id = self.tree.item(selected_item[0])['values'][0]  # Pega o ID do perfil selecionado

        # Confirmação
        if messagebox.askyesno("Confirmar", f"Você tem certeza que deseja deletar o perfil ID '{user_id}'?"):
            try:
                # Controlador lida com a exclusão no banco de dados e na visualização
                self.controler.deletar_usuario(user_id)
                self.tree.delete(selected_item[0])  # Remove o item da visualização
                messagebox.showinfo("Sucesso", "Perfil deletado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar perfil: {e}")


    def Encerrar_programa(self):
        self.destroy()