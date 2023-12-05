import requests

baseUrl="https://api.geoapify.com/v2/places?categories=commercial.supermarket&filter=rect%3A10.716463143326969%2C48.755151258420966%2C10.835314015356737%2C48.680903341613316&limit=20&apiKey=048fde22cdb44f41963fb00652ca6298"

def main():
    with open(r"categories.txt") as f:
        places ={f.readline()[:-1] for i in f}
    print(places)

main()    
#:))))))