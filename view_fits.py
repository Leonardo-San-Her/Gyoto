#!/usr/bin/env python3
import sys
import os
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Nombre del archivo .fits a visualizar
fname = sys.argv[1] if len(sys.argv) > 1 else "fixedstar.fits"

# Leer FITS
hdul = fits.open(fname)
img = np.squeeze(hdul[0].data)

# Evitar problemas con valores <= 0
img = img.astype(float)
img[img <= 0] = np.nan

# Colormap bonito
cmap = plt.cm.inferno.copy()
cmap.set_bad("black")

mx = np.nanmax(img)
vmin = mx * 1e-4  # Ajusta a 1e-3, 1e-5, etc.

plt.figure(figsize=(6, 6))
plt.imshow(img, origin="lower", cmap=cmap,
           norm=LogNorm(vmin=vmin, vmax=mx))
plt.colorbar(label="Intensity")
plt.title(fname)
plt.tight_layout()

# Nombre del PNG de salida
png_name = os.path.splitext(fname)[0] + ".png"
plt.savefig(png_name, dpi=150)
print(f"Imagen guardada en: {png_name}")
