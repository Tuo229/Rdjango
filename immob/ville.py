import requests
from bs4 import BeautifulSoup
from .models import Ville

def urls_ville():
    urls = []


    url = 'https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Ville_en_C%C3%B4te_d%27Ivoire'

    response = requests.get(url)

    if response.ok:

        soup = BeautifulSoup(response.text, 'lxml')
        tds = soup.findAll('li')
        i=0
        for td in tds:
            if i >= 139 and i <= 336:
                ville = Ville.objects.create(ville=td.text)
                ville.save()
                urls.append(td.text)
            i+=1
    return urls