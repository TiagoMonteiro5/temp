from flask import Flask
import connexion
import config

#Cria a instância da app
connex_app = config.connex_app

# Leitura do ficheiro swagger.yml para configurar os endpoints
connex_app.add_api("swagger.yml")

# Quando usamos decorador route() que diz ao Flask que URL deve acionar a nossa função
@connex_app.route('/')
    # É dado o nome á função que será usada para gerar URL's para essa função particular e
    # Retorna mensagem que mostrar ao utilizador
def home():
    """
    Esta função vai responder ao URL localhost:5000/home
    :return String "Welcome Home User"
    """
    return "Welcome to the home page"

if __name__ == '__main__':
    connex_app.run(host = '127.0.0.1', port = 8080, debug=True)