import requests

def pegar_moeda(moeda_origem, moeda_destino):
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    data = requests.get(link)

    cotacao = data.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotacao