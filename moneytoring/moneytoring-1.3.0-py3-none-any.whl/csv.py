import sys
import os


def setup_csv(path=None):
    if path is None:
        path = sys.argv[1]
    if not os.path.exists(path):
        raise FileNotFoundError("Path doesn't exist")
    with open(path, "r") as src:
        with open(os.path.join(os.path.dirname(__file__), "transactions.csv"), "w+") as dst:
            data = src.read()
            dst.write(data)
