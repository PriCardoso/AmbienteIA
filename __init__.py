def hello_world(language):
    greetings = {
        'english': 'Hello, World!',
        'portuguese': 'Olá, Mundo!',
        'spanish': '¡Hola, Mundo!',
        'french': 'Bonjour, Monde!',
        'german': 'Hallo, Welt!',
        'italian': 'Ciao, Mondo!',
        'russian': 'Привет, мир!',
        'japanese': 'こんにちは、世界！',
        'chinese': '你好，世界！',
        'hindi': 'नमस्ते, दुनिया!'
    }
    return greetings.get(language.lower(), "Language not supported.")

# Exemplo de uso:
print(hello_world('english'))  # Imprime em inglês
print(hello_world('portuguese'))  # Imprime em português
print(hello_world('spanish'))  # Imprime em espanhol
# Adicione mais chamadas de função conforme necessário para outros idiomas