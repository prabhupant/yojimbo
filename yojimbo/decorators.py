# import pytest
from yojimbo.main import start_yojimbo

# socketio_app = socketio.test_client(app)

#
# @pytest.fixture
# def test_client():
#     client = socketio.test_client(socketio_app)
#     yield client
#     client.disconnect()
#

def yojimbo(func):
    """
    Decorator function that intercepts and modifies API calls
    """

    def wrapper(*args, **kwargs):
        start_yojimbo()

        try:
            # Pass the test client to the decorated function
            result = func(*args, **kwargs)
            assert result == {"data": "cool data"}  # Example assertion
            print("Asserted successfully")
        except Exception as e:
            print(f"Error while running the test: {e}")
        finally:
            stop_yojimbo()

    return wrapper
