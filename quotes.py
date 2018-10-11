import requests
from constants import AppConstants

class Quotes:
    URL = AppConstants.URL

    def info(self):
        req = requests.get(url=self.URL)
        data = req.json()
        return data