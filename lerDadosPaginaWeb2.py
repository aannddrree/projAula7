from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pymongo

#CONFIG MONGO:
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["extradb"]
mycol = mydb["celulares"]

numeroPagina=1

url = 'https://www.extra.com.br/?Filtro=D36611&Ordenacao=_MaisVendidos&paginaAtual={}&ComparacaoProdutos=&AdicionaListaCasamento='.format(numeroPagina)

req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

nomeCelular = page_soup.findAll("strong", "name fn")

listNome = []
listPreco = []

for container in nomeCelular:
    descricao = str(container).replace('<strong class="name fn">', '')
    descricao = descricao.replace('</strong>', '')
    listNome.append(descricao)

precos = page_soup.findAll("span","for price sale")

for container in precos:
    preco = str(container).replace('<span class="for price sale">Por: <strong>', '')
    preco = preco.replace('</strong></span>', '')
    listPreco.append(preco)

print("DADOS COLETADOS DA PAGINA WEB:")
print("descricao, preco")

contador = 0
for dados in nomeCelular:
    #print("{} - {} ".format(str(listNome[contador]),str(listPreco[contador])))
    registro = {"nome": str(listNome[contador]), "preco": str(listPreco[contador])}
    x = mycol.insert_one(registro)
    print(x.inserted_id)
    contador = contador + 1
