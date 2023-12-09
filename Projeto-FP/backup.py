import requests

def link(coordenadas,raiom,atraçõeslista):
    url="https://api.geoapify.com/v2/places"
    apiKey="&apiKey=048fde22cdb44f41963fb00652ca6298"
    url1=url +"?categories=" + atraçõeslista +"&filter=circle:"+coordenadas[0]+","+coordenadas[1]+","+raiom+ "&bias=proximity:" + coordenadas[0]+","+coordenadas[1]+ "&limit=10"+apiKey
    print(url1)
    return url1
    #Função que cria e retorna o url da API
    
def request(url):
    response = requests.get(url)
    API_Data = response.json()
    return API_Data 
    #função que vai buscar os dados da API e retorna para o main       

def main():
    #localização=input("Insira a sua posição em latitude e longitude separados por virgula: ")
    localização="-8.6471993,40.6476206"
    coordenadas=localização.split(",")
    #raio=float(input("Quão longe quer viajar em kms: "))
    raio=5000
    raiom=str(raio*1000)
    #limit=input("Insira qual o número máximo de lugares que quer ver: ")
    limit = 10
    #atrações=input("Insira as suas atrações desejadas separados por virgula: ")
    atrações = "education,accommodation.hotel,accommodation"
    atraçõesList=atrações.split(",")
    apil=link(coordenadas,raiom,atrações)
    #pus isto que sao as cenas q temos que pedir a pessoa, btw aqui em baixo pus tmb a cena com o meu categories pq assim tmb consigo ver isso
    APIdata=request(apil)

    #with open(r"C:\Users\Utilizador\Desktop\projeto-FP\Projeto-FP\categories.txt") as file:
        #places = [file.readline()[:-1] for line in file]
    placesk = {}
    for i in range(limit):
        for j in range(len(atraçõesList)):
            if atraçõesList[j] in APIdata["features"][i]["properties"]["categories"]:
                placesk.setdefault(atraçõesList[j], [])
                placesk[atraçõesList[j]].append(APIdata["features"][i]["properties"]["name"])
    print(placesk)
    #placesk é um dicionário com as categorias como chave

main()