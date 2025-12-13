from pathlib import Path
from PIL import Image

SIZE = (256, 256)
SUFFIX = "_thumb"

def make_thumbs(folder: Path):
    for jpg in folder.glob("*.jpg"):
        out = jpg.with_name(f"{jpg.stem}{SUFFIX}{jpg.suffix}")
        with Image.open(jpg) as im:
            im = im.convert("RGB")  # zapewnia zapis do JPEG
            w, h = im.size
            side = min(w, h)
            left = (w - side) // 2
            top = (h - side) // 2
            right = left + side
            bottom = top + side
            cropped = im.crop((left, top, right, bottom))
            thumb = cropped.resize(SIZE, Image.LANCZOS)
            thumb.save(out, "JPEG", quality=90)
        print(f"OK: {jpg.name} -> {out.name}")

if __name__ == "__main__":
    make_thumbs(Path("."))
