import tkinter as tk
from tkinter import messagebox
from googletrans import LANGUAGES
from hello_world_popup_data import HelloWorldPopUpData

class App:
    def __init__(self, master, conexao_bd):
        self.master = master
        self.master.title("Saudações Multilíngues")

        # Conecta ao banco de dados e verifica se a conexão foi bem-sucedida
        self.teste = HelloWorldPopUpData(master)
        if self.teste.conectar():
            # Adiciona um botão para exibir saudações em diferentes idiomas
            self.btn_mostrar_saudacoes = tk.Button(
                master, text="Mostrar Saudações", command=self.mostrar_saudacoes)
            self.btn_mostrar_saudacoes.pack(pady=20)
        else:
            print("Erro: Não foi possível conectar ao banco de dados.")

    def mostrar_saudacoes(self):
        # Obtém todas as saudações disponíveis no banco de dados
        saudacoes_por_idioma = self.teste.obter_saudacoes_todas_linguagens()

        # Exibe as saudações importadas em um pop-up
        if saudacoes_por_idioma:
            mensagem = ""
            for idioma, saudacao in saudacoes_por_idioma.items():
                nome_idioma = LANGUAGES.get(idioma, 'Idioma Desconhecido')
                mensagem += f"{nome_idioma}: {saudacao}\n"

            messagebox.showinfo("Saudações Importadas", mensagem)
        else:
            messagebox.showwarning("Aviso", "Não foi possível obter saudações importadas.")

if __name__ == "__main__":
    # Criação da instância de HelloWorldPopUpData
    teste = HelloWorldPopUpData(None)

    # Conectar ao banco de dados
    if teste.conectar():
        # Dados de exemplo (substitua pelos dados reais que você possui)
        saudacoes_importadas = {
            'fr': 'Bonjour le monde',
            'es': 'Hola Mundo',
            'pt': 'Olá, Mundo!',
            'en': 'Hello, World!',
            'de': 'Hallo Welt!',
            'ru': 'Привет, мир!',
            'cn': '你好世界!',
            'fi': 'Hei maailma!',
            'pl': 'Witaj świecie!',
            'hu': 'Helló Világ!',
            # Adicione mais saudações conforme necessário
        }

        # Importar saudações
        teste.limpar_tabela_saudacoes()
        teste.importar_saudacoes(saudacoes_importadas)

        # Desconectar do banco de dados
        teste.desconectar()
    else:
        print("Erro: Não foi possível conectar ao banco de dados.")

    # Criar uma instância de Tkinter
    root = tk.Tk()

    # Passa a instância para a classe App
    app = App(root, teste.conn)

    # Executa o loop principal do tkinter
    root.mainloop()