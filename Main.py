import json
import requests


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

    r = requests.get(base_url, params=payload)

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


    places = {
        x['origin_addresses'][0]: [(x['origin_addresses'][1], x['rows'][0]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][0]['elements'][2]['distance']['value'])],

        x['origin_addresses'][1]: [(x['origin_addresses'][0], x['rows'][1]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][1]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][1]['elements'][3]['distance']['value'])],

        x['origin_addresses'][2]: [(x['origin_addresses'][0], x['rows'][2]['elements'][0]['distance']['value']),
                                   (x['origin_addresses'][1], x['rows'][2]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][2]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][2]['elements'][4]['distance']['value'])],

        x['origin_addresses'][3]: [(x['origin_addresses'][1], x['rows'][3]['elements'][1]['distance']['value']),
                                   (x['origin_addresses'][2], x['rows'][3]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][3]['elements'][4]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][3]['elements'][5]['distance']['value'])],

        x['origin_addresses'][4]: [(x['origin_addresses'][2], x['rows'][4]['elements'][2]['distance']['value']),
                                   (x['origin_addresses'][3], x['rows'][4]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][5], x['rows'][4]['elements'][5]['distance']['value'])],

        x['origin_addresses'][5]: [(x['origin_addresses'][3], x['rows'][5]['elements'][3]['distance']['value']),
                                   (x['origin_addresses'][4], x['rows'][5]['elements'][4]['distance']['value'])],
    }

    w, p = dijkstra(places, x['origin_addresses'][0], x['origin_addresses'][5])
    pprint("El camino más corto es " + str(p))
    pprint("Con una distancia" + str(w))


def dijkstra(G, a, z):

    assert a in G
    assert z in G

    Inf = 0
    for u in G:
        for v, w in G[u]:
            Inf += w

    L = dict([(u, Inf) for u in G])  # py3: L = {u:Inf for u in G}
    L[a] = 0
    S = set([u for u in G])  # py3: S = {u for u in G}
    A = {}

    def W(v):
        return L[v]

    while z in S:
        u = min(S, key=W)
        S.discard(u)
        for v, w in G[u]:
            if v in S:
                if L[u] + w < L[v]:
                    L[v] = L[u] + w
                    A[v] = u

    P = []
    u = z
    while u != a:
        P.append(u)
        u = A[u]
    P.append(a)
    P.reverse()

    return L[z], P


if __name__ == '__main__':
    from pprint import pprint

    api()

