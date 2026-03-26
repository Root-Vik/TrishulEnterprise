from rembg import remove
from PIL import Image
import os

images_dir = r"D:\Hrutvik\Learning Projects\Trishul\images"
output_dir = r"D:\Hrutvik\Learning Projects\Trishul\images\nobg"
os.makedirs(output_dir, exist_ok=True)

# Product images to process (skip banners, blueprints, plant shots)
to_process = [
    "Thrust-Bearing1-370x250.jpg",
    "Thrust-Bearing2-370x250.jpg",
    "Thrust-Bearing3-1.jpg",
    "Thrust-Bearing5.jpg",
    "Thrust-Bearing6-1-370x250.jpg",
    "Thrust-Bearing7.jpg",
    "Motor-Pump-Bearing-Bush1.png",
    "Motor-Pump-Bearing-Bush2.png",
    "Motor-Pump-Bearing-Bush3.png",
    "Impeller1.png",
    "Impeller2.png",
    "Impeller3.png",
    "Impeller4.png",
    "Other-Products2-370x250.jpg",
    "Other-Products3.jpg",
    "Other-Products4.jpg",
    "Other-Products5-370x250.jpg",
]

for filename in to_process:
    src = os.path.join(images_dir, filename)
    name = os.path.splitext(filename)[0]
    dst = os.path.join(output_dir, name + ".png")
    print(f"Processing: {filename} ...", end=" ", flush=True)
    try:
        with open(src, "rb") as f:
            inp = f.read()
        out = remove(inp)
        with open(dst, "wb") as f:
            f.write(out)
        print("done")
    except Exception as e:
        print(f"ERROR: {e}")

print("\nAll done.")
