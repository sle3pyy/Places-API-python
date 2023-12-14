import requests

def link(coordenadas,raiom,atraçõeslista,limit):
    url="https://api.geoapify.com/v2/places"
    apiKey="&apiKey=048fde22cdb44f41963fb00652ca6298"
    limit = str(limit)
    url1=url +"?categories=" + atraçõeslista +"&filter=circle:"+coordenadas[0]+","+coordenadas[1]+","+raiom+ "&bias=proximity:" + coordenadas[0]+","+coordenadas[1]+ "&limit="+ limit + apiKey
    return url1
    #Função que cria e retorna o url da API
    
def request(url):
    response = requests.get(url)
    API_Data = response.json()
    return API_Data 
    #função que vai buscar os dados da API e retorna para o main       

def info(APIdata, limit, atraçõesList):
    placesk = {}
    limit=len(APIdata["features"])
    placeNum = 0
    distance = 0
    for i in range(limit):
        a=APIdata["features"][i]["properties"]
        try:
            print((len(a["name"])+2)*"-")
            print(a["name"],":")                
            placesk[a["name"]]={}
            placesk[a["name"]]["country"]=a["country"]
            placesk[a["name"]]["city"]=a["city"]
            placesk[a["name"]]["postcode"]=a["postcode"]
            placesk[a["name"]]["street"]=a["street"]
            placesk[a["name"]]["distance"]=str(int(a["distance"])/1000)+" kms"
            placesk[a["name"]]["lon"]=a["lon"]
            placesk[a["name"]]["lat"]=a["lat"]
            placesk[a["name"]]["categories"]=a["categories"]
            distance = distance + a["distance"]
            placeNum+=1
            placesk[a["name"]]["phone"]=a["datasource"]["raw"]["phone"]
        except:
           bug=0
        try:
            for i in placesk[a["name"]]:
                print(i,":",placesk[a["name"]][i])
        except:
            bug=0       
    return distance, placeNum
    #função que vai buscar os dados que queremos da API e retorna para o main

def main():
    localização=input("Insira a sua posição em latitude e longitude separados por virgula: ")
    #localização="-8.6471993,40.6476206"
    coordenadas=localização.split(",")
    raio=float(input("Quão longe quer viajar em kms: "))
    #raio=5000
    raiom=str(raio*1000)
    distance=0
    limit=int(input("Insira qual o número máximo de lugares que quer ver: "))
    #limit = 10
    #atrações=input("Insira as suas atrações desejadas separados por virgula, sem espaços: ")
    atrações = "pet,accommodation"
    atraçõesList=atrações.split(",")
    apil=link(coordenadas,raiom,atrações,limit)
    APIdata=request(apil)
    #with open(r"categories.txt") as file:
        #places = [file.readline()[:-1] for line in file]
    distance, placeNum = info(APIdata, limit, atraçõesList)

    medium_distance = distance / placeNum            
    #print(placesk)
    print("\n")
    print("Distancia média:",medium_distance/1000,"kms")
    print("número de lugares encontrados:", placeNum)
    #placesk é um dicionário com as categorias como chave
main()