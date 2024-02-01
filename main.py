from hello_world_data import HelloWorldData
from hello_world_dao import HelloWorldDB

banco = HelloWorldData()
db = HelloWorldDB()

#print("Conectando no banco de dados")

#banco.conectar()

#print("desconectando do banco de dados")

#banco.desconectar()

db.insert_data(lang='pt', description='Bom Dia')
db.insert_data(lang='en', description='Good Morning')

