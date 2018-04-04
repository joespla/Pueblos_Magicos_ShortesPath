import json
import requests
import sys

if __name__ == '__main__':

    api_key = 'AIzaSyC84VZ_TRi70AwO6UAd6tSfKYktqhmaymc'

    # Google Distance Matrix base URL to which all other parameters are attached
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    # Google Distance Matrix domain-specific terms: origins and destinations
    origins = ['Tecate, Baja California']
    destinations = ['Metepec, Estado de mexico', 'Sombrerete, Zacatecas']
    payload = {
        'origins': '|'.join(origins),
        'destinations': '|'.join(destinations),
        'mode': 'driving',
        'api_key': api_key
    }

    # Assemble the URL and query the web service
    r = requests.get(base_url, params=payload)

    # Check the HTTP status code returned by the server. Only process the response,
    # if the status code is 200 (OK in HTTP terms).
    if r.status_code != 200:
        print('HTTP status code {} received, program terminated.'.format(r.status_code))
    else:
        try:

            x = json.loads(r.text)
            print(x)
            for isrc, src in enumerate(x['origin_addresses']):
                for idst, dst in enumerate(x['destination_addresses']):
                    row = x['rows'][isrc]
                    cell = row['elements'][idst]
                    if cell['status'] == 'OK':
                        print('{} to {}: {}, {}.'.format(src, dst, cell['distance']['text'], cell['duration']['text']))
                    else:
                        print('{} to {}: status = {}'.format(src, dst, cell['status']))

            with open('resultados.json', 'w') as f:
                f.write(r.text)


        except ValueError:
            print('Error while parsing JSON response, program terminated.')

    # Prepare for debugging, but only if interactive. Now you can pprint(x), for example.
    if sys.flags.interactive:
        from pprint import pprint
