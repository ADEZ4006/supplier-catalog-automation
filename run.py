import os
import requests

basepath = os.path.join(os.path.expanduser("~"), "supplier-data/descriptions")
folder = os.listdir(basepath)
data = []

for file in folder:
    ruta = os.path.join(basepath, file)
    with open(ruta, "r") as f:
        data.append({
            "name": f.readline().strip(),
            "weight": int(f.readline().strip().replace("lbs", "")),
            "description": f.read().strip(),
            "image_name": file.replace(".txt", ".jpeg")
        })

for item in data:
    resp = requests.post("http://localhost/fruits/", data=item)
    print(resp.status_code)