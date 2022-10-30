import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from teste import retornaPlayers

CHAVE_API = "5700877420:AAEswiXVwrG89auLKlx3tRxQSYKU_qaBZLA"

bot = telebot.TeleBot(CHAVE_API)

# import requests

def reinciarServidor():
    url = 'https://painel.enxadahost.com/api/client/servers/0073aa55/power'
    headers = {
        "Authorization": "Bearer uTko1eqVK088wCuP9rhL9HuDKlqfhGGMosG9HlLk8HEP7VeK",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = '{  "signal": "restart"}'

    response = requests.request('POST', url, data=payload, headers=headers)
    print(response.text)


# url = 'https://painel.enxadahost.com/api/client/servers/b0d57748/command'
# headers = {
#     "Authorization": "Bearer uTko1eqVK088wCuP9rhL9HuDKlqfhGGMosG9HlLk8HEP7VeK",
#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }
# payload = '{   "command": "say CodeCo says Hi!"}'

# response = requests.request('POST', url, data=payload, headers=headers)
# print(response.text)



def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2
    markup.add(
        InlineKeyboardButton("Jogadores Online"   ,callback_data = "consultaJogadores"),
        InlineKeyboardButton("Reiniciar Servidor",callback_data = "restartServer")

    )
    return markup

@bot.callback_query_handler(func=lambda teste: True,)
def callback_querry(call):
    if call.data == "consultaJogadores":
        bot.answer_callback_query(call.id, "Carregando...")
        retorno  = retornaPlayers()

        maxPlayer = retorno["maxPlayers"].values[1]
        onlinePlayers = retorno["onlinePlayers"].values[1]
        players = retorno["players"].values[1]    

        for nome in players:
            print(nome)
        if maxPlayer == 0:
            texto = """
            Servidor Offline ou Inicializando...
            """
        elif onlinePlayers == 0 :
            texto = """
                Status Servidor: 
                Jogadores: %s de %s""" % (onlinePlayers,maxPlayer)
        else:
            texto = """
                Status Servidor: 
                Jogadores: %s de %s
                Jogadores Online:""" % (onlinePlayers,maxPlayer)
            for nome in players:
                texto += """
                        %s""" % (nome)

        bot.send_message(call.message.chat.id, texto)
    if call.data == "restartServer":
        reinciarServidor()

@bot.message_handler(func=lambda teste: True,)
def responder(mensagem):
    texto = """
    Servidor: Em Busca da Cidade Automática  
    """ 
    print(mensagem)
    bot.reply_to(mensagem, texto, reply_markup = markup_inline())

bot.polling()
