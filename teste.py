import requests
import pandas as pd
 
def retornaPlayers():
    url = 'https://painel.enxadahost.com/api/client/servers/74c54e8c/players'
    headers = {
        "Authorization": "Bearer bykIFX4KH3bU3QvK7WoipXGgyrOgewotkYkkfsKBsuTriGF5",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = '{"event":"send stats","args":[null]}'

    response = requests.request('GET', url,  headers=headers)
    print(response.text)
    retorno = pd.read_json(response.text)

    retorno  = pd.DataFrame(retorno).transpose()

    # for texto in retorno:
    #     print(str(texto) + " - " + str(retorno[texto].values[1]))
    # maxPlayer = retorno["maxPlayers"].values[1]
    # onlinePlayers = retorno["onlinePlayers"].values[1]
    # players = retorno["players"].values[1]

    return retorno
