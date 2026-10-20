#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"
path = os.path.join(os.path.expanduser("~"), "supplier-data/images")

for archive in os.listdir(path):
    ruta = os.path.join(path, archive)
    if not os.path.isfile(ruta):
        continue
    if not archive.endswith(".jpeg"):
        continue
    with open(ruta, "rb") as opened:
        r = requests.post(url, files={"file": opened})