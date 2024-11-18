import tkinter as tk
from sqlalchemy import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
from functools import partial
from PIL import Image
from view.funcoes import Funções
from view.treinos_usuario_view import Treinos
from controller.controllers import UsuarioController
from controller.enviando_email import EnviandoEmail




# Configurações do CustomTkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Application(tk.Tk, Funções, Treinos):
    def __init__(self):
        super().__init__()
        self.title("4 Fitness")
        self.geometry("800x600")
        self.current_page = 0
        self.controler = UsuarioController()
        self.emails = EnviandoEmail()
        self.Treinos = Treinos()
        self.state('zoomed')
        self.menu_inicial()



# Janelas

    def menu_inicial(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.pre_cadastramento_administrador()
        
        self.pre_cadastramento_administrador()
        
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)

        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0) 

        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Logo.png"
        self.logo_image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image = ctk.CTkLabel(background_frame, image=self.logo_image, text="")
        self.label_image.grid(row=1, column=0, pady=(60, 0))

        border_frame = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=10)
        border_frame.grid(row=2, column=0, padx=20, pady=20)

        # Frame para centralizar o conteúdo
        frame = ctk.CTkFrame(border_frame, fg_color="#313131", corner_radius=10)
        frame.grid(row=0, column=0, padx=10, pady=10)
        
        #Titulo
        titulo = ctk.CTkLabel(frame, text="4 FITNESS", text_color="white", font=("Arial", 40))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)

        #Botoes
        ctk.CTkButton(frame, text="Menu Login", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.realizar_login).grid(row=1, column=0, columnspan=2, pady=30, padx=60)
        
        ctk.CTkButton(frame, text="Encerrar Programa", font=("Arial", 18), width=160, fg_color="#808080",  hover_color="#A9A9A9", command=self.Encerrar_programa).grid(row=3, column=0, columnspan=2, pady=30, padx=60)


    def realizar_login(self):
        # Remove widgets existentes
        for widget in self.winfo_children():
            widget.destroy()
        
        self.instrutor = False
        self.administrador = False

        # Criação do frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)
        
        # Configuração de colunas e linhas para centralizar
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0)  # Para centralizar verticalmente
        # Imagem

        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Logo.png"

        self.logo_image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image = ctk.CTkLabel(background_frame, image=self.logo_image, text="")
        self.label_image.grid(row=0, column=0, pady=0)

        # Frame para a borda
        border_frame = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=10)
        border_frame.grid(row=1, column=0, padx=20, pady=20)

        # Frame para centralizar o conteúdo
        frame = ctk.CTkFrame(border_frame, fg_color="#313131", corner_radius=10)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Título
        titulo = ctk.CTkLabel(frame, text="Realizar login", text_color="white", font=("Arial", 20))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Email do usuário
        ctk.CTkLabel(frame, text="Email:", text_color="white", font=("Arial", 14)).grid(row=1, column=0, sticky="e", padx=10)
        self.entry_email = ctk.CTkEntry(frame, placeholder_text="Email")
        self.entry_email.grid(row=1, column=1, pady=5, padx=20)
        # Email do usuário
        ctk.CTkLabel(frame, text="Email:", text_color="white", font=("Arial", 14)).grid(row=1, column=0, sticky="e", padx=10)
        self.entry_email = ctk.CTkEntry(frame, placeholder_text="Email")
        self.entry_email.grid(row=1, column=1, pady=5, padx=20)

        # Senha
        ctk.CTkLabel(frame, text="Senha:", text_color="white", font=("Arial", 14)).grid(row=2, column=0, sticky="e", padx=10)
        self.entry_senha = ctk.CTkEntry(frame, show="*", placeholder_text="Senha")
        self.entry_senha.grid(row=2, column=1, pady=5, padx=20)

        # Checkbutton para mostrar senha
        self.check_senha = ctk.IntVar()
        check = ctk.CTkCheckBox(frame, text="Mostrar senha", text_color="white", variable=self.check_senha, command=self.Exibir_senha)
        check.grid(row=3, column=0, columnspan=2, pady=5)

        # Botão de validar
        ctk.CTkButton(frame, text="Acessar", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.validando_login).grid(row=4, column=0, columnspan=2, pady=10)

        # Botão de voltar
        ctk.CTkButton(frame, text="Voltar", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.menu_inicial).grid(row=6, column=0, columnspan=2, pady=10)


    def cadastrar_cliente(self):
          # Remove widgets existentes
          # Remove widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Configuração de colunas e linhas para centralizar
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0)  # Para centralizar verticalmente

        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Logo.png"
        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Logo.png"
        self.logo_image = ctk.CTkImage(light_image=Image.open(image_path), size=(120, 120))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image = ctk.CTkLabel(background_frame, image=self.logo_image, text="")
        self.label_image.grid(row=1, column=0, pady=(00, 0))

        border_frame = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=10)
        border_frame.grid(row=2, column=0, padx=20, pady=00)
        
        # Frame para centralizar o conteúdo
        frame = ctk.CTkFrame(border_frame, fg_color="#313131",corner_radius=10)
        frame.grid(padx=10, pady=10)

        # Título
        title = ctk.CTkLabel(frame, text="Realizar cadastro", text_color="white", font=("Arial", 20, 'italic'))
        title.grid(row=0, column=1, pady=(15, 20), padx=(5, 00))

       
       
        # Nome
        nome_emoji = ctk.CTkLabel(frame, text="👤", text_color="white", font=("Arial", 16))
        nome_emoji.grid(row=1, column=0, padx=(60, 00))
        self.entry_nome = ctk.CTkEntry(frame, placeholder_text="Nome do Usuario")
        self.entry_nome.grid(row=1, column=1, pady=5)

        # Email
        email_emoji = ctk.CTkLabel(frame, text="📧", text_color="white", font=("Arial", 16))
        email_emoji.grid(row=2, column=0, padx=(60, 00))
        self.entry_email = ctk.CTkEntry(frame, placeholder_text="Email")
        self.entry_email.grid(row=2, column=1, pady=5)

        # Senha
        senha_emoji = ctk.CTkLabel(frame, text="🔒", text_color="white", font=("Arial", 16))
        senha_emoji.grid(row=3, column=0, padx=(60, 00))
        self.entry_senha = ctk.CTkEntry(frame, show="*", placeholder_text="Senha")
        self.entry_senha.grid(row=3, column=1, pady=5)

        # Checkbutton para mostrar senha
        self.check_senha = ctk.IntVar()
        check_button = ctk.CTkCheckBox(frame, text="Mostrar senha", text_color="white", variable=self.check_senha, command=self.Exibir_senha)
        check_button.grid(row=3, column=2, sticky="w", padx=10)  # Posicionando à esquerda

        # Telefone
        telefone_emoji = ctk.CTkLabel(frame, text="📞", text_color="white", font=("Arial", 16))
        telefone_emoji.grid(row=4, column=0, padx=(60, 00))
        self.entry_telefone = ctk.CTkEntry(frame, placeholder_text="Telefone")
        self.entry_telefone.grid(row=4, column=1, pady=5)

        # Endereço
        endereco_emoji = ctk.CTkLabel(frame, text="🏠", text_color="white", font=("Arial", 16))
        endereco_emoji.grid(row=5, column=0, padx=(60, 0))
        self.entry_endereco = ctk.CTkEntry(frame, placeholder_text="Endereço")
        self.entry_endereco.grid(row=5, column=1, pady=5)

        #CPF
        cpf_emoji = ctk.CTkLabel(frame, text="🆔", text_color="white", font=("Arial", 16))
        cpf_emoji.grid(row=6, column=0, padx=(60, 00)) 
        self.entry_cpf = ctk.CTkEntry(frame, placeholder_text="CPF")
        self.entry_cpf.grid(row=6,column=1, pady=5)
        
        #Data de nascimento
        self.entry_dataDeNascimento = ctk.CTkEntry(frame, placeholder_text="DD/MM/YYYY")
        self.entry_dataDeNascimento.grid(row=7, column=1, pady=5)
        btn_abrir_calendario = ctk.CTkButton(frame, text="🗓️", font=("Arial", 16, 'bold'), fg_color="#313131", hover_color="#313131", width=15, command=partial(self.abrir_calendario, self.entry_dataDeNascimento, ano_inicial=2005))
        btn_abrir_calendario.grid(row=7, column=0, padx=(83, 0))

        btn_abrir_calendario = ctk.CTkButton(frame, text="Escolher data", command=partial(self.abrir_calendario, self.entry_dataDeNascimento, ano_inicial=2005))
        btn_abrir_calendario.grid(row=7, column=2, padx=5)

        Objetivos = ["Emagrecimento", "Ganho de Massa", "Definição Muscular"]

        self.aluno_selecionado = ctk.StringVar(value=Objetivos[0])

        nome_emoji = ctk.CTkLabel(frame, text="🦾", text_color="white", font=("Arial", 16))
        nome_emoji.grid(row=8, column=0, padx=(60, 00))
        self.menu_Objetivos = ctk.CTkOptionMenu(frame, variable=self.aluno_selecionado, values=Objetivos)
        self.menu_Objetivos.grid(row=8, column=1, padx=5, pady=10)

        #Codigo Administrador
        codigo_emoji = ctk.CTkLabel(frame, text="🔑", text_color="white", font=("Arial", 16))
        codigo_emoji.grid(row=9, column=0, padx=(60, 00))
        self.entry_codigo_de_administrador = ctk.CTkEntry(frame, placeholder_text="Codigo de Admin")
        self.entry_codigo_de_administrador.grid(row=9, column=1, pady=5)

        self.tabela = ctk.StringVar(value="usuario")
        if self.instrutor:                
            # Ajustes estéticos para RadioButton no CustomTkinter
            Opção_1 = ctk.CTkRadioButton(
                frame,
                text="Usuário",
                variable=self.tabela,
                value="usuario",
                font=("Arial", 14),
                text_color="white",
                hover_color="#7fd350",  # Cor ao passar o mouse
                fg_color="#5ce1e6"      # Cor de seleção para contraste com o fundo
        )
            Opção_1.grid(row=10, column=1, padx=(10, 10), pady=(10, 10))
        else:
            # Ajustes estéticos para RadioButton no CustomTkinter
            Opção_1 = ctk.CTkRadioButton(
                frame,
                text="Usuário",
                variable=self.tabela,
                value="usuario",
                font=("Arial", 14),
                text_color="white",
                hover_color="#7fd350",  # Cor ao passar o mouse
                fg_color="#5ce1e6"      # Cor de seleção para contraste com o fundo
        )
            Opção_1.grid(row=10, column=0, padx=(10, 10), pady=(10, 10))     


            Opção_2 = ctk.CTkRadioButton(
                frame,
                text="Instrutor",
                variable=self.tabela,
                value="instrutor",
                font=("Arial", 14),
                text_color="white",
                hover_color="#7fd350",
                fg_color="#5ce1e6"
            )
            Opção_2.grid(row=10, column=1, padx=(10, 10), pady=(10, 10))

            Opção_3 = ctk.CTkRadioButton(
                frame,
                text="Administrador",
                variable=self.tabela,
                value="administrador",
                font=("Arial", 14),
                text_color="white",
                hover_color="#7fd350",
                fg_color="#5ce1e6"
            )
            Opção_3.grid(row=10, column=2, padx=(10, 10), pady=(10, 10))
        

        # Botão Cadastrar-se
        ctk.CTkButton(frame,text="Cadastrar-se",fg_color="#808080", hover_color="#A9A9A9", font=("Arial", 18), command=self.validar_dados).grid(row=11,column=1,pady=10)

        # Botão Voltar
        ctk.CTkButton(frame, text="Voltar",fg_color="#808080", hover_color="#A9A9A9", font=("Arial", 18), command=self.Home).grid(row=12, column=1,pady=10)


    def Home(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.puxar_informacoes()
        self.nome_usuario = self.get_informacao('nome')
        
        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="4 FITNESS", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        log_out = ctk.CTkButton(frame_superior, text=" ⬅ Log Out", text_color="white", fg_color='#ED1B24', hover_color='#242424', font=("Arial", 14, 'bold'), height=20, command=self.realizar_login)
        log_out.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario.lower().capitalize().lower().capitalize()}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.50, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame
        central_frame.place(relx=0.50, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        #Imagem Perfil

        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Home\\Perfil.png"
        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Home\\Perfil.png"

        self.logo_image_perfil = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_perfil = ctk.CTkLabel(central_frame, image=self.logo_image_perfil, text="")
        self.label_image_perfil.grid(row=0, column=0, pady=0)

        # Colocando os botões lado a lado usando grid (CustomTkinter)
        btn_perfil = ctk.CTkButton(central_frame, text="Perfil", fg_color="#808080", hover_color="#A9A9A9", command=self.Perfil_usuario, font=("Arial", 18, "bold"), width=150, height=50)
        btn_perfil.grid(row=0, column=0, pady=(250, 00))


        if self.instrutor or self.administrador:
            # Botão de criar conta
            image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Home\\btn_cadastrar.png"
            self.label_image_cadastrar = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))
            self.label_image_cadastrar = ctk.CTkLabel(central_frame, image=self.label_image_cadastrar, text="")
            self.label_image_cadastrar.grid(row=0, column=3, pady=0)
            ctk.CTkButton(central_frame, text="Cadastrar", font=("Arial", 18), width=160, height=50, fg_color="#808080",  hover_color="#A9A9A9", command=self.cadastrar_cliente).grid(row=0, column=3, pady=(250, 00))
            image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\admin\\Gerenciamento.webp"
            self.label_image_cadastrar = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))
            self.label_image_cadastrar = ctk.CTkLabel(central_frame, image=self.label_image_cadastrar, text="")
            self.label_image_cadastrar.grid(row=0, column=4, pady=0)
            ctk.CTkButton(central_frame, text="Gerenciar Perfis", font=("Arial", 18), width=160, height=50, fg_color="#808080",  hover_color="#A9A9A9", command=self.Gerenciamento).grid(row=0, column=4, pady=(250, 00))

        else:            
            image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Home\\Modalidades.png"
            self.logo_image_modalidades = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

            # Criar um Label para exibir a imagem
            self.label_image_modalidades = ctk.CTkLabel(central_frame, image=self.logo_image_modalidades, text="")
            self.label_image_modalidades.grid(row=0, column=1, pady=0)
            btn_modalidades = ctk.CTkButton(central_frame, text="Modalidades", fg_color="#808080", hover_color="#A9A9A9", command=self.Modalidades, font=("Arial", 18, "bold"), width=150, height=50)
            btn_modalidades.grid(row=0, column=1, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Home\\Ajustes.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=2, pady=0)

        btn_ajustes = ctk.CTkButton(central_frame, text="Ajustes", fg_color="#808080", hover_color="#A9A9A9", command=self.Ajustes, font=("Arial", 18, "bold"), width=150, height=50)
        btn_ajustes.grid(row=0, column=2, pady=(250, 00))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)

        if self.administrador:
            pass
        else:
            feedback_btn = ctk.CTkButton(frame_inferior, text="Feedback", fg_color="#808080", hover_color="#A9A9A9", command=self.Feedback, font=("Arial", 18, "bold"))
            feedback_btn.pack(side='right', padx=10, pady=10)


    def tela_instrutor(self):
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)

        btn_voltar = ctk.CTkButton(frame_inferior, fg_color="#808080", hover_color="#A9A9A9", command=self.Gerenciamento, text="Voltar")
        btn_voltar.pack(side="top", pady=5)

        fundo_verde = ctk.CTkFrame(background_frame, fg_color="#7fd350",corner_radius=20, width=1000, height=600)
        fundo_verde.pack(side="right", padx=(00, 180))
        fundo_verde.grid_propagate(False)

        # btn_salvar_alterações = ctk.CTkButton(fundo_verde, text="Salvar alterações", fg_color="#808080", hover_color="#A9A9A9")
        # btn_salvar_alterações.grid(row=3, column=0)

        frame_esquerda = ctk.CTkFrame(background_frame, fg_color="#313131", corner_radius=10)
        frame_esquerda.pack(side="left", fill="y", pady=20, padx=(280, 10))

        alunos = self.obter_alunos_por_instrutor()

        self.aluno_selecionado = ctk.StringVar(value=alunos[0])
        self.obter_informacoes_aluno(nome=self.aluno_selecionado.get())

        def update_placeholder(*args):
                self.obter_informacoes_aluno(nome=self.aluno_selecionado.get())
                self.objetivo_entry.configure(placeholder_text=f"{self.get_informacao_aluno('objetivo')}")
                data_validade.configure(text=f"{self.formatar_data(self.get_informacao_aluno("renovacao_data_ficha"))}")
                self.validade_entry.configure(placeholder_text=f"{self.formatar_data(self.get_informacao_aluno('atual_data_ficha'))}")
                self.comentarios_textbox.delete("1.0", "end")
                if self.get_informacao_aluno("notas") == None:
                    self.comentarios_textbox.insert(index="1.0", text="O Aluno ainda não possui anotações pessoais")
                else:
                    self.comentarios_textbox.insert(index="1.0", text=self.get_informacao_aluno("notas"))
        
        self.aluno_selecionado.trace_add("write", update_placeholder)

        nome_emoji = ctk.CTkLabel(frame_esquerda, text="👤", text_color="white", font=("Arial", 16))
        nome_emoji.grid(row=0, column=0, padx=(10, 0))
        menu_alunos = ctk.CTkOptionMenu(frame_esquerda, variable=self.aluno_selecionado, values=alunos)
        menu_alunos.grid(row=0, column=1, padx=(20, 10), pady=40)

        # Conteúdos para o fundo_verde
        titulo_label = ctk.CTkLabel(fundo_verde, text="Acompanhamento", text_color="white", font=("Arial", 22, "bold"))
        titulo_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=400)

        # Campo de Objetivo
        objetivo_label = ctk.CTkLabel(fundo_verde, text="Objetivo", text_color="white", font=("Arial", 18, "bold"))
        objetivo_label.grid(row=1, column=0, sticky="w", padx=(20, 0), pady=(10, 5))

        self.objetivo_entry = ctk.CTkEntry(fundo_verde, placeholder_text=f"{self.get_informacao_aluno('objetivo')}", width=180)
        self.objetivo_entry.grid(row=2, column=0, sticky="w", padx=(60, 0), pady=(10, 5))

        # Campo de Validade da Ficha
        validade_label = ctk.CTkLabel(fundo_verde, text="Validade da Ficha:", text_color="white", font=("Arial", 18, "bold"))
        validade_label.grid(row=3, column=0, sticky="w", padx=(20, 0), pady=(20, 5))

        data_validade = ctk.CTkLabel(fundo_verde, text=f"{self.formatar_data(self.get_informacao_aluno("renovacao_data_ficha"))}", text_color="red", font=("Arial", 16, "bold"))
        data_validade.grid(row=3, column=0, sticky="w", padx=(190, 0), pady=(20, 5))

        self.validade_entry = ctk.CTkEntry(fundo_verde, placeholder_text=f"{self.formatar_data(self.get_informacao_aluno('atual_data_ficha'))}", width=180)
        self.validade_entry.grid(row=4, column=0, sticky="w", padx=(60, 0), pady=(10, 5))
        btn_abrir_calendario = ctk.CTkButton(fundo_verde, text="🗓️", text_color="#313131", font=("Arial", 16, 'bold'), fg_color="#7fd350", hover_color="#7fd350", width=5, command=partial(self.abrir_calendario, self.validade_entry, ano_inicial=self.obter_ano_atual()))
        btn_abrir_calendario.grid(row=4, column=0, sticky="w", padx=(245, 0), pady=(10, 5))

        # Caixa de Comentários
        comentarios_label = ctk.CTkLabel(fundo_verde, text="Comentários:", text_color="white", font=("Arial", 18, "bold"))
        comentarios_label.grid(row=6, column=0, sticky="w", padx=(20, 0), pady=(25, 5))

        self.comentarios_textbox = ctk.CTkTextbox(fundo_verde, width=900, height=200, corner_radius=10)
        self.comentarios_textbox.grid(row=7, column=0, padx=(60, 20), pady=(10, 5), sticky="w")
        if self.get_informacao_aluno("notas") == None:
            self.comentarios_textbox.insert(index="1.0", text="O Aluno ainda não possui anotações pessoais")
        else:
            self.comentarios_textbox.insert(index="1.0", text=self.get_informacao_aluno("notas"))

        # # Botão Salvar Alterações
        btn_salvar_alteracoes = ctk.CTkButton(fundo_verde, text="Salvar Alterações", fg_color="#808080", hover_color="#A9A9A9", command=self.salvar_comentarios_instrutor)
        btn_salvar_alteracoes.grid(row=8, column=0, columnspan=2, pady=(20, 10))

    def Gerenciamento(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="4 FITNESS", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario.lower().capitalize().lower().capitalize()}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")


        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\admin\\Alunos.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_gerenciar_aluno = ctk.CTkButton(central_frame, text="Gerenciar Alunos", fg_color="#808080", hover_color="#A9A9A9", command=self.tela_instrutor, font=("Arial", 18, "bold"), width=150, height=50)
        btn_gerenciar_aluno.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\admin\\Perfis.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_gerenciar_perfis = ctk.CTkButton(central_frame, text="Gerenciar Perfis", fg_color="#808080", hover_color="#A9A9A9", command=self.Exibir_perfis, font=("Arial", 18, "bold"), width=150, height=50)
        btn_gerenciar_perfis.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Home, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=20)

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)

    def Exibir_perfis(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criação do frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)
        
        # Configuração de colunas e linhas para centralizar
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0)  # Para centralizar verticalmente
        
        title = tk.Label(background_frame, text="Perfis dos Clientes", fg="white", bg="#313131", font=("Arial", 20))
        title.pack(pady=20)

        colunas = ("ID", "Nome", "Email", "Nome Instrutor")
        colunas = ("ID", "Nome", "Email", "Nome Instrutor")
        self.tree = ttk.Treeview(background_frame, columns=colunas, show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Nome Instrutor", text="Nome Do instrutor")
        self.tree.heading("Nome Instrutor", text="Nome Do instrutor")
        self.tree.pack(pady=0, fill=tk.BOTH, expand=True)
        self.carregar_perfis()

        ctk.CTkButton(background_frame, text="Deletar Perfil", command=self.deletar_perfil).pack(pady=10)
        ctk.CTkButton(background_frame, text="Voltar", command=self.Gerenciamento).pack(pady=10)
    
    def Feedback(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="4 FITNESS", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        log_out = ctk.CTkButton(frame_superior, text=" ⬅ Log Out", text_color="white", fg_color='#ED1B24', hover_color='#242424', font=("Arial", 14, 'bold'), height=20, command=self.realizar_login)
        log_out.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario.lower().capitalize()}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Adicionando a imagem
        image_path = "D:\\Users\\Aluno\\Documents\\Benedito-Dev\\Senac-UC5\\Projeto Academia\\img\\Logo.png"
        self.logo_image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))
        self.label_image = ctk.CTkLabel(background_frame, image=self.logo_image, text="")
        self.label_image.pack(pady=10)

        # Frame para o conteúdo central, usando .grid para os elementos abaixo
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131", bg_color="#313131")
        central_frame.pack(pady=(10, 20))

        # Elementos organizados com .grid
        title_feedback = ctk.CTkLabel(central_frame, text="Seu Feedback", text_color="white", fg_color="#313131", font=("Arial", 18, 'italic'))
        title_feedback.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        border_frame = ctk.CTkFrame(central_frame, fg_color="green", corner_radius=10)
        border_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(20, 10))

        self.feedback_text = ctk.CTkTextbox(border_frame, width=400, height=200, fg_color="#454545", text_color="white")
        self.feedback_text.pack(pady=10, padx=10)

        submit_button = ctk.CTkButton(central_frame, text="Enviar Feedback", fg_color="#808080", hover_color="#A9A9A9", command=self.submit_feedback)
        submit_button.grid(row=2, column=0, pady=20)

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Home, font=("Arial", 18))
        btn_voltar.grid(row=2, column=1, pady=20)

    def Ajustes(self):
        for widget in self.winfo_children():
            widget.destroy()

        backgorund_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        backgorund_frame.pack(fill="both", expand=True)
   
        backgorund_frame.grid_columnconfigure(0, weight=1)
        backgorund_frame.grid_columnconfigure(1, weight=1)
        backgorund_frame.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        backgorund_frame.grid_rowconfigure(6, weight=1) 
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        self.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # Frame para centralizar o conteúdo
        frame = tk.Frame(backgorund_frame, bg='#313131', highlightthickness=4, highlightbackground='#7fd350', highlightcolor='#7fd350')
        frame.grid(row=1, column=0, columnspan=2)

        # Título
        title = tk.Label(frame, text="Ajustes", fg="white", bg="#313131", font=('Arial', 20))
        title.grid(row=0, column=0, columnspan=5, pady=10)

        # Label Notificações
        notificacoes = ctk.CTkLabel(frame, text="Notificações :", text_color="white", font=('Arial', 14))
        notificacoes.grid(row=1, column=0, pady=10, padx=10)

        notificacoes = ["Exibir", "Não exibir"]

        notificaoes_selecionada = ctk.StringVar(value=notificacoes[0])

        optionmenu_notificacoes = ctk.CTkOptionMenu(frame, variable=notificaoes_selecionada, values=notificacoes, fg_color="#808080")
        optionmenu_notificacoes = ctk.CTkOptionMenu(frame, variable=notificaoes_selecionada, values=notificacoes, fg_color="#808080")
        optionmenu_notificacoes.grid(row=1, column=1, padx=10)

        # Label Idioma
        Idioma = ctk.CTkLabel(frame, text="Idioma : ", text_color="white", font=('Arial', 14))
        Idioma.grid(row=2, column=0, pady=10, padx=10)

        idiomas = ["Português-BR"]

        idioma_selecionado = ctk.StringVar(value=idiomas[0])

        optionmenu_idioma = ctk.CTkOptionMenu(frame,variable=idioma_selecionado,values=idiomas, fg_color="#808080")
        optionmenu_idioma = ctk.CTkOptionMenu(frame,variable=idioma_selecionado,values=idiomas, fg_color="#808080")
        optionmenu_idioma.grid(row=2, column=1, padx=10)   

        # Label Unidade de Medida
        und_medida = ctk.CTkLabel(frame, text="Unidade de Medida : ", text_color="white", font=('Arial', 14))
        und_medida.grid(row=3, column=0, pady=10, padx=10)

        unidades = ["KG", "LB"]

        unidade_selecionada = ctk.StringVar(value=unidades[0])
        
        optionmenu_unidade = ctk.CTkOptionMenu(frame,variable=unidade_selecionada,values=unidades, fg_color="#808080")
        optionmenu_unidade = ctk.CTkOptionMenu(frame,variable=unidade_selecionada,values=unidades, fg_color="#808080")
        optionmenu_unidade.grid(row=3, column=1, padx=10)

        # Label Frequência
        frequencia = ctk.CTkLabel(frame, text="Frequência de Treinos :", text_color="white", font=('Arial', 14))
        frequencia.grid(row=4, column=0, pady=10, padx=10)

        Frequencias = ["5 Dias na semana", "3 Dias na semana", "4 Dias na semana"]

        Frequencia_var = ctk.StringVar(value=Frequencias[0])  
        optionmenu_frequencia = ctk.CTkOptionMenu(frame,variable=Frequencia_var, values=Frequencias, fg_color="#808080")
        optionmenu_frequencia = ctk.CTkOptionMenu(frame,variable=Frequencia_var, values=Frequencias, fg_color="#808080")
        optionmenu_frequencia.grid(row=4, column=1, padx=10)

        # Label Meta
        meta = ctk.CTkLabel(frame, text="Meta :", text_color="white", font=('Arial', 14))
        meta.grid(row=5, column=0, pady=10, padx=10)

        Metas = ["Ganho de Massa", "Hipertrofia", "Perda de Peso"]

        Meta_var = ctk.StringVar(value=Metas[0])  
        optionmenu_meta = ctk.CTkOptionMenu(frame, variable=Meta_var, values=Metas, fg_color="#808080")
        optionmenu_meta = ctk.CTkOptionMenu(frame, variable=Meta_var, values=Metas, fg_color="#808080")
        optionmenu_meta.grid(row=5, column=1, padx=10)

        # Botão Cadastrar-se
        ctk.CTkButton(frame, text="Salvar Alterações",fg_color="#696767", hover_color="#A9A9A9", command=self.Home).grid(row=6, column=0, columnspan=5, pady=10, padx=20)
        ctk.CTkButton(frame, text="Salvar Alterações",fg_color="#696767", hover_color="#A9A9A9", command=self.Home).grid(row=6, column=0, columnspan=5, pady=10, padx=20)
        
        # Botão Voltar
        ctk.CTkButton(frame, text="Voltar", fg_color="#696767", hover_color="#A9A9A9", command=self.Home).grid(row=7, column=0, columnspan=5, pady=10)
        ctk.CTkButton(frame, text="Voltar", fg_color="#696767", hover_color="#A9A9A9", command=self.Home).grid(row=7, column=0, columnspan=5, pady=10)


    def Perfil_usuario(self):
        # Remove todos os widgets existentes
        for widget in self.winfo_children():
            widget.destroy()
        
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Configurações da janela para centralização
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_columnconfigure(1, weight=1)
        background_frame.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        background_frame.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior
        
        # Criando o frame verde
        frame_verde = ctk.CTkFrame(background_frame, fg_color="#313131", corner_radius=10, border_color="green", border_width=7)
        frame_verde.grid(row=1, column=0, columnspan=2, padx=40, pady=40)  # Aumentei o padding

        # Criando a fonte Nunito
        nunito_font = ("Nunito", 12)  # Fonte um pouco maior
        titulo_font = ("Nunito", 16, "bold")
        botao_font = ("Nunito", 12, "bold")

        # Label para o título
        titulo_label = ctk.CTkLabel(frame_verde, text="Editar Informações", text_color="White", font=titulo_font)
        titulo_label.grid(row=0, column=1, pady=15)  # Mais espaço vertical

        # Labels e entradas para nome
        self.entry_novo_nome = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font, placeholder_text=self.get_informacao("nome").lower().capitalize())
        label_nome = ctk.CTkLabel(frame_verde, text="Nome:", text_color="White", font=nunito_font)
        label_nome.grid(row=1, column=0, pady=10, sticky='e')  # Espaço vertical maior
        self.entry_novo_nome.grid(row=1, column=1, pady=10)

        # Labels e entradas para data de nascimento
        self.entry_dataDeNascimento = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font, placeholder_text=self.get_informacao("data_de_nascimento"))
        label_datanasc = ctk.CTkLabel(frame_verde, text="Data de nascimento:", text_color="White", font=nunito_font)
        label_datanasc.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.entry_dataDeNascimento.grid(row=2, column=1, pady=10)

        # Botão do calendário com cor preta
        self.btn_calendario = ctk.CTkButton(frame_verde, text="Escolher data", command=partial(self.abrir_calendario, self.entry_dataDeNascimento, ano_inicial=2005), fg_color="#000000", text_color="#ffffff")
        self.btn_calendario.grid(row=2, column=2, padx=10)  # Espaço lateral maior

        # Labels e entradas para endereço
        self.entry_novo_endereco = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font, placeholder_text=self.get_informacao("endereco"))
        label_endereco = ctk.CTkLabel(frame_verde, text="Endereço:", text_color="White", font=nunito_font)
        label_endereco.grid(row=3, column=0, pady=10, sticky='e')
        self.entry_novo_endereco.grid(row=3, column=1, pady=10)

        # Labels e entradas para telefone
        self.entry_novo_telefone = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font, placeholder_text=self.get_informacao("telefone"))
        label_telefone = ctk.CTkLabel(frame_verde, text="Telefone:", text_color="White", font=nunito_font)
        label_telefone.grid(row=4, column=0, pady=10, sticky='e')
        self.entry_novo_telefone.grid(row=4, column=1, pady=10)

        # Labels e entradas para email
        self.entry_novo_email = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font, placeholder_text=self.get_informacao("email"))
        label_email = ctk.CTkLabel(frame_verde, text="E-mail:", text_color="White", font=nunito_font)
        label_email.grid(row=5, column=0, pady=10, sticky='e')
        self.entry_novo_email.grid(row=5, column=1, pady=10)

        # Labels e entradas para nova senha
        label_nova_senha = ctk.CTkLabel(frame_verde, text="Nova senha:", text_color="White", font=nunito_font)
        label_nova_senha.grid(row=6, column=0, pady=10, sticky='e')
        self.entry_nova_senha = ctk.CTkEntry(frame_verde, fg_color="#ffffff", text_color="Black", font=nunito_font, show='*', placeholder_text="Nova Senha")
        self.entry_nova_senha.grid(row=6, column=1, pady=10)

        # Botão de cancelar
        self.btn_voltar = ctk.CTkButton(frame_verde, text="Cancelar", command=self.Home, fg_color="#000000", text_color="#FF0000")
        self.btn_voltar.grid(row=7, column=1, pady=15)

        # Botão de salvar alterações
        botao_salvar = ctk.CTkButton(frame_verde, text="Salvar alterações", fg_color="#000000", text_color="#00ff00", font=botao_font, command=self.validar_alteracoes)
        botao_salvar.grid(row=8, column=1, pady=15)