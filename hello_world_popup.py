import tkinter as tk
from tkinter import messagebox

def exibir_popup(mensagem):
    messagebox.showinfo("Pop-up", mensagem)

def selecionar_idioma():
    idioma_selecionado = var_idioma.get()
    if idioma_selecionado == "Português":
        exibir_popup("Olá, Mundo!")
    elif idioma_selecionado == "Inglês":
        exibir_popup("Hello, World!")
    elif idioma_selecionado == "Espanhol":
        exibir_popup("¡Hola, Mundo!")
    elif idioma_selecionado == "Frances":
        exibir_popup("Bonjour le monde!")
    elif idioma_selecionado == "Alemão":
        exibir_popup("Hallo Welt!")
    elif idioma_selecionado == "Russo":
        exibir_popup("Привет, мир!")
    elif idioma_selecionado == "Chinês":
        exibir_popup("你好世界!")
    elif idioma_selecionado == "Finlandês":
        exibir_popup("Hei maailma!")
    elif idioma_selecionado == "Polonês":
        exibir_popup("Witaj świecie!")
    elif idioma_selecionado == "Hungaro":
        exibir_popup("Helló Világ!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Saudações Multilíngues")

# Variável para armazenar a escolha do idioma
var_idioma = tk.StringVar(janela)
var_idioma.set("Português")  # Idioma padrão

# Menu suspenso para selecionar o idioma
menu_idioma = tk.OptionMenu(janela, var_idioma, "Português", "Inglês", "Espanhol", "Frabces", "Alemão", "Russo", "Chinês", "Finlandês", "Polonês", "Hungaro")
menu_idioma.pack(pady=10)

# Botão para exibir a saudação
botao_saudacao = tk.Button(janela, text="Mostrar Saudação", command=selecionar_idioma)
botao_saudacao.pack(pady=20)

# Iniciar o loop principal da janela
janela.mainloop()