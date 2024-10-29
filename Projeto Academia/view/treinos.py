import tkinter as tk
import customtkinter as ctk
from sqlalchemy import *
from sqlalchemy.exc import SQLAlchemyError
from view.funcoes import Funções
from controller.controllers import UsuarioController
from PIL import Image, ImageTk

class Treinos(ctk.CTk, Funções):
    def __init__(self):
        super().__init__()

    
    def Treinos(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="MultiForm", text_color="white", fg_color="#5ce1e6", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#5ce1e6", font=("Arial", 18, 'bold'))
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
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Superiores(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="MultiForm", text_color="white", fg_color="#5ce1e6", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#5ce1e6", font=("Arial", 18, 'bold'))
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
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Inferiores(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Criando Fundo com CustomTkinter
        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame superior com o título e plano (usando CustomTkinter)
        frame_superior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0, height=30)
        frame_superior.pack(side="top", fill="x", pady=10)

        title = ctk.CTkLabel(frame_superior, text="MultiForm", text_color="white", fg_color="#5ce1e6", font=("Arial", 18, 'bold'))
        title.pack(side="left", padx=20)

        home_button = ctk.CTkButton(frame_superior, text="🏠 Home", font=("Arial", 14, 'bold'), text_color="white", height=20 ,command=self.Home)
        home_button.pack(side="right", padx=10)

        plano_label = ctk.CTkLabel(frame_superior, text=f"Plano Intermediário, Olá {self.nome_usuario}", text_color="white", fg_color="#5ce1e6", font=("Arial", 18, 'bold'))
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
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0,height=30)
        frame_inferior.pack(side="bottom", fill="x", pady=10)


    def Peito(self, pagina=1):
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
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\supino reto.jpg"
                    },
                    {
                        "nome": "Crucifixo inclinado\n3x15 reps",
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\crucifixo inclinado.jpg"
                    },
                    {
                        "nome": "Cruxifico no Crossover\n3x12 reps",
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\crossover-musculos-.jpg"
                    },
                                        {
                        "nome": "Elevação Lateral com Halteres\n3x12 reps",
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\elevacao_lateral.jpg"
                    },
                    {
                        "nome": "Desenvolvimento com Halteres\n3x12 reps",
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\desenvolvimento_halteres.jpg"
                    },
                    {
                        "nome": "Remada alta com barra\n3x12 reps",
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\remada_alta_barra.jpg"
                    }
                ]
            },
            2: {
                "titulo": "Treino de Tríceps",
                "exercicios": [
                    {
                        "nome": "Tríceps testa\n3x15 reps",
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\triceps_testa.png"
                    },
                    {
                        "nome": "Mergulho em bancos\n3x12 reps",
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\mergulho_bancos.jpg"
                    },
                    {
                        "nome": "Puxada de tríceps na polia\n3x15 reps",
                        "imagem": "Projeto Academia\\img\\\\Treinos\\Superiores\\Peito\\triceps_polia.jfif"
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
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")


        # Botões de navegação entre páginas
        if pagina > 1:
            btn_anterior = ctk.CTkButton(frame_inferior, text="Anterior", fg_color="#808080", hover_color="#A9A9A9",
                                        command=lambda: self.Peito(pagina-1), font=("Arial", 18, "bold"), width=150, height=50)
            btn_anterior.pack(side='left', padx=(10, 0), pady=10)

        if pagina < len(paginas):
            btn_proxima = ctk.CTkButton(frame_inferior, text="Próxima", fg_color="#808080", hover_color="#A9A9A9",
                                        command=lambda: self.Peito(pagina+1), font=("Arial", 18, "bold"), width=150, height=50)
            btn_proxima.pack(side='right', padx=(0, 10), pady=10)

        # Botão Voltar para Superiores
        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9",
                                command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.place(relx=0.5, rely=0.5, anchor="center")


    def Costas(self):

        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.pack(pady=20)

        # Título
        label_costas = ctk.CTkLabel(central_frame, text="Treino de Costas", text_color="white", font=("Arial", 22, 'bold'))
        label_costas.grid(row=2, column=0, columnspan=3, pady=10)

        # Exercício 1: Puxada alta
        puxada_alta_image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Costas\\puxada.png" 
        self.puxada_alta_image = ctk.CTkImage(light_image=Image.open(puxada_alta_image_path), size=(150, 150))
        puxada_alta_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        puxada_alta_frame.grid(row=3, column=0, padx=20, pady=20)

        label_puxada_alta_img = ctk.CTkLabel(puxada_alta_frame, image=self.puxada_alta_image, text="")
        label_puxada_alta_img.pack()

        label_puxada_alta_text = ctk.CTkLabel(puxada_alta_frame, text="Puxada alta\n3x12 reps", text_color="white", font=("Arial", 16))
        label_puxada_alta_text.pack()

        # Exercício 2: Remada curvada
        remada_curvada_image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Costas\\remada_curvada.jpg" 
        self.remada_curvada_image = ctk.CTkImage(light_image=Image.open(remada_curvada_image_path), size=(150, 150))
        remada_curvada_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        remada_curvada_frame.grid(row=3, column=1, padx=20, pady=20)

        label_remada_curvada_img = ctk.CTkLabel(remada_curvada_frame, image=self.remada_curvada_image, text="")
        label_remada_curvada_img.pack()

        label_remada_curvada_text = ctk.CTkLabel(remada_curvada_frame, text="Remada curvada\n3x12 reps", text_color="white", font=("Arial", 16))
        label_remada_curvada_text.pack()

        # Exercício 3: Levantamento terra
        levantamento_terra_image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Costas\\levantamento_terra.jpg" 
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
        rosca_direta_image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_direta_barra.png"
        self.rosca_direta_image = ctk.CTkImage(light_image=Image.open(rosca_direta_image_path), size=(150, 150))
        rosca_direta_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_direta_frame.grid(row=5, column=0, padx=20, pady=20)

        label_rosca_direta_img = ctk.CTkLabel(rosca_direta_frame, image=self.rosca_direta_image, text="")
        label_rosca_direta_img.pack()

        label_rosca_direta_text = ctk.CTkLabel(rosca_direta_frame, text="Rosca direta com barra\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_direta_text.pack()

        # Exercício 2: Rosca martelo com halteres
        rosca_martelo_image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_martelo.jfif"
        self.rosca_martelo_image = ctk.CTkImage(light_image=Image.open(rosca_martelo_image_path), size=(150, 150))
        rosca_martelo_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_martelo_frame.grid(row=5, column=1, padx=20, pady=20)

        label_rosca_martelo_img = ctk.CTkLabel(rosca_martelo_frame, image=self.rosca_martelo_image, text="")
        label_rosca_martelo_img.pack()

        label_rosca_martelo_text = ctk.CTkLabel(rosca_martelo_frame, text="Rosca martelo com halteres\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_martelo_text.pack()

        # Exercício 3: Rosca concentrada
        rosca_concentrada_image_path = "Projeto Academia\\img\\Treinos\\Superiores\\Costas\\rosca_concentrada.jfif"
        self.rosca_concentrada_image = ctk.CTkImage(light_image=Image.open(rosca_concentrada_image_path), size=(150, 150))
        rosca_concentrada_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        rosca_concentrada_frame.grid(row=5, column=2, padx=20, pady=20)

        label_rosca_concentrada_img = ctk.CTkLabel(rosca_concentrada_frame, image=self.rosca_concentrada_image, text="")
        label_rosca_concentrada_img.pack()

        label_rosca_concentrada_text = ctk.CTkLabel(rosca_concentrada_frame, text="Rosca concentrada\n3x12 reps", text_color="white", font=("Arial", 16))
        label_rosca_concentrada_text.pack()


        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Superiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)


    def Quadriceps(self):
        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame central para os exercícios, centralizado
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)  # Centralizando o frame

        # Título do treino
        label_pernas = ctk.CTkLabel(central_frame, text="Treino de Quadríceps", text_color="white", font=("Arial", 22, 'bold'))
        label_pernas.grid(row=0, column=0, columnspan=3, pady=10)

        # Exercício 1: Agachamento Smith
        agachamento_smith_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\agachamento_smith.gif"
        self.agachamento_smith_image = ctk.CTkImage(light_image=Image.open(agachamento_smith_image_path), size=(150, 150))
        agachamento_smith_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        agachamento_smith_frame.grid(row=1, column=0, padx=20, pady=20)

        label_agachamento_smith_img = ctk.CTkLabel(agachamento_smith_frame, image=self.agachamento_smith_image, text="")
        label_agachamento_smith_img.pack()

        label_agachamento_smith_text = ctk.CTkLabel(agachamento_smith_frame, text="Agachamento Smith \n3x12 reps", text_color="white", font=("Arial", 16))
        label_agachamento_smith_text.pack()

        # Exercício 2: Extensão de Pernas
        extensao_pernas_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\extensao_pernas.gif"
        self.extensao_pernas_image = ctk.CTkImage(light_image=Image.open(extensao_pernas_image_path), size=(150, 150))
        extensao_pernas_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30, width=200, height=200)
        extensao_pernas_frame.grid(row=1, column=1, padx=20, pady=20)

        label_extensao_pernas_img = ctk.CTkLabel(extensao_pernas_frame, image=self.extensao_pernas_image, text="")
        label_extensao_pernas_img.pack()

        label_extensao_pernas_text = ctk.CTkLabel(extensao_pernas_frame, text="Extensão de Pernas \n3x12 reps", text_color="white", font=("Arial", 16))
        label_extensao_pernas_text.pack()

        # Exercício 3: Leg Press
        leg_press_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\leg_press.gif"
        self.leg_press_image = ctk.CTkImage(light_image=Image.open(leg_press_image_path), size=(150, 150))
        leg_press_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        leg_press_frame.grid(row=1, column=2, padx=20, pady=20)

        label_leg_press_img = ctk.CTkLabel(leg_press_frame, image=self.leg_press_image, text="")
        label_leg_press_img.pack()

        label_leg_press_text = ctk.CTkLabel(leg_press_frame, text="Leg Press \n3x12 reps", text_color="white", font=("Arial", 16))
        label_leg_press_text.pack()

        # Exercício 4: Agachamento Frontal
        agachamento_frontal_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\agachamento_frontal.webp"
        self.agachamento_frontal_image = ctk.CTkImage(light_image=Image.open(agachamento_frontal_image_path), size=(150, 150))
        agachamento_frontal_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        agachamento_frontal_frame.grid(row=2, column=0, padx=20, pady=20)

        label_agachamento_frontal_img = ctk.CTkLabel(agachamento_frontal_frame, image=self.agachamento_frontal_image, text="")
        label_agachamento_frontal_img.pack()

        label_agachamento_frontal_text = ctk.CTkLabel(agachamento_frontal_frame, text="Agachamento Frontal \n3x10 reps", text_color="white", font=("Arial", 16))
        label_agachamento_frontal_text.pack()

        # Exercício 5: Avanço
        avancado_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\avanco.webp"
        self.avancado_image = ctk.CTkImage(light_image=Image.open(avancado_image_path), size=(150, 150))
        avancado_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        avancado_frame.grid(row=2, column=1, padx=20, pady=20)

        label_avancado_img = ctk.CTkLabel(avancado_frame, image=self.avancado_image, text="")
        label_avancado_img.pack()

        label_avancado_text = ctk.CTkLabel(avancado_frame, text="Avanço \n3x12 reps", text_color="white", font=("Arial", 16))
        label_avancado_text.pack()

        # Exercício 6: Step-Up
        step_up_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Quadriceps\\step_up.webp"
        self.step_up_image = ctk.CTkImage(light_image=Image.open(step_up_image_path), size=(150, 150))
        step_up_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        step_up_frame.grid(row=2, column=2, padx=20, pady=20)

        label_step_up_img = ctk.CTkLabel(step_up_frame, image=self.step_up_image, text="")
        label_step_up_img.pack()

        label_step_up_text = ctk.CTkLabel(step_up_frame, text="Step-Up \n3x12 reps", text_color="white", font=("Arial", 16))
        label_step_up_text.pack()


        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)



    def Perna(self):
        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, fg_color="#313131", corner_radius=0)
        background_frame.pack(fill="both", expand=True)

        # Frame central para os exercícios, centralizado
        central_frame = ctk.CTkFrame(background_frame, fg_color="#313131")
        central_frame.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)  # Centralizando o frame

        # Título do treino
        label_pernas = ctk.CTkLabel(central_frame, text="Treino de Perna", text_color="white", font=("Arial", 22, 'bold'))
        label_pernas.grid(row=0, column=0, columnspan=3, pady=10)

        # Exercício 1: Stiff
        stiff_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\stiff.webp"
        self.stiff_image = ctk.CTkImage(light_image=Image.open(stiff_image_path), size=(150, 150))
        stiff_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=15, width=200, height=200)
        stiff_frame.grid(row=1, column=0, padx=20, pady=20)

        label_stiff_img = ctk.CTkLabel(stiff_frame, image=self.stiff_image, text="")
        label_stiff_img.pack()

        label_stiff_text = ctk.CTkLabel(stiff_frame, text="Stiff \n3x12 reps", text_color="white", font=("Arial", 16))
        label_stiff_text.pack()

        # Exercício 2: Afundo com Halteres
        afundo_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\afundo_halteres.gif"
        self.afundo_image = ctk.CTkImage(light_image=Image.open(afundo_image_path), size=(150, 150))
        afundo_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30, width=200, height=200)
        afundo_frame.grid(row=1, column=1, padx=20, pady=20)

        label_afundo_img = ctk.CTkLabel(afundo_frame, image=self.afundo_image, text="")
        label_afundo_img.pack()

        label_afundo_text = ctk.CTkLabel(afundo_frame, text="Afundo com Halteres\n3x12 reps", text_color="white", font=("Arial", 16))
        label_afundo_text.pack()

        # Exercício 3: Flexão de Pernas na Máquina
        pernas_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\pernas-na-maquina.webp"
        self.pernas_image = ctk.CTkImage(light_image=Image.open(pernas_image_path), size=(150, 150))
        pernas_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        pernas_frame.grid(row=1, column=2, padx=20, pady=20)

        label_pernas_img = ctk.CTkLabel(pernas_frame, image=self.pernas_image, text="")
        label_pernas_img.pack()

        label_pernas_text = ctk.CTkLabel(pernas_frame, text="Flexão de Pernas na Máquina \n3x15 reps", text_color="white", font=("Arial", 16))
        label_pernas_text.pack()

            # Exercício 4: Agachamento Sumô
        sumo_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\agachamento_sumo.webp"
        self.sumo_image = ctk.CTkImage(light_image=Image.open(sumo_image_path), size=(150, 150))
        sumo_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        sumo_frame.grid(row=2, column=0, padx=20, pady=20)

        label_sumo_img = ctk.CTkLabel(sumo_frame, image=self.sumo_image, text="")
        label_sumo_img.pack()

        label_sumo_text = ctk.CTkLabel(sumo_frame, text="Agachamento Sumô \n3x12 reps", text_color="white", font=("Arial", 16))
        label_sumo_text.pack()

        # Exercício 5: Levantamento de Quadril
        hip_thrust_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\levantamento_quadril.gif"
        self.hip_thrust_image = ctk.CTkImage(light_image=Image.open(hip_thrust_image_path), size=(150, 150))
        hip_thrust_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        hip_thrust_frame.grid(row=2, column=1, padx=20, pady=20)

        label_hip_thrust_img = ctk.CTkLabel(hip_thrust_frame, image=self.hip_thrust_image, text="")
        label_hip_thrust_img.pack()

        label_hip_thrust_text = ctk.CTkLabel(hip_thrust_frame, text="Levantamento de Quadril \n3x12 reps", text_color="white", font=("Arial", 16))
        label_hip_thrust_text.pack()

        # Exercício 6: Elevação de Panturrilha
        panturrilha_image_path = "Projeto Academia\\img\\Treinos\\Inferiores\\Pernas\\elevacao_panturrilha.webp"
        self.panturrilha_image = ctk.CTkImage(light_image=Image.open(panturrilha_image_path), size=(150, 150))
        panturrilha_frame = ctk.CTkFrame(central_frame, fg_color="#29412b", corner_radius=30)
        panturrilha_frame.grid(row=2, column=2, padx=20, pady=20)

        label_panturrilha_img = ctk.CTkLabel(panturrilha_frame, image=self.panturrilha_image, text="")
        label_panturrilha_img.pack()

        label_panturrilha_text = ctk.CTkLabel(panturrilha_frame, text="Elevação de Panturrilha \n3x15 reps", text_color="white", font=("Arial", 16))
        label_panturrilha_text.pack()

        # Frame inferior com botão Voltar
        frame_inferior = ctk.CTkFrame(background_frame, fg_color="#5ce1e6", corner_radius=0, height=50)
        frame_inferior.pack(side="bottom", fill="x")

        btn_voltar = ctk.CTkButton(frame_inferior, text="Voltar", fg_color="#808080", hover_color="#A9A9A9", command=self.Inferiores, font=("Arial", 18, "bold"), width=150, height=50)
        btn_voltar.pack(pady=10)
