from googletrans import Translator
from hello_world_data import HelloWorldData
from hello_world_dao import HelloWorldDB

# Cria uma instância de HelloWorldData
teste = HelloWorldData()
teste.conectar()

# Cria uma instância de HelloWorldDB
db_instance = HelloWorldDB()

# Cria uma instância do Translator
translator = Translator()

# A frase que queremos traduzir
phrase = "Olá Mundo"

# Lista de idiomas para os quais queremos traduzir nossa frase.
# Estes são os códigos de idioma para cada um dos idiomas.
# Espanhol, Francês, Alemão, Russo e Chinês
languages = ['es', 'fr', 'de', 'ru', 'zh-cn', 'fi', 'pl', 'hu']

# Traduzindo a frase para cada idioma
for lang in languages:
    translated_phrase = translator.translate(phrase, dest=lang)
    db_instance.insert_data(lang, translated_phrase.text)
    print(f'{translated_phrase.origin} ({translated_phrase.src}) --> {translated_phrase.text} ({translated_phrase.dest})')
