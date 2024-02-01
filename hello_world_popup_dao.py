import psycopg2
from psycopg2 import sql
from hello_world_popup_data import HelloWorldPopUpData

class HelloWorldPopUpDB:
    def insert_data(self, lang, description):
        """
        Inserts a new language and its description into the hello_world table.

        Parameters:
        lang (str): The language to be inserted.
        description (str): The description of the language to be inserted.
        """
        # Initialize the database connection
        banco = HelloWorldPopUpData()
        conn = banco.conectar()
        cursor = conn.cursor()   # Adicione as saudações para os idiomas desejados
        
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