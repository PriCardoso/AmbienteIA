import os
import psycopg2

class HelloWorldData:
    """
    A class to handle database operations for a HelloWorld application.
    """
    
    def __init__(self):
        """
        Initializes the HelloWorldData instance by setting database connection parameters.
        """
        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.conn = None
        self.cursor = None

    def conectar(self):
        """
        Establishes a connection to the database using the psycopg2 library.
        Prints the status of the connection attempt.
        """
        print('conectando banco')
        print(os.getenv("DB_NAME"))
        
        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Conexão estabelecida com sucesso.")
            return conn
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")