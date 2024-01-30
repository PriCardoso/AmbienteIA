import sqlite3
from googletrans import LANGUAGES



class HelloWorldPopUpData:
    def __init__(self, master):
        self.master = master
        self.conn = None  # Inicializa a conexão como None

    def conectar(self):
        # Implemente a lógica de conexão com o banco de dados
        try:
            self.conn = sqlite3.connect('F:\Estudos\AI\AmbienteIA\saudacoes.sql')
            return True
        except sqlite3.Error as e:
            print(f"Erro na conexão com o banco de dados: {e}")
            return False

    def desconectar(self):
        if self.conn:
            self.conn.close()

    def obter_saudacao(self, idioma):
        if self.conn:
            query = "SELECT mensagem FROM saudacoes WHERE idioma = ?"
            cursor = self.conn.execute(query, (idioma,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        else:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return None

    def obter_saudacoes_todas_linguagens(self):
        saudacoes_por_idioma = {}

        if self.conn:
            for idioma, nome_idioma in LANGUAGES.items():
                saudacao = self.obter_saudacao(idioma)
                saudacoes_por_idioma[idioma] = saudacao if saudacao else f"Saudação não encontrada para {nome_idioma}"

        return saudacoes_por_idioma

    def inserir_saudacao(self, idioma, mensagem):
        if self.conn:
            try:
                query = "INSERT INTO saudacoes (idioma, mensagem) VALUES (?, ?)"
                self.conn.execute(query, (idioma, mensagem))
                self.conn.commit()
                print("Saudação inserida com sucesso.")
            except sqlite3.Error as e:
                print(f"Erro ao inserir saudação no banco de dados: {e}")
        else:
            print("Erro: Conexão com o banco de dados não estabelecida.")

    def obter_saudacoes_todas_linguagens(self):
            saudacoes_por_idioma = {}

            if self.conn:
                try:
                    query = "SELECT idioma, mensagem FROM saudacoes"
                    cursor = self.conn.execute(query)
                    resultados = cursor.fetchall()

                    for idioma, mensagem in resultados:
                        saudacoes_por_idioma[idioma] = mensagem

                    return saudacoes_por_idioma
                except sqlite3.Error as e:
                    print(f"Erro ao obter saudações do banco de dados: {e}")
            else:
                print("Erro: Conexão com o banco de dados não estabelecida.")
                return None

    def importar_saudacoes(self, saudacoes):
        if self.conn:
            for idioma, mensagem in saudacoes.items():
                self.inserir_saudacao(idioma, mensagem)
        else:
            print("Erro: Conexão com o banco de dados não estabelecida.")
        
    def limpar_tabela_saudacoes(self):
        query = "DELETE FROM saudacoes"
        self.conn.execute(query)
        self.conn.commit()
