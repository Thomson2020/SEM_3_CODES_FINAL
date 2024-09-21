import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

# Load the FITS file
file_path = 'J010104-285801.fits'
hdu_list = fits.open(file_path)

# Get information about the FITS file structure
hdu_list.info()

# Extract header and data
header = hdu_list[0].header
data = hdu_list[0].data

# Print header
print(repr(header))

CRPIX1 = 1
CD1_1 = 3.62161104717198E-06
UP_WLSRT = 3283.02131791165
CRVAL1 = 3.51672940407668
num_pixel = data.shape[1]
print("The Number of pixel is:", num_pixel)

flux = data[0]

# Calculate wavelength
wavelength = UP_WLSRT * 10 ** ((np.arange(num_pixel) + 1 - CRPIX1) * CD1_1)
print(wavelength)

plt.figure(figsize=(60,10))
plt.plot(wavelength, flux, color = 'lime')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Flux')
plt.title('J010104-285801')
plt.ylim(-0.5,1.5)
plt.xlim(4320, 4620)

# Calculate redshift
z = (4466 / 1215.67) - 1  # 4466 is observed Lyman-alpha and 1215.67 is rest Lyman wavelength
print("Redshift of J010104-285801:", z)

# Elements showing absorption
elements = {
    'Si II': 1526.70698,
    'Ni II': 1317.217,
    'Fe II': 2382.7641781,
    'Al I': 2367.7750,
    'Cr II': 2056.25693,
    'Ca I': 2276.169
}

# Calculate observed wavelengths for the elements
observed_wavelengths = {element: wl * (1 + z) for element, wl in elements.items()}

# Plot each element's absorption line individually
for element, obs_wl in observed_wavelengths.items():
    # Define a range around the expected wavelength to search for the dip
    range_width = 20  # Width in nm to search for the dip
    range_min = obs_wl - range_width
    range_max = obs_wl + range_width

    # Find the indices corresponding to this range
    range_indices = np.where((wavelength >= range_min) & (wavelength <= range_max))

    # Find the position of the minimum flux value within this range
    dip_index = range_indices[0][np.argmin(flux[range_indices])]
    dip_wavelength = wavelength[dip_index]
    dip_flux = flux[dip_index]

    plt.figure(figsize=(15, 5))
    plt.plot(wavelength, flux, color='lime')
    plt.axvline(x=dip_wavelength, color='red', linestyle='--', 
                label=f'{element}:\nWavelength = {dip_wavelength:.2f} nm\nFlux = {dip_flux:.2f}\nRedshift = {z:.3f}')
    plt.ylim(-0.5, 1.5)
    plt.xlim(dip_wavelength - 5, dip_wavelength + 5)  # Adjust the window around the absorption line
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Flux')
    plt.title(f'Absorption Line of {element}')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

# Close the FITS file
hdu_list.close()
