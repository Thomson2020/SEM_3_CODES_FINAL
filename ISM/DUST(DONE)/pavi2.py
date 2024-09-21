import astropy.io.fits as fits
import matplotlib.pyplot as plt
from astroquery.mast import Observations

# Search for HD 147933 in the MAST archive
obs = Observations.query_criteria(target_name='HD 147933', collection='HST')
data_products = Observations.get_product_list(obs[0])
spectrum_files = Observations.get_product_list(data_products)
spectrum_file = spectrum_files[0]

# Download the spectrum
Observations.download_products(data_products[0:1])

# Read the spectrum
with fits.open(spectrum_file) as hdul:
    spectrum_data = hdul[1].data
    wavelengths = spectrum_data['WAVELENGTH']
    fluxes = spectrum_data['FLUX']
    flux_errors = spectrum_data['FLUXERR']

# Plot the original spectrum
plt.figure(figsize=(12, 6))
plt.errorbar(wavelengths, fluxes, yerr=flux_errors, fmt='-', label='Original Spectrum')
plt.xlabel('Wavelength (Å)')
plt.ylabel('Flux')
plt.title('UV Spectrum of HD 147933')
plt.legend()
plt.show()
