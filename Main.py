import json
import requests
import sys


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


def pueblos(nombres):
    filename = 'PueblosMagicos.txt'

    # Using the newer with construct to close the file automatically.
    with open(filename) as f:
        data = f.readlines()

    for place in data:
        nombres.append(place.rstrip())


if __name__ == '__main__':
    from pprint import pprint

    # Crea arreglo con los pueblos del archivo txt
    magic = []
    pueblos(magic)
    # Llave para usar el API
    api_key = 'AIzaSyCyrjA1EaA9aknTz2mDabiR_bC4jNprzog'

    # URL del Google Distance Matrix
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    # Google Distance Matrix domain-specific terms: origins and destinations
    origins = []
    destinations = []
    for i in range(1):
        for j in range(100):
            destinations.append(magic[j])
        origins.append(magic[i])
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
            x = json.loads(r.text)
            print(x)

            for isrc, src in enumerate(x['origin_addresses']):
                for idst, dst in enumerate(x['destination_addresses']):
                    print("Hello")

            with open('resultados.json', 'w') as f:
                f.write(r.text)

            G1 = {  # Rosen, Figura 4 (pp. 559)
                'a': [('b', 4), ('c', 2)],
                'b': [('a', 4), ('c', 1), ('d', 5)],
                'c': [('a', 2), ('b', 1), ('d', 8), ('e', 10)],
                'd': [('b', 5), ('c', 8), ('e', 2), ('z', 6)],
                'e': [('c', 10), ('d', 2), ('z', 3)],
                'z': [('d', 6), ('e', 3)],
            }

            G2 = {  # Rosen, Ej. 8.6-2 (pp. 562)
                'a': [('b', 2), ('c', 3)],
                'b': [('a', 2), ('d', 5), ('e', 2)],
                'c': [('a', 3), ('e', 5)],
                'd': [('b', 5), ('e', 1), ('z', 2)],
                'e': [('b', 2), ('c', 5), ('d', 1), ('z', 4)],
                'z': [('d', 2), ('e', 4)],
            }

            w, p = dijkstra(G1, 'a', 'z')
            pprint(p)
            pprint(w)

            w, p = dijkstra(G2, 'a', 'z')
            pprint(p)
            pprint(w)

        except ValueError:
            print("Error while parsing JSON respone, program KILLED")


'''
    La información del API se encuentra en el siguiente link:
        https://developers.google.com/maps/documentation/distance-matrix/usage-limits
'''