import requests

def link(coordenadas,raiom,atraçõeslista,limit):
    url="https://api.geoapify.com/v2/places"
    apiKey="&apiKey=048fde22cdb44f41963fb00652ca6298"
    limit = str(limit)
    url1=url +"?categories=" + atraçõeslista +"&filter=circle:"+coordenadas[0]+","+coordenadas[1]+","+raiom+ "&bias=proximity:" + coordenadas[0]+","+coordenadas[1]+ "&limit="+ limit + apiKey
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
    distance=0
    #limit=input("Insira qual o número máximo de lugares que quer ver: ")
    limit = 10
    #atrações=input("Insira as suas atrações desejadas separados por virgula, sem espaços: ")
    atrações = "education,pet,accommodation"
    atraçõesList=atrações.split(",")
    apil=link(coordenadas,raiom,atrações,limit)
    APIdata=request(apil)
    aux=0

    #with open(r"categories.txt") as file:
        #places = [file.readline()[:-1] for line in file]
    placesk = {}
   
    for i in range(limit):
        a=APIdata["features"][i]["properties"]
        for j in range(len(atraçõesList)):
            if atraçõesList[j] in a["categories"]:
                try:
                    placesk.setdefault(atraçõesList[j], [])
                    placesk[atraçõesList[j]].append(a["name"])
                    placesk[atraçõesList[j]].append(a["city"])
                    placesk[atraçõesList[j]].append(a["postcode"])
                    placesk[atraçõesList[j]].append(a["country"])
                    placesk[atraçõesList[j]].append(a["street"])
                    placesk[atraçõesList[j]].append(a["distance"])
                    placesk[atraçõesList[j]].append(a["lon"])
                    placesk[atraçõesList[j]].append(a["lat"])
                    distance = distance + a["distance"]
                    aux+=1
                except:
                    print("bug")
                try:
                    placesk[atraçõesList[j]].append(a["datasource"]["raw"]["phone"])  
                except: 
                    print("idfk")           
                    
    medium_distance = distance / limit            
    print(placesk)
    print("Distancia média:",medium_distance/1000,"kms")
    print("número de lugares encontrados:", aux)
    #placesk é um dicionário com as categorias como chave
main()