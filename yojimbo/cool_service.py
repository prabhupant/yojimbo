import requests


class CoolService:

    def __init__(self, base_url: str = "http://localhost:8712"):
        self.url = base_url + "/getCoolData"

    def get_data(self):
        response = requests.get(self.url)

        print("in get data ", response)

        if response.ok:
            return {"data": "cool data"}
        return {"data": "not so cool data"}

    def some_good_function(self):
        data = self.get_data()
        print(f"data in some_good_function - {data}")
        return data

    def math(self):
        return 2 + 2
