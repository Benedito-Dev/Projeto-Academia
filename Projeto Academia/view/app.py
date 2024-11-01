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
        
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)

        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0) 


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Logo.png"
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

        # Criação do frame de fundo
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)
        
        # Configuração de colunas e linhas para centralizar
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0)  # Para centralizar verticalmente
        
        # Imagem

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Logo.png"

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

        # Botão de criar conta
        ctk.CTkButton(frame, text="Cadastrar", font=("Arial", 18), width=160, fg_color="#808080",  hover_color="#A9A9A9", command=self.cadastrar_usuario).grid(row=5, column=0, columnspan=2, pady=10)

        # Botão de voltar
        ctk.CTkButton(frame, text="Voltar", font=("Arial", 18), width=160, fg_color="#808080", hover_color="#A9A9A9", command=self.menu_inicial).grid(row=6, column=0, columnspan=2, pady=10)


    def cadastrar_usuario(self):
        # Remove widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Configuração de colunas e linhas para centralizar
        background_frame.grid_columnconfigure(0, weight=1)
        background_frame.grid_rowconfigure(0, weight=0)  # Para centralizar verticalmente

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Logo.png"
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

        icon_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\icons\\halter.png"
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

        check_button_adm = ctk.CTkCheckBox(frame, text="Administrador", text_color="white")
        check_button_adm.grid(row=1, column=0, pady=5)  # Posicionando à esquerda

        check_button_aluno = ctk.CTkCheckBox(frame, text="Aluno", text_color="white")
        check_button_aluno.grid(row=1, column=1, pady=5)

        check_button_instrutor = ctk.CTkCheckBox(frame, text="Instrutor", text_color="white")
        check_button_instrutor.grid(row=1, column=2, pady=5)

        # Nome
        ctk.CTkLabel(frame, text="Nome:",text_color="white", font=("Arial", 14)).grid(row=2, column=0, sticky="e", padx=10)
        self.entry_nome = ctk.CTkEntry(frame)
        self.entry_nome.grid(row=2, column=1, pady=5)

        # Email
        ctk.CTkLabel(frame, text="Email:", text_color="white", font=("Arial", 14)).grid(row=3, column=0, sticky="e", padx=10)
        self.entry_email = ctk.CTkEntry(frame)
        self.entry_email.grid(row=3, column=1, pady=5)

        # Senha
        ctk.CTkLabel(frame, text="Senha:", text_color="white", font=("Arial", 14)).grid(row=4, column=0, sticky="e", padx=10)
        self.entry_senha = ctk.CTkEntry(frame, show="*")
        self.entry_senha.grid(row=4, column=1, pady=5)

        # Checkbutton para mostrar senha
        self.check_senha = ctk.IntVar()
        check_button = ctk.CTkCheckBox(frame, text="Mostrar senha", text_color="white", variable=self.check_senha, command=self.Exibir_senha)
        check_button.grid(row=5, column=1, sticky="w", padx=10)  # Posicionando à esquerda

        # Telefone
        ctk.CTkLabel(frame, text="Telefone:", text_color="white", font=("Arial", 14)).grid(row=6, column=0, sticky="e", padx=10)
        self.entry_telefone = ctk.CTkEntry(frame)
        self.entry_telefone.grid(row=6, column=1, pady=5)

        # Endereço
        ctk.CTkLabel(frame, text="Endereço:", text_color="white", font=("Arial", 14)).grid(row=7, column=0, sticky="e", padx=10)
        self.entry_endereco = ctk.CTkEntry(frame)
        self.entry_endereco.grid(row=7, column=1, pady=5)

        #CPF 
        ctk.CTkLabel(frame, text="CPF", text_color="white", font=("Arial", 14)).grid(row=8, column=0, sticky="e",padx=10)
        self.entry_cpf = ctk.CTkEntry(frame)
        self.entry_cpf.grid(row=8,column=1, pady=5)
        
        #Data de nascimento 
        ctk.CTkLabel(frame, text="Data de nascimento", text_color="white", font=("Arial", 14)).grid(row=9,column=0, sticky="e", padx=10)
        
        self.entry_dataDeNascimento = ctk.CTkEntry(frame)
        self.entry_dataDeNascimento.grid(row=9,column=1,pady=5)

        btn_abrir_calendario = ttk.Button(frame, text="Escolher data", command=self.abrir_calendario)
        btn_abrir_calendario.grid(row=9, column=2,padx=10)

        ctk.CTkLabel(frame, text="Cód.Funcionario", text_color="white", font=("Arial", 14)).grid(row=10, column=0, sticky="e", padx=10)

        self.entry_cod_funcionario = ctk.CTkEntry(frame)
        self.entry_cod_funcionario.grid(row=10, column=1, padx=10)

        

        # Botão Cadastrar-se
        ctk.CTkButton(frame,text="Cadastrar-se",fg_color="#609746", hover_color="#A9A9A9", command=self.validar_dados).grid(row=11,column=1,pady=10)

        # Botão Voltar
        ctk.CTkButton(frame, text="Voltar",fg_color="#808080", hover_color="#A9A9A9", command=self.realizar_login).grid(row=12, column=1,pady=10)

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

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Home\\Perfil.png"

        self.logo_image_perfil = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_perfil = ctk.CTkLabel(central_frame, image=self.logo_image_perfil, text="")
        self.label_image_perfil.grid(row=0, column=0, pady=0)

        # Colocando os botões lado a lado usando grid (CustomTkinter)
        btn_perfil = ctk.CTkButton(central_frame, text="Perfil", fg_color="#808080", hover_color="#A9A9A9", command=self.Perfil_usuario, font=("Arial", 18, "bold"), width=150, height=50)
        btn_perfil.grid(row=0, column=0, pady=(250, 00))


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Home\\Treinos.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=1, pady=0)

        if self.instrutor:
            btn_treinos = ctk.CTkButton(central_frame, text="Treinos", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos_instrutor, font=("Arial", 18, "bold"), width=150, height=50)
            btn_treinos.grid(row=0, column=1, pady=(250, 00))

        elif self.administrador:
            btn_treinos = ctk.CTkButton(central_frame, text="Gerenciamento da academia", fg_color="#808080", hover_color="#A9A9A9", font=("Arial", 18, "bold"), width=150, height=50)
            btn_treinos.grid(row=0, column=1, pady=(250, 00))

        else:
            btn_treinos = ctk.CTkButton(central_frame, text="Treinos", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos, font=("Arial", 18, "bold"), width=150, height=50)
            btn_treinos.grid(row=0, column=1, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Home\\Ajustes.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=2, pady=0)

        btn_ajustes = ctk.CTkButton(central_frame, text="Ajustes", fg_color="#808080", hover_color="#A9A9A9", command=self.Ajustes, font=("Arial", 18, "bold"), width=150, height=50)
        btn_ajustes.grid(row=0, column=2, pady=(250, 00))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


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

        alunos = ctk.CTkLabel(central_frame, text="👤 Alunos :", text_color="white", font=('Arial', 14))
        alunos.grid(row=1, column=0, pady=10, padx=10)

        alunos = self.obter_alunos_por_instrutor()

        self.aluno_selecionado = ctk.StringVar(value=alunos[0])

        optionmenu_alunos = ctk.CTkOptionMenu(central_frame, variable=self.aluno_selecionado, values=alunos)
        optionmenu_alunos.grid(row=1, column=1, padx=10)

        avancar_btn = ctk.CTkButton(central_frame, text="Avançar", text_color="white", fg_color="#808080", hover_color="#A9A9A9", command=self.Treinos)
        avancar_btn.grid(row=2, column=0, columnspan=2, pady=5)

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
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


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Menu-Treinos\\Puxador.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_superiores = ctk.CTkButton(central_frame, text="Superiores", fg_color="#808080", hover_color="#A9A9A9", command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_superiores.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Menu-Treinos\\Leg-press.png"

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

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Peito = ctk.CTkButton(central_frame, text="Peito", fg_color="#808080", hover_color="#A9A9A9", command=self.Peito, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Peito.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas.png"

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

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Perna.png"

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Perna.png"
        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Perna = ctk.CTkButton(central_frame, text="Perna", fg_color="#808080", hover_color="#A9A9A9", command=self.Perna, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Perna.grid(row=0, column=0, pady=(250, 00))


        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps.png"

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
        central_frame.pack(pady=20)

        # Dicionário com dados de cada página
        paginas = {
            1: {
                "titulo": "Treino de Peito e Ombros",
                "exercicios": [
                    {
                        "nome": "Supino reto com barra\n3x15 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\supino reto.jpg"
                    },
                    {
                        "nome": "Crucifixo inclinado\n3x15 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\crucifixo inclinado.jpg"
                    },
                    {
                        "nome": "Cruxifico no Crossover\n3x12 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\crossover-musculos-.jpg"
                    },
                                        {
                        "nome": "Elevação Lateral com Halteres\n3x12 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\elevacao_lateral.jpg"
                    },
                    {
                        "nome": "Desenvolvimento com Halteres\n3x12 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\desenvolvimento_halteres.jpg"
                    },
                    {
                        "nome": "Remada alta com barra\n3x12 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\remada_alta_barra.jpg"
                    }
                ]
            },
            2: {
                "titulo": "Treino de Tríceps",
                "exercicios": [
                    {
                        "nome": "Tríceps testa\n3x15 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\triceps_testa.png"
                    },
                    {
                        "nome": "Mergulho em bancos\n3x12 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\mergulho_bancos.jpg"
                    },
                    {
                        "nome": "Puxada de tríceps na polia\n3x15 reps",
                        "imagem": "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\triceps_polia.jfif"
                    }
                ]
            }
        }

        # Título da página
        label_titulo = ctk.CTkLabel(central_frame, text=paginas[pagina]["titulo"], text_color="white", font=("Arial", 22, 'bold'))
        label_titulo.grid(row=0, column=2, pady=20, padx=(0,0))

        # Mostrar exercícios da página atual
        total_exercicios = len(paginas[pagina]["exercicios"])
        for i, exercicio in enumerate(paginas[pagina]["exercicios"]):
            image_path = exercicio["imagem"]
            self.exercise_image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 150))

            # Definir a linha com base no índice
            coluna = i % 3 + 1  # 1 para os exercícios de peito e 2 para os de ombro
            linha = i // 3  # A mesma coluna para peito e ombro

            exercise_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
            exercise_frame.grid(row=linha+1, column=coluna, padx=20, pady=20)

            label_exercise_img = ctk.CTkLabel(exercise_frame, image=self.exercise_image, text="")
            label_exercise_img.pack()

            label_exercise_text = ctk.CTkLabel(exercise_frame, text=exercicio["nome"], text_color="white", font=("Arial", 16))
            label_exercise_text.pack()


        # Frame inferior com botões de navegação
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
        central_frame.pack(pady=20)

        # Título
        label_costas = ctk.CTkLabel(central_frame, text="Treino de Costas", text_color="white", font=("Arial", 22, 'bold'))
        label_costas.grid(row=2, column=0, columnspan=3, pady=10)

        # Exercício 1: Puxada alta
        puxada_alta_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\puxada.png" 
        self.puxada_alta_image = ctk.CTkImage(light_image=Image.open(puxada_alta_image_path), size=(150, 150))
        puxada_alta_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        puxada_alta_frame.grid(row=3, column=0, padx=20, pady=20)

        label_puxada_alta_img = ctk.CTkLabel(puxada_alta_frame, image=self.puxada_alta_image, text="")
        label_puxada_alta_img.pack()

        label_puxada_alta_text = ctk.CTkLabel(puxada_alta_frame, text="Puxada alta\n3x12 reps", text_color="white", font=("Arial", 16))
        label_puxada_alta_text.pack()

        # Exercício 2: Remada curvada
        remada_curvada_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\remada_curvada.jpg" 
        self.remada_curvada_image = ctk.CTkImage(light_image=Image.open(remada_curvada_image_path), size=(150, 150))
        remada_curvada_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        remada_curvada_frame.grid(row=3, column=1, padx=20, pady=20)

        label_remada_curvada_img = ctk.CTkLabel(remada_curvada_frame, image=self.remada_curvada_image, text="")
        label_remada_curvada_img.pack()

        label_remada_curvada_text = ctk.CTkLabel(remada_curvada_frame, text="Remada curvada\n3x12 reps", text_color="white", font=("Arial", 16))
        label_remada_curvada_text.pack()

        # Exercício 3: Levantamento terra
        levantamento_terra_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\levantamento_terra.jpg" 
        self.levantamento_terra_image = ctk.CTkImage(light_image=Image.open(levantamento_terra_image_path), size=(150, 150))
        levantamento_terra_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        levantamento_terra_frame.grid(row=3, column=2, padx=20, pady=20)

        label_levantamento_terra_img = ctk.CTkLabel(levantamento_terra_frame, image=self.levantamento_terra_image, text="")
        label_levantamento_terra_img.pack()

        label_levantamento_terra_text = ctk.CTkLabel(levantamento_terra_frame, text="Levantamento terra\n3x10 reps", text_color="white", font=("Arial", 16))
        label_levantamento_terra_text.pack()

        # Adicionando Treino de Bíceps
        label_biceps = ctk.CTkLabel(central_frame, text="Treino de Bíceps", text_color="white", font=("Arial", 22, 'bold'))
        label_biceps.grid(row=4, column=0, columnspan=3, pady=10)

        # Exercício 1: Rosca direta com barra
        rosca_direta_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_direta_barra.png"
        self.rosca_direta_image = ctk.CTkImage(light_image=Image.open(rosca_direta_image_path), size=(150, 150))
        rosca_direta_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_direta_frame.grid(row=5, column=0, padx=20, pady=20)

        label_rosca_direta_img = ctk.CTkLabel(rosca_direta_frame, image=self.rosca_direta_image, text="")
        label_rosca_direta_img.pack()

        label_rosca_direta_text = ctk.CTkLabel(rosca_direta_frame, text="Rosca direta com barra\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_direta_text.pack()

        # Exercício 2: Rosca martelo com halteres
        rosca_martelo_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_martelo.jfif"
        self.rosca_martelo_image = ctk.CTkImage(light_image=Image.open(rosca_martelo_image_path), size=(150, 150))
        rosca_martelo_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_martelo_frame.grid(row=5, column=1, padx=20, pady=20)

        label_rosca_martelo_img = ctk.CTkLabel(rosca_martelo_frame, image=self.rosca_martelo_image, text="")
        label_rosca_martelo_img.pack()

        label_rosca_martelo_text = ctk.CTkLabel(rosca_martelo_frame, text="Rosca martelo com halteres\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_martelo_text.pack()

        # Exercício 3: Rosca concentrada
        rosca_concentrada_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_concentrada.jfif"
        self.rosca_concentrada_image = ctk.CTkImage(light_image=Image.open(rosca_concentrada_image_path), size=(150, 150))
        rosca_concentrada_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_concentrada_frame.grid(row=5, column=2, padx=20, pady=20)

        label_rosca_concentrada_img = ctk.CTkLabel(rosca_concentrada_frame, image=self.rosca_concentrada_image, text="")
        label_rosca_concentrada_img.pack()

        label_rosca_concentrada_text = ctk.CTkLabel(rosca_concentrada_frame, text="Rosca concentrada\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_concentrada_text.pack()


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
        central_frame.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)  # Centralizando o frame

        # Título do treino
        label_pernas = ctk.CTkLabel(central_frame, text="Treino de Quadríceps", text_color="white", font=("Arial", 22, 'bold'))
        label_pernas.grid(row=0, column=0, columnspan=3, pady=10)

        # Exercício 1: Agachamento Smith
        agachamento_smith_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\agachamento_smith.gif"
        self.agachamento_smith_image = ctk.CTkImage(light_image=Image.open(agachamento_smith_image_path), size=(150, 150))
        agachamento_smith_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        agachamento_smith_frame.grid(row=1, column=0, padx=20, pady=20)

        label_agachamento_smith_img = ctk.CTkLabel(agachamento_smith_frame, image=self.agachamento_smith_image, text="")
        label_agachamento_smith_img.pack()

        label_agachamento_smith_text = ctk.CTkLabel(agachamento_smith_frame, text="Agachamento Smith \n3x12 reps", text_color="white", font=("Arial", 16))
        label_agachamento_smith_text.pack()

        # Exercício 2: Extensão de Pernas
        extensao_pernas_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\extensao_pernas.gif"
        self.extensao_pernas_image = ctk.CTkImage(light_image=Image.open(extensao_pernas_image_path), size=(150, 150))
        extensao_pernas_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30, width=200, height=200)
        extensao_pernas_frame.grid(row=1, column=1, padx=20, pady=20)

        label_extensao_pernas_img = ctk.CTkLabel(extensao_pernas_frame, image=self.extensao_pernas_image, text="")
        label_extensao_pernas_img.pack()

        label_extensao_pernas_text = ctk.CTkLabel(extensao_pernas_frame, text="Extensão de Pernas \n3x12 reps", text_color="white", font=("Arial", 16))
        label_extensao_pernas_text.pack()

        # Exercício 3: Leg Press
        leg_press_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\leg_press.gif"
        self.leg_press_image = ctk.CTkImage(light_image=Image.open(leg_press_image_path), size=(150, 150))
        leg_press_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        leg_press_frame.grid(row=1, column=2, padx=20, pady=20)

        label_leg_press_img = ctk.CTkLabel(leg_press_frame, image=self.leg_press_image, text="")
        label_leg_press_img.pack()

        label_leg_press_text = ctk.CTkLabel(leg_press_frame, text="Leg Press \n3x12 reps", text_color="white", font=("Arial", 16))
        label_leg_press_text.pack()

        # Exercício 4: Agachamento Frontal
        agachamento_frontal_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\agachamento_frontal.webp"
        self.agachamento_frontal_image = ctk.CTkImage(light_image=Image.open(agachamento_frontal_image_path), size=(150, 150))
        agachamento_frontal_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        agachamento_frontal_frame.grid(row=2, column=0, padx=20, pady=20)

        label_agachamento_frontal_img = ctk.CTkLabel(agachamento_frontal_frame, image=self.agachamento_frontal_image, text="")
        label_agachamento_frontal_img.pack()

        label_agachamento_frontal_text = ctk.CTkLabel(agachamento_frontal_frame, text="Agachamento Frontal \n3x10 reps", text_color="white", font=("Arial", 16))
        label_agachamento_frontal_text.pack()

        # Exercício 5: Avanço
        avancado_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\avanco.webp"
        self.avancado_image = ctk.CTkImage(light_image=Image.open(avancado_image_path), size=(150, 150))
        avancado_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        avancado_frame.grid(row=2, column=1, padx=20, pady=20)

        label_avancado_img = ctk.CTkLabel(avancado_frame, image=self.avancado_image, text="")
        label_avancado_img.pack()

        label_avancado_text = ctk.CTkLabel(avancado_frame, text="Avanço \n3x12 reps", text_color="white", font=("Arial", 16))
        label_avancado_text.pack()

        # Exercício 6: Step-Up
        step_up_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\step_up.webp"
        self.step_up_image = ctk.CTkImage(light_image=Image.open(step_up_image_path), size=(150, 150))
        step_up_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        step_up_frame.grid(row=2, column=2, padx=20, pady=20)

        label_step_up_img = ctk.CTkLabel(step_up_frame, image=self.step_up_image, text="")
        label_step_up_img.pack()

        label_step_up_text = ctk.CTkLabel(step_up_frame, text="Step-Up \n3x12 reps", text_color="white", font=("Arial", 16))
        label_step_up_text.pack()


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
        central_frame.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)  # Centralizando o frame

        # Título do treino
        label_pernas = ctk.CTkLabel(central_frame, text="Treino de Perna", text_color="white", font=("Arial", 22, 'bold'))
        label_pernas.grid(row=0, column=0, columnspan=3, pady=10)

        # Exercício 1: Stiff
        stiff_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\stiff.webp"
        self.stiff_image = ctk.CTkImage(light_image=Image.open(stiff_image_path), size=(150, 150))
        stiff_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        stiff_frame.grid(row=1, column=0, padx=20, pady=20)

        label_stiff_img = ctk.CTkLabel(stiff_frame, image=self.stiff_image, text="")
        label_stiff_img.pack()

        label_stiff_text = ctk.CTkLabel(stiff_frame, text="Stiff \n3x12 reps", text_color="white", font=("Arial", 16))
        label_stiff_text.pack()

        # Exercício 2: Afundo com Halteres
        afundo_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\afundo_halteres.gif"
        self.afundo_image = ctk.CTkImage(light_image=Image.open(afundo_image_path), size=(150, 150))
        afundo_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30, width=200, height=200)
        afundo_frame.grid(row=1, column=1, padx=20, pady=20)

        label_afundo_img = ctk.CTkLabel(afundo_frame, image=self.afundo_image, text="")
        label_afundo_img.pack()

        label_afundo_text = ctk.CTkLabel(afundo_frame, text="Afundo com Halteres\n3x12 reps", text_color="white", font=("Arial", 16))
        label_afundo_text.pack()

        # Exercício 3: Flexão de Pernas na Máquina
        pernas_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\pernas-na-maquina.webp"
        self.pernas_image = ctk.CTkImage(light_image=Image.open(pernas_image_path), size=(150, 150))
        pernas_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        pernas_frame.grid(row=1, column=2, padx=20, pady=20)

        label_pernas_img = ctk.CTkLabel(pernas_frame, image=self.pernas_image, text="")
        label_pernas_img.pack()

        label_pernas_text = ctk.CTkLabel(pernas_frame, text="Flexão de Pernas na Máquina \n3x15 reps", text_color="white", font=("Arial", 16))
        label_pernas_text.pack()

            # Exercício 4: Agachamento Sumô
        sumo_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\agachamento_sumo.webp"
        self.sumo_image = ctk.CTkImage(light_image=Image.open(sumo_image_path), size=(150, 150))
        sumo_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        sumo_frame.grid(row=2, column=0, padx=20, pady=20)

        label_sumo_img = ctk.CTkLabel(sumo_frame, image=self.sumo_image, text="")
        label_sumo_img.pack()

        label_sumo_text = ctk.CTkLabel(sumo_frame, text="Agachamento Sumô \n3x12 reps", text_color="white", font=("Arial", 16))
        label_sumo_text.pack()

        # Exercício 5: Levantamento de Quadril
        hip_thrust_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\levantamento_quadril.gif"
        self.hip_thrust_image = ctk.CTkImage(light_image=Image.open(hip_thrust_image_path), size=(150, 150))
        hip_thrust_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        hip_thrust_frame.grid(row=2, column=1, padx=20, pady=20)

        label_hip_thrust_img = ctk.CTkLabel(hip_thrust_frame, image=self.hip_thrust_image, text="")
        label_hip_thrust_img.pack()

        label_hip_thrust_text = ctk.CTkLabel(hip_thrust_frame, text="Levantamento de Quadril \n3x12 reps", text_color="white", font=("Arial", 16))
        label_hip_thrust_text.pack()

        # Exercício 6: Elevação de Panturrilha
        panturrilha_image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\elevacao_panturrilha.webp"
        self.panturrilha_image = ctk.CTkImage(light_image=Image.open(panturrilha_image_path), size=(150, 150))
        panturrilha_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        panturrilha_frame.grid(row=2, column=2, padx=20, pady=20)

        label_panturrilha_img = ctk.CTkLabel(panturrilha_frame, image=self.panturrilha_image, text="")
        label_panturrilha_img.pack()

        label_panturrilha_text = ctk.CTkLabel(panturrilha_frame, text="Elevação de Panturrilha \n3x15 reps", text_color="white", font=("Arial", 16))
        label_panturrilha_text.pack()

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
        botao_salvar.grid(row=8, column=1, pady=15)