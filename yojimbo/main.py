import subprocess
from typing import Optional

from flask import Flask, request
from yojimbo import config
from yojimbo.stubber import Stubber
import threading
from flask_socketio import SocketIO

import logging

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)
socketio = SocketIO(app)

# Global variable to store the thread reference
yojimbo_thread: Optional[threading.Thread] = None


@app.route(
    "/",
    defaults={"path": ""},
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
)
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
def generic_endpoint(path):
    # Log the request details or perform any desired processing
    request_details = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "data": request.get_data().decode("utf-8"),
    }

    # You can now use request_details as needed
    # For example, you can log it or process the data in some way
    stubber = Stubber("/Users/batman/work/yojimbo/yojimbo/stubs.json")
    response = stubber.get_stub(extract_stub_url(request.url))

    return response["body"]


def extract_stub_url(path: str):
    # Extract the URL from the request
    port_index = path.index(str(config.YOJIMBO_PORT)) + len(str(config.YOJIMBO_PORT))
    return path[port_index:]


def start_yojimbo():
    socketio.run(app, allow_unsafe_werkzeug=True, port=config.YOJIMBO_PORT)


@socketio.on("message")
def handle_message(message):
    print("Received message:", message)
    socketio.emit("message", message)


def run_yojimbo():
    global yojimbo_thread
    print("Running Yojimbo")
    yojimbo_thread = threading.Thread(target=start_yojimbo)
    yojimbo_thread.start()


def stop_yojimbo():
    global yojimbo_thread
    print("Stopping Yojimbo")
    if yojimbo_thread and yojimbo_thread.is_alive():
        socketio.emit("shutdown", namespace="/")
        yojimbo_thread.join(timeout=5)


#
# if __name__ == '__main__':
#     run_yojimbo()
