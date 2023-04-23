import telebot
from telebot import types
from news_parser import *

class TheJornalBot():

    #Key do Bot: #Token do Bot: 5491245870:AAEtvN233Q2FKL0nTjRj8oZ0BNtU6XGsjJo

    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.bot = telebot.TeleBot(self.api_key)
        pass


    def __pegaPortais(self):


        #Message Handler que exibe a mensagem inicial quando o código é executado.
        @self.bot.message_handler(commands=['start'])
        def mensagemInicial(mensagem):
            self.bot.reply_to(mensagem, "Olá, bem vindo ao bot de notícias. Aqui você pode escolher um site de notícias da sua preferência e eu irei automaticamente puxar as últimas cinco principais notícias.")
            self.bot.reply_to(mensagem, "Acesse meus portais de notícia disponíveis com o comando /buscarportais")


        #Message Handler que exibe um KeyBoard com todos os portais disponíveis para acessar.
        @self.bot.message_handler(commands=['buscarportais'])
        def resposta(mensagem):

            #Definindo o KeyBoard:
            keyboard = types.ReplyKeyboardMarkup()
            option1 = types.KeyboardButton("G1")
            option2 = types.KeyboardButton("BandNews")
            keyboard.add(option1, option2)

            self.bot.reply_to(mensagem, "Escolha um veículo de notícias.", reply_markup=keyboard)


            #Se o usuário escolher o G1, o código irá exibir uma mensagem e em seguida irá executar o método "get_link" da classe G1Parser.
            @self.bot.message_handler(func=lambda message: message.text == "G1")
            def materias_g1(mensagem):
                self.bot.reply_to(mensagem, "Aqui estão as últimas notícias do G1:")

                g1_links = G1Parser("https://g1.globo.com")
                materias = g1_links.get_link()

                for materia in materias:
                    self.bot.reply_to(mensagem, f'{materia}')


            #Se o usuário escolher o BandNews, o código irá exibir uma mensagem e em seguida irá executar o método "get_link" da classe BandParser.
            @self.bot.message_handler(func=lambda message: message.text == "BandNews")
            def materias_g1(mensagem):
                self.bot.reply_to(mensagem, "Aqui estão as últimas notícias do BandNews:")

                band_links = BandParser('https://www.band.uol.com.br')
                materias = band_links.get_link()

                for materia in materias:
                    self.bot.reply_to(mensagem, f'{materia}')


    
    def executaBot(self):

        #Executa o código de pegar os portais de notícias:
        self.__pegaPortais()
        
        self.bot.polling()