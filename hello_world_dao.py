import psycopg2
from psycopg2 import sql
from hello_world_data import HelloWorldData

class HelloWorldDB:
    def insert_data(self, lang, description):
        """
        Inserts a new language and its description into the hello_world table.

        Parameters:
        lang (str): The language to be inserted.
        description (str): The description of the language to be inserted.
        """
        # Initialize the database connection
        banco = HelloWorldData()
        conn = banco.conectar()
        cursor = conn.cursor()

        # Construct and execute the insert query
        insert_query = sql.SQL('INSERT INTO hello_world (lang, description) VALUES ({}, {});').format(
            sql.Literal(lang),
            sql.Literal(description)
        )
        print(insert_query)
        cursor.execute(insert_query)
        conn.commit()