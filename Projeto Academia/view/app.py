import tkinter as tk
from sqlalchemy import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageOps
from view.funcoes import Funções
from view.treinos_usuario_view import Treinos
from controller.controllers import UsuarioController

# Configurações do CustomTkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Application(tk.Tk, Funções, Treinos):
    def __init__(self):
        super().__init__()
        self.title("MultiForm")
        self.geometry("800x600")
        self.current_page = 0
        self.controler = UsuarioController()
        self.state('zoomed')
        self.menu_inicial()

# Janelas

    def menu_inicial(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.instrutor = False
        self.administrador = False
        
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)

        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0) 

        image_path = "Projeto Academia\\img\\Logo.png"
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
        ctk.CTkButton(frame, text="Login", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.realizar_login).grid(row=1, column=0, columnspan=2, pady=30, padx=60)

        ctk.CTkButton(frame, text="Gerenciar Perfis", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.Exibir_perfis).grid(row=2, column=0, columnspan=2, pady=30, padx=60)
        
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
        image_path = "Projeto Academia\\img\\Logo.png"
        self.logo_image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image = ctk.CTkLabel(background_frame, image=self.logo_image, text="")
        self.label_image.grid(row=1, column=0, pady=(60, 0))

        border_frame = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=10)
        border_frame.grid(row=2, column=0, padx=20, pady=20)

        # Frame para centralizar o conteúdo
        frame = ctk.CTkFrame(border_frame, fg_color="#313131", corner_radius=10)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Título
        titulo = ctk.CTkLabel(frame, text="Realizar login", text_color="white", font=("Arial", 20))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Nome do usuário
        nome_emoji = ctk.CTkLabel(frame, text="👤", text_color="white", font=("Arial", 16))
        nome_emoji.grid(row=1, column=0, padx=(10, 00))
        self.entry_nome = ctk.CTkEntry(frame, placeholder_text="Nome")
        self.entry_nome.grid(row=1, column=1, pady=5, padx=20)

        # Senha
        senha_emoji = ctk.CTkLabel(frame, text="🔒", text_color="white", font=("Arial", 16))
        senha_emoji.grid(row=2, column=0, padx=(10, 00))
        self.entry_senha = ctk.CTkEntry(frame, placeholder_text="Senha", show="*")
        self.entry_senha.grid(row=2, column=1, pady=5, padx=20)

        # Checkbutton para mostrar senha
        self.check_senha = ctk.IntVar()
        check = ctk.CTkCheckBox(frame, text="Mostrar senha", text_color="white", variable=self.check_senha, command=self.Exibir_senha)
        check.grid(row=3, column=1, columnspan=2, pady=5)

        # Botão de validar
        ctk.CTkButton(frame, text="Acessar", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.validando_login).grid(row=4, column=0, columnspan=2, pady=10)
        # Botão de voltar
        ctk.CTkButton(frame, text="Voltar", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.menu_inicial).grid(row=6, column=0, columnspan=2, pady=10)


    def Home(self):
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

        log_out = ctk.CTkButton(frame_superior, text=" ⬅ Log Out", text_color="white", fg_color='#ED1B24', hover_color='#242424', font=("Arial", 14, 'bold'), height=20, command=self.realizar_login)
        log_out.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        #Imagem Perfil

        image_path = "Projeto Academia\\img\\Home\\Perfil.png"

        self.logo_image_perfil = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_perfil = ctk.CTkLabel(central_frame, image=self.logo_image_perfil, text="")
        self.label_image_perfil.grid(row=0, column=0, pady=0)

        # Colocando os botões lado a lado usando grid (CustomTkinter)
        btn_perfil = ctk.CTkButton(central_frame, text="Perfil", fg_color="#808080", hover_color="#A9A9A9", command=self.tela_instrutor, font=("Arial", 18, "bold"), width=150, height=50)
        btn_perfil.grid(row=0, column=0, pady=(250, 00))


        if self.instrutor or self.administrador:
            # Botão de criar conta
            image_path = "Projeto Academia\\img\\Cadastrar\\btn_cadastrar.png"
            self.label_image_cadastrar = ctk.CTkImage(light_image=Image.open(image_path), size=(210, 198))
            self.label_image_cadastrar = ctk.CTkLabel(central_frame, image=self.label_image_cadastrar, text="")
            self.label_image_cadastrar.grid(row=0, column=3, pady=0)
            ctk.CTkButton(central_frame, text="Cadastrar", font=("Arial", 18), width=160, height=50, fg_color="#808080",  hover_color="#A9A9A9", command=self.cadastrar_cliente).grid(row=0, column=3, pady=(250, 00))
            # ctk.CTkButton(central_frame,text="Gerenciar aluno", font=("Arial", 18), width= 160, height=50, fg_color="#808080", hover_color="#A9A9A9", command=self.tela_instrutor).grid(row=0,colunm=4,pady=(250, 00))
        else:

            image_path = "Projeto Academia\\img\\Home\\Treinos.png"
            self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem
            self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
            self.label_image_treinos.grid(row=0, column=1, pady=0)
            btn_treinos = ctk.CTkButton(central_frame, text="Treinos", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
            btn_treinos.grid(row=0, column=1, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Home\\Ajustes.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=2, pady=0)

        btn_ajustes = ctk.CTkButton(central_frame, text="Ajustes", fg_color="#808080", hover_color="#A9A9A9", command=self.Ajustes, font=("Arial", 18, "bold"), width=150, height=50)
        btn_ajustes.grid(row=0, column=2, pady=(250, 00))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)

    def tela_instrutor(self):
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)

        fundo_verde = ctk.CTkFrame(background_frame,fg_color="#7fd350",corner_radius=20,width=1000,height=600)
        fundo_verde.pack(side="right", padx=(20,40),pady=(40))

        # btn_salvar_alterações = ctk.CTkButton(fundo_verde, text="Salvar alterações", fg_color="#808080", hover_color="#A9A9A9")
        # btn_salvar_alterações.grid(row=3, column=0)

        frame_esquerda = ctk.CTkFrame(background_frame, fg_color="#808080", corner_radius=10)
        frame_esquerda.pack(side="left", fill="y", expand=True, pady=20, padx=(0, 300))

        alunos = ["Aluno1", "Aluno2", "Aluno3"]

        nome_emoji = ctk.CTkLabel(frame_esquerda, text="👤", text_color="black", font=("Arial", 16))
        nome_emoji.grid(row=0, column=0, padx=(10, 0))
        menu_alunos = ctk.CTkOptionMenu(frame_esquerda, values=alunos, command=print(1))
        menu_alunos.grid(row=0, column=1, padx=(20, 10), pady=40)

        # acompanhamento_label = ctk.CTkLabel(fundo_verde, text="Acompanhamento", text_color="white", font=("Arial", 20))
        # acompanhamento_label.grid(row=0, column=0,pady=10)



    def cadastrar_cliente(self):
          # Remove widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Configuração de colunas e linhas para centralizar
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0)  # Para centralizar verticalmente

        image_path = "Projeto Academia\\img\\Logo.png"
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

        icon_path = "Projeto Academia\\img\\icons\\halter.png"
        icon = Image.open(icon_path)

        # Espelhe a imagem horizontalmente
        imagem_espelhada = ImageOps.mirror(icon)

        # Converta a imagem para um formato compatível com CustomTkinter
        imagem_ctk = ctk.CTkImage(imagem_espelhada, size=(30, 30))

        logo_image = ctk.CTkImage(light_image=Image.open(icon_path), size=(30, 30))  # Ajuste o tamanho da imagem

        # Halter
        label_image = ctk.CTkLabel(frame, image=logo_image, text="")
        label_image.grid(row=0, column=0, pady=10, padx=(90, 00))

        #halter Invertido
        label_image = ctk.CTkLabel(frame, image=imagem_ctk, text="")
        label_image.grid(row=0, column=2, pady=10, padx=(00, 100))

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
        btn_abrir_calendario = ctk.CTkButton(frame, text="🗓️", font=("Arial", 16, 'bold'), fg_color="#313131", hover_color="#313131", width=15, command=self.abrir_calendario)
        btn_abrir_calendario.grid(row=7, column=0, padx=(83, 0))
        self.entry_dataDeNascimento = ctk.CTkEntry(frame, placeholder_text="DD/MM/YYYY")
        self.entry_dataDeNascimento.grid(row=7, column=1, pady=5)

        btn_abrir_calendario = ctk.CTkButton(frame, text="Escolher data", command=self.abrir_calendario)
        btn_abrir_calendario.grid(row=7, column=2, padx=5)

        #Codigo Administrador
        codigo_emoji = ctk.CTkLabel(frame, text="🔑", text_color="white", font=("Arial", 16))
        codigo_emoji.grid(row=8, column=0, padx=(60, 00))
        self.entry_codigo_de_administrador = ctk.CTkEntry(frame, placeholder_text="Codigo de Admin")
        self.entry_codigo_de_administrador.grid(row=8, column=1, pady=5)

        self.tabela = ctk.StringVar(value="usuario")
        print(self.instrutor)
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
            Opção_1.grid(row=9, column=1, padx=(10, 10), pady=(10, 10))
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
            Opção_1.grid(row=9, column=0, padx=(10, 10), pady=(10, 10))     


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
            Opção_2.grid(row=9, column=1, padx=(10, 10), pady=(10, 10))

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
            Opção_3.grid(row=9, column=2, padx=(10, 10), pady=(10, 10))
        

        # Botão Cadastrar-se
        ctk.CTkButton(frame,text="Cadastrar-se",fg_color="#808080", hover_color="#A9A9A9", font=("Arial", 18), command=self.validar_dados).grid(row=10,column=1,pady=10)

        # Botão Voltar
        ctk.CTkButton(frame, text="Voltar",fg_color="#808080", hover_color="#A9A9A9", font=("Arial", 18), command=self.Home).grid(row=11, column=1,pady=10)

    def Treinos_instrutor(self):
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

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá Instrutor {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        #Imagem Perfil

        image_path = "Projeto Academia\\img\\Home\\Perfil.png"

        self.logo_image_perfil = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_perfil = ctk.CTkLabel(central_frame, image=self.logo_image_perfil, text="")
        self.label_image_perfil.grid(row=0, column=0, pady=0)

        # Colocando os botões lado a lado usando grid (CustomTkinter)
        btn_perfil = ctk.CTkButton(central_frame, text="Perfil", fg_color="#808080", hover_color="#A9A9A9", command=self.Perfil_usuario, font=("Arial", 18, "bold"), width=150, height=50)
        btn_perfil.grid(row=0, column=0, pady=(250, 00))


        image_path = "Projeto Academia\\img\\Home\\Treinos.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=1, pady=0)

        btn_treinos = ctk.CTkButton(central_frame, text="Treinos", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
        btn_treinos.grid(row=0, column=1, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Home\\Ajustes.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=2, pady=0)

        btn_ajustes = ctk.CTkButton(central_frame, text="Ajustes", fg_color="#808080", hover_color="#A9A9A9", command=self.Ajustes, font=("Arial", 18, "bold"), width=150, height=50)
        btn_ajustes.grid(row=0, column=2, pady=(250, 00))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)

    def Medidas(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.puxar_informacoes()

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

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá Instrutor {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Obter a lista de musculaturas do banco de dados
        lista_musculos = ['peso','altura','braco_direito','braco_esquerdo','peitoral','cintura','quadril','coxa_direita','coxa_esquerda','panturrilha_direita','panturrilha_esquerda']

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        Musculos = ctk.CTkLabel(central_frame, text="Músculos:", text_color="white", font=('Arial', 14))
        Musculos.grid(row=1, column=0, pady=10, padx=10)

        # Exibindo a lista de músculos no OptionMenu
        if lista_musculos:
            self.musculo_selecionado = ctk.StringVar(value=str(lista_musculos[0]))
            optionmenu_alunos = ctk.CTkOptionMenu(central_frame, variable=self.musculo_selecionado, values=[str(m) for m in lista_musculos])
            optionmenu_alunos.grid(row=1, column=1, padx=10)
            self.entry_musculo = ctk.CTkEntry(central_frame, placeholder_text="Medida do Musculo", text_color="white")
            self.entry_musculo.grid(row=1, column=2)

            def update_placeholder(*args):
                self.entry_musculo.configure(placeholder_text=self.get_informacao(self.musculo_selecionado.get()))

            # Conectando a função à StringVar para que seja chamada sempre que o valor mudar
            self.musculo_selecionado.trace_add("write", update_placeholder)
        else:
            vazio_label = ctk.CTkLabel(central_frame, text="Nenhuma musculatura encontrada", text_color="red", font=('Arial', 14))
            vazio_label.grid(row=1, column=1, padx=10)

        avancar_btn = ctk.CTkButton(
            central_frame,
            text="Avançar",
            text_color="white",
            fg_color="#808080",
            hover_color="#A9A9A9",
            command=lambda: self.enviar_medidas(self.musculo_selecionado.get()) # Chama ambas as funções
        )
        avancar_btn.grid(row=2, column=0, columnspan=2, pady=5)

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Treinos(self):
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

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame


        image_path = "Projeto Academia\\img\\Treinos\\Menu-Treinos\\Puxador.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_superiores = ctk.CTkButton(central_frame, text="Superiores", fg_color="#808080", hover_color="#A9A9A9", command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_superiores.grid(row=0, column=0, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Treinos\\Menu-Treinos\\Leg-press.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_inferiores = ctk.CTkButton(central_frame, text="Inferiores", fg_color="#808080", hover_color="#A9A9A9", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_inferiores.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Home, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Superiores(self):
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

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Peito.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Peito = ctk.CTkButton(central_frame, text="Peito", fg_color="#808080", hover_color="#A9A9A9", command=self.Peito, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Peito.grid(row=0, column=0, pady=(250, 00))

        image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Costas.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_Costas = ctk.CTkButton(central_frame, text="Costas", fg_color="#808080", hover_color="#A9A9A9", command=self.Costas, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Costas.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Inferiores(self):
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

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame

        image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Perna.png"

        image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Perna.png"
        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Perna = ctk.CTkButton(central_frame, text="Perna", fg_color="#808080", hover_color="#A9A9A9", command=self.Perna, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Perna.grid(row=0, column=0, pady=(250, 00))


        image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_quadriceps = ctk.CTkButton(central_frame, text="Quadríceps", fg_color="#808080", hover_color="#A9A9A9", command=self.Quadriceps, font=("Arial", 18, "bold"), width=150, height=50)
        btn_quadriceps.grid(row=0, column=1, pady=(250, 00))


        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)

        btn_voltar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Peito(self):
        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        # Frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame central
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.pack(pady=20, padx=20)  # Adicionando padding

        # Configurar pesos das colunas e linhas para centralização
        central_frame.grid_columnconfigure(0, weight=1)
        central_frame.grid_columnconfigure(1, weight=1)
        central_frame.grid_columnconfigure(2, weight=1)
        central_frame.grid_rowconfigure(1, weight=2)  # Se houver uma segunda linha para o carrossel

        # Exercícios de Peito para o carrossel
        exercicios_peito = [
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\supino reto.jpg", "nome": "Supino Reto", "series": 3, "repeticoes": 15},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\crucifixo inclinado.jpg", "nome": "Crucifixo Inclinado", "series": 3, "repeticoes": 15},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\crossover-musculos-.jpg", "nome": "Crossover", "series": 3, "repeticoes": 12}
        ]

        # Exercícios de Ombros para o carrossel
        exercicios_ombros = [
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\elevacao_lateral.jpg", "nome": "Elevação Lateral", "series": 3, "repeticoes": 12},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\desenvolvimento_halteres.jpg", "nome": "Desenvolvimento com Halteres", "series": 3, "repeticoes": 12},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\remada_alta_barra.jpg", "nome": "Remada Alta", "series": 3, "repeticoes": 12}
        ]

        # Exercícios de Triceps para o carrossel
        exercicios_triceps = [
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\mergulho_bancos.jpg", "nome": "Mergulho Bancos", "series": 3, "repeticoes": 15},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\triceps_polia.jfif", "nome": "triceps polia", "series": 3, "repeticoes": 15},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Peito\\triceps_testa.png", "nome": "triceps testa", "series": 3, "repeticoes": 12}
        ]

        # Inicializar o carrossel de imagens com título "Treino de Peito e Ombros"
        self.exercicios_atual = exercicios_peito
        self.indice_atual = 0
        self.iniciar_carrossel_imagens("Treino de Peito", central_frame, self.exercicios_atual, 200, 200)

        # Frame para botões de controle
        btn_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        btn_frame.pack(pady=30)

        # Botões para alternar os grupos de exercícios
        btn_peito = ctk.CTkButton(btn_frame, text="Peito", command=lambda: self.mudar_exercicios("Treino de Peito", exercicios_peito, central_frame), font=("Arial", 18, "bold"))
        btn_peito.pack(side="left", padx=5)

        btn_peito = ctk.CTkButton(btn_frame, text="Ombros", command=lambda: self.mudar_exercicios("Treino de Ombros", exercicios_ombros, central_frame), font=("Arial", 18, "bold"))
        btn_peito.pack(side="left", padx=5)

        btn_peito = ctk.CTkButton(btn_frame, text="Triceps", command=lambda: self.mudar_exercicios("Treino de Triceps", exercicios_triceps, central_frame), font=("Arial", 18, "bold"))
        btn_peito.pack(side="right", padx=5)

        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)


    def Costas(self):
        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        # Frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame central
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.pack(pady=20, padx=20)  # Adicionando padding

        # Configurar pesos das colunas e linhas para centralização
        central_frame.grid_columnconfigure(0, weight=1)
        central_frame.grid_columnconfigure(1, weight=1)
        central_frame.grid_columnconfigure(2, weight=1)
        central_frame.grid_rowconfigure(1, weight=2)  # Se houver uma segunda linha para o carrossel

        # Caminhos das imagens do treino
        exercicios_costas = [
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Costas\\puxada.png", "nome": "Puxada", "series": 3, "repeticoes": 12},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Costas\\remada_curvada.jpg", "nome": "Remada Curvada", "series": 3, "repeticoes": 10},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Costas\\levantamento_terra.jpg", "nome": "Levantamento Terra", "series": 4, "repeticoes": 8}
        ]

        exercicios_biceps = [
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_concentrada.jfif", "nome": "Rosca Concentrada", "series": 3, "repeticoes": 12},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_direta_barra.png", "nome": "Rosca Direta", "series": 3, "repeticoes": 10},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_martelo.jfif", "nome": "Rosca", "series": 4, "repeticoes": 8}
        ]

        # Inicializar o carrossel de imagens
        self.exercicios_atual = exercicios_costas
        self.indice_atual = 0
        self.iniciar_carrossel_imagens("Treino de Costas", central_frame, self.exercicios_atual, 200, 200)

        btn_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        btn_frame.pack(pady=30)

        # Botões para alternar entre os grupos de exercícios
        btn_costas = ctk.CTkButton(btn_frame, text="Costas", command=lambda: self.mudar_exercicios("Treino de Costas", exercicios_costas, central_frame), font=("Arial", 18, "bold"))
        btn_costas.pack(side="left", padx=5)

        btn_biceps = ctk.CTkButton(btn_frame, text="Bíceps", command=lambda: self.mudar_exercicios("Treino de Biceps", exercicios_biceps, central_frame), font=("Arial", 18, "bold"))
        btn_biceps.pack(side="right", padx=5)

        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)


    def Quadriceps(self):
        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        # Frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame central
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.pack(pady=20, padx=20)  # Adicionando padding

        # Configurar pesos das colunas e linhas para centralização
        central_frame.grid_columnconfigure(0, weight=1)
        central_frame.grid_columnconfigure(1, weight=1)
        central_frame.grid_columnconfigure(2, weight=1)
        central_frame.grid_rowconfigure(1, weight=2)  # Se houver uma segunda linha para o carrossel

        # Caminhos das imagens do treino
        exercicios_quadriceps = [
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\agachamento_frontal.webp", "nome": "Agachamento Frontal", "series": 3, "repeticoes": 12},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\agachamento_smith.gif", "nome": "Agachamento no Smith", "series": 3, "repeticoes": 10},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\avanco.webp", "nome": "Avanço", "series": 3, "repeticoes": 15},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\extensao_pernas.gif", "nome": "Extensão de Pernas", "series": 4, "repeticoes": 12},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\leg_press.gif", "nome": "Leg Press", "series": 4, "repeticoes": 10},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\step_up.webp", "nome": "Step Up", "series": 3, "repeticoes": 12}
        ]

        # Inicializar o carrossel de imagens
        self.exercicios_atual = exercicios_quadriceps
        self.indice_atual = 0
        self.iniciar_carrossel_imagens("Treino de Quadriceps", central_frame, self.exercicios_atual, 200, 200)

        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)


    def Perna(self):
        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        # Frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame central
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.pack(pady=20, padx=20)  # Adicionando padding

        # Configurar pesos das colunas e linhas para centralização
        central_frame.grid_columnconfigure(0, weight=1)
        central_frame.grid_columnconfigure(1, weight=1)
        central_frame.grid_columnconfigure(2, weight=1)
        central_frame.grid_rowconfigure(1, weight=2)  # Se houver uma segunda linha para o carrossel

        # Caminhos das imagens do treino
        exercicios_pernas = [
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\afundo_halteres.gif", "nome": "Afundo com Halteres", "series": 3, "repeticoes": 12},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\agachamento_sumo.webp", "nome": "Agachamento Sumo", "series": 3, "repeticoes": 10},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\elevacao_panturrilha.webp", "nome": "Elevação de Panturrilha", "series": 4, "repeticoes": 15},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\levantamento_quadril.gif", "nome": "Levantamento de Quadril", "series": 4, "repeticoes": 12},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\pernas-na-maquina.webp", "nome": "Pernas na Máquina", "series": 3, "repeticoes": 10},
            {"imagem": r"Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\stiff.webp", "nome": "Stiff", "series": 3, "repeticoes": 12}
        ]

        # Inicializar o carrossel de imagens
        self.exercicios_atual = exercicios_pernas
        self.indice_atual = 0
        self.iniciar_carrossel_imagens("Treino de Perna", central_frame, self.exercicios_atual, 200, 200)

        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)


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
        self.tree = ttk.Treeview(background_frame, columns=colunas, show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Nome Instrutor", text="Nome Instrutor")
        self.tree.pack(pady=0, fill=tk.BOTH, expand=True)
        self.carregar_perfis()

        ctk.CTkButton(background_frame, text="Deletar Perfil", command=self.deletar_perfil).pack(pady=10)
        ctk.CTkButton(background_frame, text="Voltar", command=self.menu_inicial).pack(pady=10)


    def Ajustes(self):
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)
   
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_columnconfigure(1, weight=1)
        background_frame.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        background_frame.grid_rowconfigure(6, weight=1) 
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        self.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # Frame para centralizar o conteúdo
        frame = tk.Frame(background_frame, bg='#313131', highlightthickness=4, highlightbackground='#7fd350', highlightcolor='#7fd350')
        frame.grid(row=1, column=0, columnspan=2)

        # Título
        title = tk.Label(frame, text="Ajustes", fg="white", bg="#313131", font=('Arial', 20))
        title.grid(row=0, column=0, columnspan=5, pady=10)

        # Label Notificações
        notificacoes = ctk.CTkLabel(frame, text="Notificações :", text_color="white", font=('Arial', 14))
        notificacoes.grid(row=1, column=0, pady=10, padx=10)

        notificacoes = ["Exibir", "Não exibir"]

        notificaoes_selecionada = ctk.StringVar(value=notificacoes[0])

        optionmenu_notificacoes = ctk.CTkOptionMenu(frame, variable=notificaoes_selecionada, values=notificacoes)
        optionmenu_notificacoes.grid(row=1, column=1, padx=10)

        # Label Idioma
        Idioma = ctk.CTkLabel(frame, text="Idioma : ", text_color="white", font=('Arial', 14))
        Idioma.grid(row=2, column=0, pady=10, padx=10)

        idiomas = ["Português-BR"]

        idioma_selecionado = ctk.StringVar(value=idiomas[0])

        optionmenu_idioma = ctk.CTkOptionMenu(frame,variable=idioma_selecionado,values=idiomas)
        optionmenu_idioma.grid(row=2, column=1, padx=10)   

        # Label Unidade de Medida
        und_medida = ctk.CTkLabel(frame, text="Unidade de Medida : ", text_color="white", font=('Arial', 14))
        und_medida.grid(row=3, column=0, pady=10, padx=10)

        unidades = ["KG", "LB"]

        unidade_selecionada = ctk.StringVar(value=unidades[0])
        
        optionmenu_unidade = ctk.CTkOptionMenu(frame,variable=unidade_selecionada,values=unidades)
        optionmenu_unidade.grid(row=3, column=1, padx=10)

        # Label Frequência
        frequencia = ctk.CTkLabel(frame, text="Frequência de Treinos :", text_color="white", font=('Arial', 14))
        frequencia.grid(row=4, column=0, pady=10, padx=10)

        Frequencias = ["5 Dias na semana", "3 Dias na semana", "4 Dias na semana"]

        Frequencia_var = ctk.StringVar(value=Frequencias[0])  
        optionmenu_frequencia = ctk.CTkOptionMenu(frame,variable=Frequencia_var, values=Frequencias)
        optionmenu_frequencia.grid(row=4, column=1, padx=10)

        # Label Meta
        meta = ctk.CTkLabel(frame, text="Meta :", text_color="white", font=('Arial', 14))
        meta.grid(row=5, column=0, pady=10, padx=10)

        Metas = ["Ganho de Massa", "Hipertrofia", "Perda de Peso"]

        Meta_var = ctk.StringVar(value=Metas[0])  
        optionmenu_meta = ctk.CTkOptionMenu(frame, variable=Meta_var, values=Metas)
        optionmenu_meta.grid(row=5, column=1, padx=10)

        # Botão Cadastrar-se
        ctk.CTkButton(frame, text="Salvar Alterações",fg_color="#696767", command=self.Home).grid(row=6, column=0, columnspan=5, pady=10, padx=20)
        
        # Botão Voltar
        ctk.CTkButton(frame, text="Voltar", fg_color="#696767",command=self.Home).grid(row=7, column=0, columnspan=5, pady=10)


    def Perfil_usuario(self):
        # Remove todos os widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        self.puxar_informacoes()
        
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Configurações da janela para centralização
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_columnconfigure(1, weight=1)
        background_frame.grid_rowconfigure(0, weight=1)  # Para centralizar verticalmente
        background_frame.grid_rowconfigure(6, weight=1)  # Espaço na parte inferior

        # frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        # frame_superior.pack(side="top", fill="x", pady=10)
        
        # Criando o frame verde
        frame_verde = ctk.CTkFrame(background_frame, fg_color="#313131", corner_radius=10, border_color="green", border_width=7)
        frame_verde.grid(row=1, column=0, columnspan=2, padx=40, pady=40)  # Aumentei o padding

        # frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        # frame_inferior.pack(side="bottom", fill="x", pady=10)

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
        self.btn_calendario = ctk.CTkButton(frame_verde, text="Escolher data", command=self.abrir_calendario, fg_color="#000000", text_color="#ffffff")
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
        botao_salvar.grid(row=9, column=1, pady=15)

        botao_medidas = ctk.CTkButton(frame_verde,text="Alterar medidas", command=self.Medidas, fg_color="#000000", text_color="#FF0000")
        botao_medidas.grid(row=8, column=1, pady=15)