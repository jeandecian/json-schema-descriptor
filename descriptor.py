from json import load
from requests import get
from sys import argv

source = argv[1]

print(source)

if "http" in source:
    data = get(source).json()
elif ".json" in source:
    data = load(open(source))

print(data)
