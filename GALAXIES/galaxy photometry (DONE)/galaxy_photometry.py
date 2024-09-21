import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from photutils.isophote import Ellipse, EllipseGeometry, build_ellipse_model
from photutils.isophote import EllipseSample, EllipseFitter
from photutils.aperture import EllipticalAperture

hdul = fits.open('NGC_1199.fits')
data = hdul[0].data
hdul.info()
plt.imshow(data, cmap='gray', origin='lower')
plt.colorbar()
plt.title('Galaxy FITS Image')
plt.show()

x0, y0 = 123, 123
geometry = EllipseGeometry(x0=x0, y0=y0, sma=21, eps=0.4, pa=-40.0 * np.pi / 180.0)
aper = EllipticalAperture((geometry.x0, geometry.y0), geometry.sma, geometry.sma * (1 - geometry.eps), geometry.pa)

plt.figure()
plt.imshow(data, cmap='gray', origin='lower')
aper.plot(color='red')
plt.title('Elliptical Aperture')
plt.show()

ellipse = Ellipse(data, geometry)
isolist = ellipse.fit_image()
print(isolist.pa)

iso_table = isolist.to_table()
print(iso_table)

sma = isolist.sma
intensity = isolist.intens
eps = isolist.eps
pa = isolist.pa
x0_list = isolist.x0
y0_list = isolist.y0

norm_intensity = intensity / np.max(intensity)
plt.figure()
plt.plot(sma, norm_intensity, marker='o')
plt.xlabel('Semi-Major Axis Length')
plt.ylabel('Normalized Surface Brightness')
plt.title('Surface Brightness Profile')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 10))
plt.subplots_adjust(hspace=0.35, wspace=0.35)

plt.subplot(2, 2, 1)
plt.errorbar(isolist.sma, isolist.eps, yerr=isolist.ellip_err, fmt='o', markersize=4)
plt.xlabel('Semimajor Axis Length (pix)')
plt.ylabel('Ellipticity')

plt.subplot(2, 2, 2)
plt.errorbar(isolist.sma, isolist.pa / np.pi * 180.0, yerr=isolist.pa_err / np.pi * 180.0, fmt='o', markersize=4)
plt.xlabel('Semimajor Axis Length (pix)')
plt.ylabel('PA (deg)')

plt.subplot(2, 2, 3)
plt.errorbar(isolist.sma, isolist.x0, yerr=isolist.x0_err, fmt='o', markersize=4)
plt.xlabel('Semimajor Axis Length (pix)')
plt.ylabel('x0')

plt.subplot(2, 2, 4)
plt.errorbar(isolist.sma, isolist.y0, yerr=isolist.y0_err, fmt='o', markersize=4)
plt.xlabel('Semimajor Axis Length (pix)')
plt.ylabel('y0')
plt.show()
