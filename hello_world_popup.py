import tkinter as tk
from tkinter import messagebox
import sqlite3

        
        
class SaudacaoDAO:
    def __init__(self):
        self.conn = sqlite3.connect("saudacoes.db")
        self.criar_tabela()

    def criar_tabela(self):
        query = """CREATE TABLE IF NOT EXISTS saudacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    idioma TEXT,
                    mensagem TEXT
                )"""
      
        self.conn.execute(query)
        self.conn.commit()
        
        # Adicione as saudações para os idiomas desejados
        
        idiomas_saudacoes = [
            ("Português", "Olá, Mundo!"),
            ("Inglês", "Hello, World!"),
            ("Espanhol", "¡Hola, Mundo!"),
            ("Frances", "Bonjour le monde!"),
            ("Alemão", "Hallo Welt!"),
            ("Russo", "Привет, мир!"),
            ("Chinês", "你好世界!"),
            ("Finlandês", "Hei maailma!"),
            ("Polonês", "Witaj świecie!"),
            ("Hungaro", "Helló Világ!"),
            # Adicione mais idiomas e saudações conforme necessário
            ]
                           
        for idioma, saudacao in idiomas_saudacoes:
                self.adicionar_saudacao(idioma, saudacao)
  

    def adicionar_saudacao(self, idioma, mensagem):
        query = "INSERT INTO saudacoes (idioma, mensagem) VALUES (?, ?)"
        self.conn.execute(query, (idioma, mensagem))
        self.conn.commit()

    def obter_saudacao(self, idioma):
        query = "SELECT mensagem FROM saudacoes WHERE idioma = ?"
        cursor = self.conn.execute(query, (idioma,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Saudações Multilíngues")

        self.dao = SaudacaoDAO()
    
  

        # Variável para armazenar a escolha do idioma
        self.var_idioma = tk.StringVar(self.master)
        self.var_idioma.set("Português")  # Idioma padrão
        self.var_idioma.set("Inglês")
        self.var_idioma.set("Espanhol")
        self.var_idioma.set("Frances")
        self.var_idioma.set("Alemão")
        self.var_idioma.set("Russo")
        self.var_idioma.set("Chinês")
        self.var_idioma.set("Finlandês")
        self.var_idioma.set("Polonês")
        self.var_idioma.set("Hungaro")

        # Menu suspenso para selecionar o idioma
        
        
        self.menu_idioma = tk.OptionMenu(self.master, self.var_idioma, "Português", "Inglês", "Espanhol", "Frances", "Alemão", "Russo", "Chinês", "Finlandês", "Polonês", "Hungaro")
        self.menu_idioma.pack(pady=10)
            

        # Botão para exibir a saudação
        self.botao_saudacao = tk.Button(self.master, text="Mostrar Saudação", command=self.mostrar_saudacao)
        self.botao_saudacao.pack(pady=20)
        
        


    def mostrar_saudacao(self):
        idioma_selecionado = self.var_idioma.get()
        mensagem = self.dao.obter_saudacao(idioma_selecionado)
        if mensagem:
            messagebox.showinfo("Saudação", mensagem)
        else:
            messagebox.showwarning("Aviso", "Saudação não encontrada para o idioma selecionado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
