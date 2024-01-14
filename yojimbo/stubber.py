import json
import os


class Stubber:
    def __init__(self, stub_file: str = "stubs.json"):
        self.stub_file = stub_file
        self.stubs: dict = {}

        assert os.path.exists(stub_file), f"The file '{stub_file}' does not exist."

        self.read_stubs()

    def read_stubs(self):
        with open(self.stub_file, "r") as f:
            self.stubs = json.loads(f.read())

    def get_stub(self, url):
        for stub in self.stubs["mappings"]:
            if stub["request"]["url"] == url:
                return stub["response"]
