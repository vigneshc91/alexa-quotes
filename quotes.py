import requests

class Quotes:
    URL = AppConstants.URL

    def info(self):
        req = requests.get(url=self.URL)
        data = req.json()
        return data