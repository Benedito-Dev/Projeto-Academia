import tkinter as tk
from customtkinter import CTkLabel, CTkButton
from random import randint
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk
from controller.controllers import UsuarioController


class Funções():
    def __init__(self):
        self.controler = UsuarioController()

    def Exibir_senha(self):
        if self.check_senha.get() == 1:
            self.entry_senha.configure(show="")
        else:
            self.entry_senha.configure(show="*")
    

    def iniciar_carrossel_imagens(self, titulo, frame, exercicios, largura, altura):
        # Carrega as imagens e informações dos exercícios
        imagens_carregadas = [
            {
                "imagem": ImageTk.PhotoImage(Image.open(ex["imagem"]).resize((largura, altura))),
                "nome": ex["nome"],
                "series": ex["series"],
                "repeticoes": ex["repeticoes"]
            } for ex in exercicios
        ]
        index = 0

        #Label para exibir titulo do exericios
        label_titulo = CTkLabel(frame, text=titulo, text_color="white", font=("Arial", 22, 'bold'))
        label_titulo.grid(row=0, column=0, columnspan=3, pady=20)

        # Label para exibir a imagem no carrossel
        label_imagem = CTkLabel(frame, text="")
        label_imagem.grid(row=1, column=1)

        # Label para exibir o texto do exercício
        label_texto = CTkLabel(frame, text="", text_color="white", font=("Arial", 16, 'bold'))
        label_texto.grid(row=2, column=1, pady=10)

        # Função para exibir a imagem e o texto atual
        def exibir_imagem():
            exercicio_atual = imagens_carregadas[index]
            label_imagem.configure(image=exercicio_atual["imagem"])
            label_texto.configure(text=f"{exercicio_atual['nome']}: {exercicio_atual['series']} séries de {exercicio_atual['repeticoes']} repetições")

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
        btn_anterior = CTkButton(frame, text="⟵ Anterior", command=mostrar_anterior)
        btn_anterior.grid(row=1, column=0, padx=5, pady=5)

        btn_proximo = CTkButton(frame, text="Próximo ⟶", command=mostrar_proximo)
        btn_proximo.grid(row=1, column=2, padx=5, pady=5)

        # Exibe a primeira imagem e texto
        exibir_imagem()


    def mudar_exercicios(self, titulo, novos_exercicios, central_frame):

        """Muda os exercícios exibidos para o carrossel."""
        self.exercicios_atual = novos_exercicios
        self.indice_atual = 0
        # Limpa o frame central
        for widget in central_frame.winfo_children():
            widget.destroy()
        # Reinicia o carrossel de imagens
        self.iniciar_carrossel_imagens(titulo, central_frame, self.exercicios_atual, 200, 200)

    def gerar_codigo(self):
        # Gera o primeiro número entre 1 e 7 para que os próximos sejam sequenciais
        a = randint(1, 7)

        choose = randint(1, 2)

        if choose == 1:
            b = a + 1
            c = b + 1

        else:
            b = a - 1
            c = b - 1

        # Concatena os números para formar o código em string
        codigo = f"{a}{b}{c}"
        return codigo

    def carregar_perfis(self):
        try:
            # Obtendo os dados da tabela através do controlador
            users = self.controler.listar_usuarios()

            #Ordendando lista de usuarios por nome
            users = sorted(users, key=lambda user : user.nome)

            # Inserindo os dados na ordem correta no TreeView
            for user in users:
                id = user.id  # Acessando o atributo 'id'
                nome = user.nome  # Acessando o atributo 'nome'
                data_de_nascimento = user.data_de_nascimento
                self.tree.insert('', tk.END, values=(id, nome, data_de_nascimento))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar perfis: {e}")


    def validar_dados(self):
        nome = self.entry_nome.get().strip()
        data_de_nascimento = self.entry_dataDeNascimento.get().strip()

        # Validação do nome (mínimo de 3 letras, apenas caracteres alfabéticos)
        if len(nome) < 3 or not nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return

        # Se todos os dados estiverem válidos, prosseguir com a lógica de envio
        self.enviar_dados(nome=nome, data_de_nascimento=data_de_nascimento)


    def enviar_dados(self, nome, data_de_nascimento):
        if self.controler.adicionar_usuario(nome.upper(), data_de_nascimento):
            self.after(500, self.menu_inicial)


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
        nome = self.entry_nome.get().strip()
        data_de_nascimento = self.entry_dataDeNascimento.get().strip()

        # Verificando atributos
        if len(nome) < 3 or not nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return
        
        if not data_de_nascimento:
            messagebox.showerror("Erro", "A data de nascimento não pode estar vazia.")
            return
        
        #Convertendo data antes de enviar
        data_de_nascimento =  datetime.strptime(data_de_nascimento, "%d/%m/%Y")
        data_de_nascimento = data_de_nascimento.date()
        
        # Chama o método do controlador para validar o login
        if self.controler.fazer_login(nome.upper(), data_de_nascimento) :
            self.nome_usuario = nome.capitalize()
            self.after(500, self.Home)
        else:
            pass
    

    def puxar_informacoes(self):
        user_name = self.nome_usuario.strip().upper()

        try:
            user = self.controler.obter_usuario_por_nome(user_name)


            if user:
                self.informacoes = user

            else:
                messagebox.showinfo("Info", "Usuario não encontrado")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Ao buscar informações : {e}")


    def get_informacao(self, informacao):
        return getattr(self.informacoes, informacao, None)
    

    def validar_alteracoes(self):
        id_cliente = self.get_informacao("id")  # Renomeado para id_cliente para maior clareza

        novo_nome = self.entry_novo_nome.get().strip().upper() or self.get_informacao("nome").upper()
        nova_data_de_nascimento = self.entry_dataDeNascimento.get().strip() or self.get_informacao("data_de_nascimento")


        # Validação do nome
        if len(novo_nome) < 3 or not novo_nome.isalpha():
            messagebox.showerror("Erro", "O nome deve ter pelo menos 3 letras e conter apenas caracteres alfabéticos.")
            return

        # Chamada para salvar alterações
        self.salvar_alterações(id_cliente, novo_nome, nova_data_de_nascimento)


    def salvar_alterações(self, id, nome, data_de_nascimento):
        if not data_de_nascimento:
            messagebox.showerror("Erro", "Data de nascimento inválida")
            return

        try:
            self.nome_usuario = nome
            self.controler.atualizar_usuario(id=id, nome=nome, data_de_nascimento=data_de_nascimento)
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