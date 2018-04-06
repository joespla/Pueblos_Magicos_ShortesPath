import json
import requests
import sys
import time


def pueblos(nombres):
    filename = 'PueblosMagicos.txt'

    # Using the newer with construct to close the file automatically.
    with open(filename) as f:
        data = f.readlines()

    for place in data:
        nombres.append(place.rstrip())


def api():
    # Crea arreglo con los pueblos del archivo txt
    magic = []
    pueblos(magic)
    # Llave para usar el API
    api_key = 'AIzaSyBJfqJ9hsD4IufN_h8vRcDAevKOc2R12bM'

    # URL del Google Distance Matrix
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    # Google Distance Matrix domain-specific terms: origins and destinations
    origins = []

    destinations = []
    destinations2 = []

    lugar = []
    tiempo = []

    tf = len(tiempo)

    for i in range(1):
        origins.append(magic[i])
    for j in range(1, 101):
        destinations.append(magic[j])
    for k in range(100, 112):
        destinations2.append(magic[k])

    payload = {
        'origins': '|'.join(origins),
        'destinations': '|'.join(destinations),
        'mode': 'driving',
        'api_key': api_key
    }
    payload2 = {
        'origins': '|'.join(origins),
        'destinations': '|'.join(destinations2),
        'mode': 'driving',
        'api_key': api_key
    }

    # Assemble the URL and query the web service
    r = requests.get(base_url, params=payload)
    time.sleep(1)
    s = requests.get(base_url, params=payload2)

    # Checa el codigo regresado por el servidor HTTP. Sólo funciona con código 200
    if r.status_code != 200:
        print('HTTP status code {} received, program terminated.'.format(r.status_code))
    else:
        try:
            a = r.text
            b = s.text
            x = json.loads(a)
            y = json.loads(b)

            print(str(x) + str(y))
            print("\n")

            with open('resultados.json', 'w') as f:
                f.write(a)
                f.write(b)

        except ValueError:
            print("Error while parsing JSON respone, program KILLED")

    for isrc, src in enumerate(x['origin_addresses']):
        for idst, dst in enumerate(x['destination_addresses']):
            lugar.append(dst)
            row = x['rows'][isrc]
            cell = row['elements'][idst]
            z = cell['distance']['value']
            tiempo.append(z)

    chico = tiempo[0]
    orden = []
    while not tiempo:
        for iitem, item in enumerate(tiempo, start=0):
            if item < chico:
                chico = item
                orden.append(iitem)
            if iitem == len(tiempo)-1:
                tiempo.remove(chico)

    for i in range(len(lugar)):
        print(lugar[orden[i]] + "\n")


if __name__ == '__main__':


    api()

'''
    La información del API se encuentra en el siguiente link:
        https://developers.google.com/maps/documentation/distance-matrix/usage-limits
'''
