import subprocess

from flask import Flask, request
from yojimbo import config
from yojimbo.stubber import Stubber
import threading
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def generic_endpoint(path):
    # Log the request details or perform any desired processing
    request_details = {
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
        'data': request.get_data().decode('utf-8')
    }

    # You can now use request_details as needed
    # For example, you can log it or process the data in some way
    stubber = Stubber("/Users/prabhu/personal/yojimbo/yojimbo/stubs.json")
    response = stubber.get_stub(extract_stub_url(request.url))

    return response['body']


def extract_stub_url(path: str):
    # Extract the URL from the request
    port_index = path.index(str(config.YOJIMNO_PORT)) + len(str(config.YOJIMNO_PORT))
    return path[port_index:]


def start_yojimbo():
    # app.run(debug=True, port=config.YOJIMNO_PORT)
    socketio.run(app, allow_unsafe_werkzeug=True, port=config.YOJIMNO_PORT)


def run():
    thread = threading.Thread(target=start_yojimbo)
    thread.start()

    # # Wait for the thread to finish (optional)
    # thread.join()


if __name__ == '__main__':
    run()