#!/usr/bin/env python3

import os
from PIL import Image

path = os.path.join(os.path.expanduser("~"), "supplier-data/images")

os.makedirs(path, exist_ok=True)

for image in os.listdir(path):
    if image.startswith("."):
        continue
    if not image.endswith(".tiff"):
        continue
    
    ruta = os.path.join(path, image)
    if not os.path.isfile(ruta):
        continue
    
    base, _ = os.path.splitext(image)
    new_name = os.path.join(path, base + ".jpeg")

    with Image.open(ruta) as img:
        img = img.convert("RGB")
        img = img.resize((600, 400))
        img.save(new_name, format="JPEG")