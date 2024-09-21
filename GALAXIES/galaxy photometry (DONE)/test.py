from astropy.io import fits
import matplotlib.pyplot as plt
from photutils.isophote import EllipseGeometry, Ellipse
from photutils.aperture import EllipticalAperture
import numpy as np

# Open the FITS file
hdul = fits.open('NGC_1199.fits')
data = hdul[0].data
hdul.info()

# Display the image
plt.imshow(data, cmap='gray', origin='lower')
plt.colorbar()
plt.title('Galaxy FITS Image')
plt.show()

# Define the geometry of the ellipse
x0, y0 = 124, 124
geometry = EllipseGeometry(x0=x0, y0=y0, sma=15, eps=0.5, pa=-35.0 * np.pi / 180.0)
aper = EllipticalAperture((geometry.x0, geometry.y0), geometry.sma, geometry.sma * (1 - geometry.eps), geometry.pa)

# Display the image with the aperture
plt.imshow(data, cmap='gray', origin='lower')
aper.plot(color='red')
plt.title('Galaxy with Elliptical Aperture')
plt.show()

# Fit the ellipse
ellipse = Ellipse(data, geometry)
isolist = ellipse.fit_image()

# Extract data for plotting
sma = isolist.sma
intensity = isolist.intens
eps = isolist.eps
pa = isolist.pa
x0_list = isolist.x0
y0_list = isolist.y0

# Normalize the intensity (surface brightness)
#ormalized_intensity = intensity / np.max(intensity)

# Plot length along semi-major axis vs. normalized intensity
#plt.figure()
#plt.plot(sma, normalized_intensity)
#plt.xlabel('Semi-major axis length (pixels)')
#plt.ylabel('Normalized Intensity')
#plt.title('Surface Brightness Profile')
#plt.show()

# Plot ellipticity as a function of distance from the galaxy center
plt.figure()
plt.scatter(sma, eps)
plt.xlabel('Semi-major axis length (pixels)')
plt.ylabel('Ellipticity')
plt.title('Ellipticity vs. Semi-major Axis Length')
plt.show()

# Plot position angle as a function of distance from the galaxy center
plt.figure()
plt.scatter(sma, np.rad2deg(pa))
plt.xlabel('Semi-major axis length (pixels)')
plt.ylabel('Position Angle (degrees)')
plt.title('Position Angle vs. Semi-major Axis Length')
plt.show()

# Plot x0 vs semi-major axis length
plt.figure()
plt.scatter(sma, x0_list)
plt.xlabel('Semi-major axis length (pixels)')
plt.ylabel('x0 (pixels)')
plt.title('x0 vs. Semi-major Axis Length')
plt.show()

# Plot y0 vs semi-major axis length
plt.figure()
plt.scatter(sma, y0_list)
plt.xlabel('Semi-major axis length (pixels)')
plt.ylabel('y0 (pixels)')
plt.title('y0 vs. Semi-major Axis Length')
plt.show()

# List the geometric parameters used
print(f"Central coordinates: ({x0}, {y0})")
print(f"Semi-major axis length: {geometry.sma}")
print(f"Ellipticity: {geometry.eps}")
print(f"Position angle: {np.rad2deg(geometry.pa)} degrees")
