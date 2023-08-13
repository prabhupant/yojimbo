import requests

from yojimbo.main import app

# app.run(debug=True, port=8712)


class CoolService:

    def __init__(self, base_url: str = "http://localhost:8712"):
        self.url = base_url + "/askai/api/v1/get-pulse-summaries/1"


    def get_data(self):
        response = requests.get(self.url)

        if response.ok:
            return {"data": "cool data"}
        return {"data": "not so cool data"}


def some_good_function():

    cool_service = CoolService()

    data = cool_service.get_data()

    return data


def test_of_some_good_function():
    response = some_good_function()

    assert response == {"data": "cool data"}
    print("asserted successfully")


if __name__ == "__main__":
    test_of_some_good_function()