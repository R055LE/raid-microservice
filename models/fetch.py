import os
from abc import ABC, abstractmethod

import requests


class Fetch(ABC):
    api_key: str = os.environ.get('APIKEY')
    headers = {"x-api-key": api_key}
    base_uri: str = 'https://api.marvelstrikeforce.com/game/v1'
    path_uri: str = ''

    @abstractmethod
    def get(self):
        """Fetch API Information from Address"""


class RootFetch(Fetch):
    path_uri = '/raids'

    def get(self):
        return requests.get(url=f'{self.base_uri}{self.path_uri}', headers=self.headers).json()

# data = r.get('data')


# for record in data:
#     record: dict
#     record_id: str = record.get('id')

#     r: dict = requests.get(url=uri + f'/{record_id}', headers=headers).json()
#     data: dict = r.get('data')
#     print(data.get('name'))

# Here is where to export the data.
