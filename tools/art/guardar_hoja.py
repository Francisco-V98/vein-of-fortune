#!/usr/bin/env python3
"""Descarga una imagen generada y la guarda como WebP ligero en studio/assets-ref/.

Uso:
    python3 tools/art/guardar_hoja.py <url> <destino sin extensión>
Ejemplo:
    python3 tools/art/guardar_hoja.py https://.../hoja.png personajes/reme/modelo

Guarda studio/assets-ref/personajes/reme/modelo.webp (calidad 92, unos 400 KB por
hoja de 2688 px en lugar de unos 4 MB en PNG). Requiere Pillow.
"""
import io
import pathlib
import sys
import urllib.request

from PIL import Image

ASSETS = pathlib.Path(__file__).resolve().parents[2] / "studio" / "assets-ref"


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    url, dest = argv[1], argv[2]
    out = ASSETS / (dest + ".webp")
    out.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as resp:  # noqa: S310 (la URL la entrega el servicio de imágenes)
        data = resp.read()
    Image.open(io.BytesIO(data)).convert("RGB").save(out, "WEBP", quality=92, method=6)
    print("%s (%d KB)" % (out.relative_to(ASSETS.parent.parent), out.stat().st_size // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
