from googletrans import LANGUAGES
from googletrans import Translator
from hello_world_data import HelloWorldData

#Cria conexao com banco de dados
teste = HelloWorldData()
teste.conectar



# Cria uma instância do Translator
translator = Translator()

# A frase que queremos traduzir
phrase = "Olá Mundo"

# Lista de idiomas para os quais queremos traduzir nossa frase.
# Estes são os códigos de idioma para cada um dos idiomas.
# Espanhol, Francês, Alemão, Russo, Chinês, Finlandes, polones e hungaro
languages = ['es', 'fr', 'de', 'ru', 'zh-cn', 'fi', 'pl', 'hu']

# Traduzindo a frase para cada idioma
for lang in languages:
    translated_phrase = translator.translate(phrase, dest=lang)
    print(f'{translated_phrase.origin} ({translated_phrase.src}) --> {translated_phrase.text} ({translated_phrase.dest})')
    

