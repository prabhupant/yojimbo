import subprocess

from flask import Flask, request
from yojimbo import config
from yojimbo.stubber import Stubber

app = Flask(__name__)


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


def run_yojimbo():
    flask_process = subprocess.Popen(["python", "flask_app.py"])

    # Perform other test-related activities
    print("Running tests...")

    # Terminate the Flask app process after tests are done
    flask_process.terminate()
    flask_process.wait()


if __name__ == '__main__':
    app.run(debug=True, port=config.YOJIMNO_PORT)