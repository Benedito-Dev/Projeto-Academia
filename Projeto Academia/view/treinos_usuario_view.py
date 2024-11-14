from controller.controllers import UsuarioController
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from PIL import Image

class Treinos():
    def __init__(self):
        self.controler = UsuarioController()
    
    
    def Modalidades(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="MultiForm", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)  # Centralizando o frame


        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Menu-Treinos\\Artes Marciais.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_artesMarciais = ctk.CTkButton(central_frame, text="Artes Marciais", fg_color="#808080", hover_color="#A9A9A9", command=self.Artes_marciais, font=("Arial", 18, "bold"), width=150, height=50)
        btn_artesMarciais.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Menu-Treinos\\Musculação-Menu.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_musculação = ctk.CTkButton(central_frame, text="Musculação", fg_color="#808080", hover_color="#A9A9A9", command=self.Musculação, font=("Arial", 18, "bold"), width=150, height=50)
        btn_musculação.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Home, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)

    def Musculação(self):
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


        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Menu-Treinos\\Puxador.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_superiores = ctk.CTkButton(central_frame, text="Superiores", fg_color="#808080", hover_color="#A9A9A9", command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_superiores.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Menu-Treinos\\Leg-press.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_inferiores = ctk.CTkButton(central_frame, text="Inferiores", fg_color="#808080", hover_color="#A9A9A9", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_inferiores.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Modalidades, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=20)

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)

    def Artes_marciais(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="MultiForm", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Menu-Treinos\\Karate.png"

        logo_image_karate = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        label_image_karate = ctk.CTkLabel(central_frame, image=logo_image_karate, text="", height=200)
        label_image_karate.grid(row=0, column=0)

        btn_karate = ctk.CTkButton(central_frame, text="Karate", fg_color="#808080", hover_color="#A9A9A9", command=self.Karate, font=("Arial", 18, "bold"), width=150, height=50)
        btn_karate.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Menu-Treinos\\muaythai_menu.png"
        logo_image_muaythai = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))
        label_image_karate = ctk.CTkLabel(central_frame, image=logo_image_muaythai, text="", height=200)
        label_image_karate.grid(row=0, column=1)

        btn_MuayThai = ctk.CTkButton(central_frame, text="Muay Thai", fg_color="#808080", hover_color="#A9A9A9", command=self.MuayThai, font=("Arial", 18, "bold"), width=150, height=50)
        btn_MuayThai.grid(row=0, column=1, pady=(250, 00))


        btn_JiuJitsu = ctk.CTkButton(central_frame, text="Jiu-Jitsu", fg_color="#808080", hover_color="#A9A9A9", command=self.JiuJitsu, font=("Arial", 18, "bold"), width=150, height=50)
        btn_JiuJitsu.grid(row=0, column=2, pady=(250, 00))

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Modalidades, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)

    def MuayThai(self):
        for widget in self.winfo_children():
            widget.destroy()
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="MultiForm", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

        label_numero = ctk.CTkLabel(central_frame, text="#AAA", text_color="green", font=("Arial", 24))
        label_numero.grid(row=0, column=0, pady=0)

        label_text = ctk.CTkLabel(central_frame, text="", font=("Arial", 14, 'bold'))
        label_text.grid(row=1, column=0, pady=5)

        # Cria um botão que gera e exibe o número diretamente ao ser clicado
        botao_gerar = ctk.CTkButton(
            central_frame, 
            text="Gerar Código Experimental", 
            command=lambda: [
                label_numero.configure(text=f"#{self.gerar_codigo()}"), 
                label_text.configure(text="Apresente este código ao nosso instrutor Wilkson")
            ]
        )
        botao_gerar.grid(row=2, column=0, pady=20)

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Artes_marciais, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)



    def Karate(self):
        for widget in self.winfo_children():
            widget.destroy()

         # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="MultiForm", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#7fd350", font=("Arial", 18, 'bold'))
        plano_label.pack(side="top")

        # Frame central para os botões (usando CustomTkinter)
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

        label_numero = ctk.CTkLabel(central_frame, text="#AAA", text_color="green", font=("Arial", 24))
        label_numero.grid(row=0, column=0, pady=0)

        label_text = ctk.CTkLabel(central_frame, text="", font=("Arial", 14, 'bold'))
        label_text.grid(row=1, column=0, pady=5)

        # Cria um botão que gera e exibe o número diretamente ao ser clicado
        botao_gerar = ctk.CTkButton(
            central_frame, 
            text="Gerar Código Experimental", 
            command=lambda: [
                label_numero.configure(text=f"#{self.gerar_codigo()}"), 
                label_text.configure(text="Apresente este código ao nosso instrutor Wilkson")
            ]
        )
        botao_gerar.grid(row=2, column=0, pady=20)

        # Frame inferior (usando CustomTkinter)
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Artes_marciais, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)
 
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

        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito.png"

        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Peito = ctk.CTkButton(central_frame, text="Peito", fg_color="#808080", hover_color="#A9A9A9", command=self.Peito, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Peito.grid(row=0, column=0, pady=(250, 00))

        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_Costas = ctk.CTkButton(central_frame, text="Costas", fg_color="#808080", hover_color="#A9A9A9", command=self.Costas, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Costas.grid(row=0, column=1, pady=(250, 00))

        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Musculação, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=20)

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

        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Perna.png"

        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Perna.png"
        self.logo_image_treinos = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_treinos = ctk.CTkLabel(central_frame, image=self.logo_image_treinos, text="")
        self.label_image_treinos.grid(row=0, column=0, pady=0)

        btn_Perna = ctk.CTkButton(central_frame, text="Perna", fg_color="#808080", hover_color="#A9A9A9", command=self.Perna, font=("Arial", 18, "bold"), width=150, height=50)
        btn_Perna.grid(row=0, column=0, pady=(250, 00))


        image_path = "D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps.png"

        self.logo_image_ajustes = ctk.CTkImage(light_image=Image.open(image_path), size=(350, 350))  # Ajuste o tamanho da imagem

        # Criar um Label para exibir a imagem
        self.label_image_ajustes = ctk.CTkLabel(central_frame, image=self.logo_image_ajustes, text="")
        self.label_image_ajustes.grid(row=0, column=1, pady=0)

        btn_quadriceps = ctk.CTkButton(central_frame, text="Quadríceps", fg_color="#808080", hover_color="#A9A9A9", command=self.Quadriceps, font=("Arial", 18, "bold"), width=150, height=50)
        btn_quadriceps.grid(row=0, column=1, pady=(250, 00))


        btn_voltar = ctk.CTkButton(central_frame, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Musculação, font=("Arial", 18, "bold"), width=150, height=50)

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
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\supino reto.gif", "nome": "Supino Reto", "series": 3, "repeticoes": 15},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\crucifixo inclinado.gif", "nome": "Crucifixo Inclinado", "series": 3, "repeticoes": 15},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\crossover-musculos.gif", "nome": "Crossover", "series": 3, "repeticoes": 12}
        ]

        # Exercícios de Ombros para o carrossel
        exercicios_ombros = [
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\elevacao_lateral.gif", "nome": "Elevação Lateral", "series": 3, "repeticoes": 12},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\desenvolvimento_halteres.gif", "nome": "Desenvolvimento com Halteres", "series": 3, "repeticoes": 12},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\remada_alta_barra.gif", "nome": "Remada Alta", "series": 3, "repeticoes": 12}
        ]

        # Exercícios de Triceps para o carrossel
        exercicios_triceps = [
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\mergulho_bancos.gif", "nome": "Mergulho Banco", "series": 3, "repeticoes": 15},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\triceps_polia.gif", "nome": "Tríceps Polia", "series": 3, "repeticoes": 15},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Peito\\triceps_testa.gif", "nome": "Tríceps Testa", "series": 3, "repeticoes": 12}
        ]

        # Inicializar o carrossel de imagens com título "Treino de Peito e Ombros"
        self.exercicios_atual = exercicios_peito
        self.indice_atual = 0
        self.iniciar_carrossel_imagens("Treino de Peito", central_frame, self.exercicios_atual, 200, 200)

        # Frame para botões de controle
        btn_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        btn_frame.pack(pady=30)

        # Botões para alternar os grupos de exercícios
        btn_peito = ctk.CTkButton(btn_frame, text="Peito", fg_color="#808080", hover_color="#A9A9A9", command=lambda: self.mudar_exercicios("Treino de Peito", exercicios_peito, central_frame), font=("Arial", 18, "bold"))
        btn_peito.pack(side="left", padx=5)

        btn_peito = ctk.CTkButton(btn_frame, text="Ombros", fg_color="#808080", hover_color="#A9A9A9", command=lambda: self.mudar_exercicios("Treino de Ombros", exercicios_ombros, central_frame), font=("Arial", 18, "bold"))
        btn_peito.pack(side="left", padx=5)

        btn_peito = ctk.CTkButton(btn_frame, text="Triceps", fg_color="#808080", hover_color="#A9A9A9", command=lambda: self.mudar_exercicios("Treino de Triceps", exercicios_triceps, central_frame), font=("Arial", 18, "bold"))
        btn_peito.pack(side="right", padx=5)



    # Novo frame para o botão "Finalizar treino" abaixo dos botões de controle
        finalizar_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        finalizar_frame.pack(pady=10)

        def concluir_treino():
            messagebox.showinfo(" ", "De hoje tá pago!🦾")
            self.Superiores()

        # Botão Finalizar treino
        btn_finalizar = ctk.CTkButton(finalizar_frame, text="Finalizar treino", fg_color="#32CD32", hover_color="#228B22", command=concluir_treino, font=("Arial", 18, "bold"), width=150, height=50)
        btn_finalizar.pack()

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
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\puxada.gif", "nome": "Puxada", "series": 3, "repeticoes": 12},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\remada_curvada.gif", "nome": "Remada Curvada", "series": 3, "repeticoes": 10},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\levantamento_terra.gif", "nome": "Levantamento Terra", "series": 4, "repeticoes": 8}
        ]

        exercicios_biceps = [
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_concentrada.gif", "nome": "Rosca Concentrada", "series": 3, "repeticoes": 12},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_direta_barra.gif", "nome": "Rosca Direta", "series": 3, "repeticoes": 10},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_martelo.gif", "nome": "Rosca Martelo", "series": 4, "repeticoes": 8}
        ]

        # Inicializar o carrossel de imagens
        self.exercicios_atual = exercicios_costas
        self.indice_atual = 0
        self.iniciar_carrossel_imagens("Treino de Costas", central_frame, self.exercicios_atual, 200, 200)


        btn_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        btn_frame.pack(pady=30)

        # Botões para alternar entre os grupos de exercícios
        btn_costas = ctk.CTkButton(btn_frame, text="Costas", fg_color="#808080", hover_color="#A9A9A9", command=lambda: self.mudar_exercicios("Treino de Costas", exercicios_costas, central_frame), font=("Arial", 18, "bold"))
        btn_costas.pack(side="left", padx=5)

        btn_biceps = ctk.CTkButton(btn_frame, text="Bíceps", fg_color="#808080", hover_color="#A9A9A9", command=lambda: self.mudar_exercicios("Treino de Biceps", exercicios_biceps, central_frame), font=("Arial", 18, "bold"))
        btn_biceps.pack(side="right", padx=5)

       # Novo frame para o botão "Finalizar treino" abaixo dos botões de controle
        finalizar_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        finalizar_frame.pack(pady=10)

        def concluir_treino():
            messagebox.showinfo(" ", "De hoje tá pago!🦾")
            self.Superiores()

        # Botão Finalizar treino
        btn_finalizar = ctk.CTkButton(finalizar_frame, text="Finalizar treino", fg_color="#32CD32", hover_color="#228B22", command=concluir_treino, font=("Arial", 18, "bold"), width=150, height=50)
        btn_finalizar.pack()

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
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\agachamento_frontal.gif", "nome": "Agachamento Frontal", "series": 3, "repeticoes": 12},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\agachamento_smith.gif", "nome": "Agachamento no Smith", "series": 3, "repeticoes": 10},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\avanco.gif", "nome": "Avanço", "series": 3, "repeticoes": 15},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\extensao_pernas.gif", "nome": "Extensão de Pernas", "series": 4, "repeticoes": 12},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\leg_press.gif", "nome": "Leg Press", "series": 4, "repeticoes": 10},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\step_up.gif", "nome": "Step Up", "series": 3, "repeticoes": 12}
        ]

        # Inicializar o carrossel de imagens
        self.exercicios_atual = exercicios_quadriceps
        self.indice_atual = 0
        self.iniciar_carrossel_imagens("Treino de Quadriceps", central_frame, self.exercicios_atual, 200, 200)

        # Função para exibir a mensagem de conclusão
        def concluir_treino():
            messagebox.showinfo(" ", "De hoje tá pago!🦾")
            self.Inferiores()

        # Botão Finalizar treino, abaixo da imagem no mesmo frame
        btn_finalizar = ctk.CTkButton(central_frame, text="Finalizar treino", fg_color="#32CD32", hover_color="#228B22", command=concluir_treino, font=("Arial", 18, "bold"), width=150, height=50)
        btn_finalizar.grid(column= 1, columnspan= 2, padx=(0,150), pady=30)

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
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\afundo_halteres.gif", "nome": "Afundo com Halteres", "series": 3, "repeticoes": 12},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\agachamento_sumo.gif", "nome": "Agachamento Sumô", "series": 3, "repeticoes": 10},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\levantamento_quadril.gif", "nome": "Levantamento de Quadril", "series": 4, "repeticoes": 12},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\pernas-na-maquina.gif", "nome": "Pernas na Máquina", "series": 3, "repeticoes": 10},
            {"imagem": r"D:\\Users\\Aluno\\Documents\GUILPROGIT\\Projeto-Academia\\Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\stiff.gif", "nome": "Stiff", "series": 3, "repeticoes": 12}
        ]

        # Inicializar o carrossel de imagens
        self.exercicios_atual = exercicios_pernas
        self.indice_atual = 0
        self.iniciar_carrossel_imagens("Treino de Perna", central_frame, self.exercicios_atual, 200, 200)

        # Função para exibir a mensagem de conclusão
        def concluir_treino():
            messagebox.showinfo(" ", "De hoje tá pago!🦾")
            self.Inferiores()

        # Botão Finalizar treino, abaixo da imagem no mesmo frame
        btn_finalizar = ctk.CTkButton(central_frame, text="Finalizar treino", fg_color="#32CD32", hover_color="#228B22", command=concluir_treino, font=("Arial", 18, "bold"), width=150, height=50)
        btn_finalizar.grid(column= 1, columnspan= 2, padx=(0,150), pady=30)

        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#7fd350", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)