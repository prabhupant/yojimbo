import requests

from yojimbo.decorators import yojimbo
from yojimbo.main import socketio


# run()


class CoolService:

    def __init__(self, base_url: str = "http://localhost:8712"):
        self.url = base_url + "/getCoolData"

    def get_data(self):
        response = requests.get(self.url)

        print("in get data ", response)

        if response.ok:
            return {"data": "cool data"}
        return {"data": "not so cool data"}


def some_good_function():

    cool_service = CoolService()

    data = cool_service.get_data()

    return data


@yojimbo
def test_of_some_good_function():
    response = some_good_function()

    assert response == {"data": "cool data"}

    print("asserted successfully")


if __name__ == "__main__":
    test_of_some_good_function()
