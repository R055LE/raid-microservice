import requests
import os
# import json

api_key = os.environ.get('APIKEY')

base_uri = 'https://api.marvelstrikeforce.com/game/v1'
path_uri = '/raids'

uri = f'{base_uri}{path_uri}'
headers = {"x-api-key": api_key}

r: dict = requests.get(url=uri, headers=headers).json()
data = r.get('data')

for record in data:
    record: dict
    record_id: str = record.get('id')

    r: dict = requests.get(url=uri + f'/{record_id}', headers=headers).json()
    data: dict = r.get('data')
    print(data.get('name'))

    # Here is where to export the data.
