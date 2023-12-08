import requests

testUrl="https://api.geoapify.com/v2/places?categories=commercial.supermarket&filter=rect%3A10.716463143326969%2C48.755151258420966%2C10.835314015356737%2C48.680903341613316&limit=20&apiKey=048fde22cdb44f41963fb00652ca6298"
url="https://api.geoapify.com/v2/places"
apiKey="&apiKey=048fde22cdb44f41963fb00652ca6298"
def link(coordenadas,raiom,atraçõeslista):

    for x in range(len(atraçõeslista)):
        url1=url +"?categories=" + atraçõeslista[x]+"&filter=circle:"+coordenadas[0]+","+coordenadas[1]+","+raiom+ "&bias=proximity:" + coordenadas[0]+","+coordenadas[1]+ "&limit=20"+apiKey
    return url1

    #criei esta função para criar o url, nao sei se esta boa ou nao, pode ser q exista uma me5rda mais rapida e nao vi

def main():
    localização=input("Ensira a sua posição em latitude e longitude separados por virgula: ")
    coordenadas=localização.split(",")
    raio=float(input("Quão longe quer viajar em kms: "))
    raiom=str(raio*1000)
    atrações=input("Ensira as suas atrações desejadas separados por virgula: ")
    atraçõeslista=atrações.split(",")
    apil=link(coordenadas,raiom,atraçõeslista)
    #pus isto que sao as cenas q temos que pedir a pessoa, btw aqui em baixo pus tmb a cena com o meu categories pq assim tmb consigo ver isso
    request(apil)

    with open(r"C:\Users\simao\Desktop\FP\Projeto-FP\projeto-FP\Projeto-FP\categories.txt") as file:
        places = [file.readline()[:-1] for line in file]
        placesk = {}
        for i in places:
            placesk[i] = None
    #print(placesk)
    #placesk é um dicionário com as categorias como chave
    

def request(url):
    response = requests.get(url)
    API_Data = response.json()
    for key in API_Data:
        print(key,":", API_Data[key])    

main()