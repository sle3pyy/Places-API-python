import requests

baseUrl="https://api.geoapify.com/v2/places?categories=commercial.supermarket&filter=rect%3A10.716463143326969%2C48.755151258420966%2C10.835314015356737%2C48.680903341613316&limit=20&apiKey=048fde22cdb44f41963fb00652ca6298"

def main():
    with open(r"C:\Users\simao\Downloads\Projeto-FP\projeto-FP\Projeto-FP\categories.txt") as file:
        places = [file.readline()[:-1] for line in file]
        placesk = {}
        for i in places:
            placesk[i] = None
    print(placesk)
    #placesk é um dicionário com as categorias como chave

main()