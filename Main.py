import json
import requests
import sys
import time


def pueblos(nombres):
    filename = 'PueblosMagicosRes.txt'

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

    for i in range(len(magic)):
        origins.append(magic[i])
        destinations.append(magic[i])

    payload = {
        'origins': '|'.join(origins),
        'destinations': '|'.join(destinations),
        'mode': 'driving',
        'api_key': api_key
    }

    # Assemble the URL and query the web service
    r = requests.get(base_url, params=payload)

    # Checa el codigo regresado por el servidor HTTP. Sólo funciona con código 200
    if r.status_code != 200:
        print('HTTP status code {} received, program terminated.'.format(r.status_code))
    else:
        try:
            a = r.text
            x = json.loads(a)

            print(str(x) + '\n')

            with open('resultados.json', 'w') as f:
                f.write(a)

        except ValueError:
            print("Error while parsing JSON respone, program KILLED")

    '''
    for isrc, src in enumerate(x['origin_addresses']):
        for idst, dst in enumerate(x['destination_addresses']):
            lugar.append(dst)
            row = x['rows'][isrc]
            cell = row['elements'][idst]
            z = cell['distance']['value']
            tiempo.append(z)
    '''

    places = {
        x['origin_addresses'][0]: [(x['origin_addresses'][1], x['rows'][0]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][0]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][0]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][0]['elements'][4]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][0]['elements'][5]['distance']['value']),
                                   (x['origin_addresses'][6], x['rows'][0]['elements'][6]['distance']['value']),
                                   (x['origin_addresses'][7], x['rows'][0]['elements'][7]['distance']['value'])],

        x['origin_addresses'][1]: [(x['origin_addresses'][0], x['rows'][1]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][1]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][1]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][1]['elements'][4]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][1]['elements'][5]['distance']['value']),
                                   (x['origin_addresses'][6], x['rows'][1]['elements'][6]['distance']['value']),
                                   (x['origin_addresses'][7], x['rows'][1]['elements'][7]['distance']['value'])],

        x['origin_addresses'][2]: [(x['origin_addresses'][0], x['rows'][2]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][1], x['rows'][2]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][2]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][2]['elements'][4]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][2]['elements'][5]['distance']['value']),
                                   (x['origin_addresses'][6], x['rows'][2]['elements'][6]['distance']['value']),
                                   (x['origin_addresses'][7], x['rows'][2]['elements'][7]['distance']['value'])],

        x['origin_addresses'][3]: [(x['origin_addresses'][0], x['rows'][3]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][1], x['rows'][3]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][3]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][3]['elements'][4]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][3]['elements'][5]['distance']['value']),
                                   (x['origin_addresses'][6], x['rows'][3]['elements'][6]['distance']['value']),
                                   (x['origin_addresses'][7], x['rows'][3]['elements'][7]['distance']['value'])],

        x['origin_addresses'][4]: [(x['origin_addresses'][0], x['rows'][4]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][1], x['rows'][4]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][4]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][4]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][4]['elements'][5]['distance']['value']),
                                   (x['origin_addresses'][6], x['rows'][4]['elements'][6]['distance']['value']),
                                   (x['origin_addresses'][7], x['rows'][4]['elements'][7]['distance']['value'])],

        x['origin_addresses'][5]: [(x['origin_addresses'][0], x['rows'][5]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][1], x['rows'][5]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][5]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][5]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][5]['elements'][4]['distance']['value']),
                                   (x['origin_addresses'][6], x['rows'][5]['elements'][6]['distance']['value']),
                                   (x['origin_addresses'][7], x['rows'][5]['elements'][7]['distance']['value'])],

        x['origin_addresses'][6]: [(x['origin_addresses'][0], x['rows'][6]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][1], x['rows'][6]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][6]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][6]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][6]['elements'][4]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][6]['elements'][5]['distance']['value']),
                                   (x['origin_addresses'][7], x['rows'][6]['elements'][7]['distance']['value'])],

        x['origin_addresses'][7]: [(x['origin_addresses'][0], x['rows'][7]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][1], x['rows'][7]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][7]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][7]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][7]['elements'][4]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][7]['elements'][5]['distance']['value']),
                                   (x['origin_addresses'][6], x['rows'][7]['elements'][6]['distance']['value'])],
    }

    w, p = dijkstra(places, x['origin_addresses'][0], x['origin_addresses'][7])
    pprint(p)
    pprint(w)


def dijkstra(G, a, z):
    """
    Algoritmo de Dijkstra
    Determina el camino mas corto entre los vertices 'a' y 'z' de un
    grafo ponderado y conexo 'G'.
    https://developers.google.com/maps/documentation/distance-matrix/get-api-key
    """
    assert a in G
    assert z in G

    # Definicion de infinito como un valor mayor
    # al doble de suma de todos los pesos
    Inf = 0
    for u in G:
        for v, w in G[u]:
            Inf += w

    # Inicializacion de estructuras auxiliares:
    #  L: diccionario vertice -> etiqueta
    #  S: conjunto de vertices con etiquetas temporales
    #  A: vertice -> vertice previo (en camino longitud minima)
    L = dict([(u, Inf) for u in G])  # py3: L = {u:Inf for u in G}
    L[a] = 0
    S = set([u for u in G])  # py3: S = {u for u in G}
    A = {}

    # Funcion auxiliar, dado un vertice retorna su etiqueta
    # se utiliza para encontrar el vertice the etiqueta minima
    def W(v):
        return L[v]

    # Iteracion principal del algoritmo de Dijkstra
    while z in S:
        u = min(S, key=W)
        S.discard(u)
        for v, w in G[u]:
            if v in S:
                if L[u] + w < L[v]:
                    L[v] = L[u] + w
                    A[v] = u

    # Reconstruccion del camino de longitud minima
    P = []
    u = z
    while u != a:
        P.append(u)
        u = A[u]
    P.append('a')
    P.reverse()

    # retorna longitud minima y camino de longitud minima
    return L[z], P


if __name__ == '__main__':
    from pprint import pprint

    api()

'''
    - Sólo ocupar 10 nodos/pueblos
    -
'''

'''
    G1 = {  # Rosen, Figura 4 (pp. 559)
        'a': [('b', 4), ('c', 2)],
        'b': [('a', 4), ('c', 1), ('d', 5)],
        'c': [('a', 2), ('b', 1), ('d', 8), ('e', 10)],
        'd': [('b', 5), ('c', 8), ('e', 2), ('z', 6)],
        'e': [('c', 10), ('d', 2), ('z', 3)],
        'z': [('d', 6), ('e', 3)],
    }

    w, p = dijkstra(G1, 'a', 'z')
    pprint(p)
    pprint(w)
'''


