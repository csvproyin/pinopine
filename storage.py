import json
import os


def load_data(filename):

    if not os.path.exists(filename):

        with open(filename, "w") as f:
            json.dump({}, f)

    with open(filename, "r") as f:
        return json.load(f)


def save_data(filename, data):

    with open(filename, "w") as f:
        json.dump(data, f)