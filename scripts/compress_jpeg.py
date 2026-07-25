# This script is used to change the quality level of all jpegs in a folder

from PIL import Image
import os


def compressDir(target_dir, quality):
    cwd = os.getcwd().replace("\\", "/")
    if (cwd.split("/")[-1].lower() != "grants_map" and cwd.split("/")[-1].lower() != "grantsmap"):
        exit("ERROR: This script must be run from the project root directory")

    for filename in os.listdir(target_dir):
        if not filename.lower().endswith(('.jpg', '.jpeg')):
            continue

        input_path = os.path.join(target_dir, filename)
        output_path = os.path.join(target_dir, filename)

        with Image.open(input_path) as img:
            img.save(output_path, "JPEG", quality=quality, optimize=True)
            print(f"Compressed {target_dir}/{filename} to quality {quality}")



# Keep track of quality used for each dir
dirs = [
    # ("images/photobook/japan", 8),
    ("images/", 8),
]

for d, q in dirs:
    compressDir(d, q)