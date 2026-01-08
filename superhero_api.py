import requests

class SuperHeroAPIService:
    BASE_URL = "https://superheroapi.com/api"

    def __init__(self, token):
        self.token = token

    def search(self, hero_name):
        url = f"{self.BASE_URL}/{self.token}/search/{hero_name}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        if data.get("response") == "success":
            return data["results"]
        return []

    @staticmethod
    def filter_by_publisher(results, publisher):
        return [
            hero for hero in results
            if hero["biography"].get("publisher") == publisher
        ]
