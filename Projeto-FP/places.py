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

def info(APIdata, filtro):
    placesk = {}
    placeNum = 0
    distance = 0
    
    #ciclo que vai buscar os dados que queremos da API e coloca num dicionario, parando quando não encontra os dados necessarios
    for i in range(len(APIdata["features"])):
        a=APIdata["features"][i]["properties"]
        try:            
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
        
        #remove os lugares que não tem o necessário para os filtros funcionarem
        try:
            bug=(placesk[a["name"]])
            try:
                bug=(placesk[a["name"]]["distance"])
                bug=(placesk[a["name"]]["categories"])
            except:
                placesk.pop(a["name"], None)  
        except:
            bug=0           
                
    #manda os dados recolhidos para a filtrar e retorna o numero de lugares encontrados e a distancia total
    filtrar(placesk, filtro)
    return distance, placeNum
   
    
    
def filtrar(placesk, filtro):
    #função que procura dentro do dicionario placesk o primeiro a chave que é cada nome da atração e depois analisa o dicionario do valor de cada chave e escolhe o valor para ordenar
    if filtro=="1":
        #neste bastou analisar a primeira chave
        listaAlfabetica = sorted(placesk.items(), key=lambda x: x[0])
        dicAlfabetico = dict(listaAlfabetica)
        for key, dados in dicAlfabetico.items():
            print(f'{key}:')
            for key2, valor in dados.items():
                print(f'{key2}: {valor}')
            print("\n")    
            
    elif filtro=="2":
        #a partir deste vou preciso analisar o que estava no segundo dicionario para ordenar corretamente
        listaDistanciaMenor = sorted(placesk.items(), key=lambda x: float(x[1]['distance'].split(' ')[0]))#tem split porque é um testo com numeros e "kms"
        dicDistanciaMenor = dict(listaDistanciaMenor)
        for key, dados in dicDistanciaMenor.items():
            print(f'{key}:')
            for key2, valor in dados.items():
                print(f'{key2}: {valor}')
            print("\n")         

    elif filtro=="3":
        listaDistanciaMaior = sorted(placesk.items(), key=lambda x: float(x[1]['distance'].split(' ')[0]), reverse=True)
        dicDistanciaMaior = dict(listaDistanciaMaior)
        for key, dados in dicDistanciaMaior.items():
            print(f'{key}:')
            for key2, valor in dados.items():
                print(f'{key2}: {valor}')
            print("\n")
    elif filtro=="4":
        listaNumCategoriasMenor = sorted(placesk.items(), key=lambda x: len(x[1]['categories']))
        dicCategoriasMenor = dict(listaNumCategoriasMenor)
        for key, dados in dicCategoriasMenor.items():
            print(f'{key}:')
            for key2, valor in dados.items():
                print(f'{key2}: {valor}')
            print("\n")
    elif filtro=="5":
        listaNumCategoriasMaior = sorted(placesk.items(), key=lambda x: len(x[1]['categories']), reverse=True)
        dicCategoriasMaior = dict(listaNumCategoriasMaior)
        for key, dados in dicCategoriasMaior.items():
            print(f'{key}:')
            for key2, valor in dados.items():
                print(f'{key2}: {valor}')
            print("\n")
            
            
def main(filtro):

    #input do utilizador:
    #localização=input("Insira a sua posição em latitude e longitude separados por virgula: ")
    localização="20,54"
    coordenadas=localização.split(",")
    #raio=float(input("Quão longe quer viajar em kms: "))
    raio=5000
    raiom=str(raio*1000)
    distance=0
    #limit=int(input("Insira qual o número máximo de lugares que quer ver: "))
    limit = 10
    #atrações=input("Insira as suas atrações desejadas separados por virgula, sem espaços: ")
    atrações = "pet,bingus,accommodation,caralho,yeet,commercial,food,drikn"
    atraçõesList=atrações.split(",")
    
    #criação de uma lista com as categorias existentes para comparação:
    with open(r"categories.txt") as file:
        places = [line[:-1] for line in file]
    #comparação entre a lista de categorias e a lista de categorias inseridas pelo utilizador para eliminar as categorias que não existem:    
    for i in range(len(atraçõesList)-1, -1, -1): 
        if atraçõesList[i] not in places:
            atraçõesList.pop(i)
            atrações=",".join(atraçõesList)

    #criação do url, pedido dos dados e filtragem dos dados:
    apil=link(coordenadas,raiom,atrações,limit)
    APIdata=request(apil)
    distance, placeNum = info(APIdata, filtro)
    
    if placeNum == 0:
        print("Não foi encontrado nada nestas condições")
    else:
        medium_distance = distance / placeNum            
        print("\n")
        print("Distancia média:",medium_distance/1000,"kms")
        print("número de lugares encontrados:", placeNum)
        
        
def menu():
    print("Bem-vindo a pesquisa das suas atrações favoritas")
    print("Opções")
    print("1-Ordenar por ordem alfabética")
    print("2-Ordenar por distância crescente")
    print("3-Ordenar por distância decrescente")
    print("4-Ordenar por número de categorias, crescente")
    print("5-Ordenar por número de categorias, decrescente")

    filtro=input("Escolha o filtro: ")
    if filtro in ("1", "2", "3", "4", "5"):
        main(filtro)
    else:
        print("Valor inválido")
        menu()

menu()