import requests

class APIClient:
    def __init__(self,base_url):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}", timeout=60)
    
    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=60
        )