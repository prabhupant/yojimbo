from yojimbo.decorators import yojimbo
from yojimbo.cool_service import CoolService


@yojimbo
def test_of_some_good_function():
    # with app.test_client() as client
    cool_service = CoolService()
    response = cool_service.some_good_function()

    assert response == {"data": "cool data"}

    print("asserted successfully")


def test_math():
    cool_service = CoolService()
    response = cool_service.math()

    assert response == 4


# if __name__ == "__main__":
#     test_of_some_good_function()
