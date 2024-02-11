from json import load
from requests import get
from schema import schema
from sys import argv

source = argv[1]

if "http" in source:
    url = source.split("?")
    schema["source"]["url"]["base"] = url[0]
    if len(url) > 1:
        for param in url[1].split("&"):
            key, value = param.split("=")
            schema["source"]["url"]["params"][key] = value

    schema["source"]["data"] = get(source).json()
elif ".json" in source:
    schema["source"]["file"] = source

    schema["source"]["data"] = load(open(source))

print(schema)
