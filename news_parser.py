import requests
from bs4 import BeautifulSoup

class G1Parser():

    def __init__(self, link):
        self.link = link


    #Método que pega todos os links de matérias do site.
    def get_link(self):
        
        #lista que será preenchida posteriormente com os links da página.
        link_materia = []

        # faz uma requisição para a página
        response = requests.get(self.link)

        # analisa o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # encontra todas as divs que tem a classe 'bastian-feed-item'
        divs_materia = soup.find_all('div', {'class':'bastian-feed-item'})

        #itera sobre cada div dentro das divs_materia e encontra os 'a'
        for div in divs_materia:

            links_materia = div.find_all('a')

            #Itera sobre cada link dentro de cada 'a' das divs
            for link in links_materia:

                link_materia.append(link.get('href'))

        link_materia = list(set(link_materia))
        return link_materia


class BandParser():

    def __init__(self, link) -> None:
        self.link = link
        pass


    def get_link(self):

        link_materia=[]

        r = requests.get(self.link)

        soup = BeautifulSoup(r.text, 'html.parser')

        divs_materia = soup.find_all('li', {'class':'item item--200 item--3columns hibrido borderless'})

        for div in divs_materia:

            links_materia = div.find_all('a')

            for link in links_materia:

                fim_link = link.get('href')
                comeco_link = 'https://www.band.uol.com.br'
                link = f'{comeco_link}{fim_link}'

                link_materia.append(link)

        link_materia = list(set(link_materia))
        return link_materia
    

