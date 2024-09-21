import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np
import astropy.units as u
from astropy.table import Table
from dust_extinction.parameter_averages import CCM89, F99

# Open and read the FITS file
with fits.open('AV69.fits') as hdul:
    hdul.info()  # Display the structure of the FITS file
    primary_hdu = hdul[0]
    data = primary_hdu.data

# Read the table and extract wavelengths and spectrum
t_lwr = Table.read('AV69.fits')
wavelengths = t_lwr['WAVELENGTH'][0] * u.AA  # Assuming wavelength is in Angstroms
spectrum = t_lwr['FLUX'][0] * (u.erg / (u.s * u.cm**2 * u.AA))  # Assuming flux units

# Convert wavelengths from Angstroms to microns
wavelengths_microns = wavelengths.to(u.micron)

# Calculate the corresponding x values (1/micron)
x = 1 / wavelengths_microns

# Filter out the wavelengths that are outside the valid range for the models
valid_range = (x.value >= 0.3) & (x.value <= 10.0)
wavelengths_valid = wavelengths[valid_range]
spectrum_valid = spectrum[valid_range]

# Plotting

# Combined plot for both models
fig_combined, ax_combined = plt.subplots(figsize=(10, 6))

# Plot for CCM89
ext_ccm89 = CCM89(Rv=3.1)
spectrum_ext_ccm89 = spectrum_valid * ext_ccm89.extinguish(wavelengths_valid, Ebv=0.11)
spectrum_noext_ccm89 = spectrum_ext_ccm89 / ext_ccm89.extinguish(wavelengths_valid, Av=1.55)

ax_combined.plot(wavelengths_valid, spectrum_valid, label='Original Spectrum (CCM89)', linewidth=2)
ax_combined.plot(wavelengths_valid, spectrum_ext_ccm89, label='Reddened Spectrum (CCM89)')
ax_combined.plot(wavelengths_valid, spectrum_noext_ccm89, 'k', label='De-reddened Spectrum (CCM89)')

# Plot for F99
ext_f99 = F99(Rv=3.1)
spectrum_ext_f99 = spectrum_valid * ext_f99.extinguish(wavelengths_valid, Ebv=0.11)
spectrum_noext_f99 = spectrum_ext_f99 / ext_f99.extinguish(wavelengths_valid, Av=1.55)

ax_combined.plot(wavelengths_valid, spectrum_ext_f99, '--', label='Reddened Spectrum (F99)')
ax_combined.plot(wavelengths_valid, spectrum_noext_f99, 'r--', label='De-reddened Spectrum (F99)')

# Set labels and scales for combined plot
ax_combined.set_xlabel('$\lambda$ [{}]'.format(wavelengths_valid.unit))
ax_combined.set_ylabel('Flux [{}]'.format(spectrum_valid.unit))
ax_combined.set_xscale('log')
ax_combined.set_yscale('log')
ax_combined.legend(loc='best')
ax_combined.set_title('Combined: CCM89 and F99 Extinction Models')
plt.tight_layout()
plt.show()

# Individual plot for CCM89
fig_ccm89, ax_ccm89 = plt.subplots(figsize=(10, 6))
ax_ccm89.plot(wavelengths_valid, spectrum_valid, label='Original Spectrum', linewidth=2)
ax_ccm89.plot(wavelengths_valid, spectrum_ext_ccm89, label='Reddened Spectrum')
ax_ccm89.plot(wavelengths_valid, spectrum_noext_ccm89, 'k', label='De-reddened Spectrum')

# Set labels and scales for CCM89 plot
ax_ccm89.set_xlabel('$\lambda$ [{}]'.format(wavelengths_valid.unit))
ax_ccm89.set_ylabel('Flux [{}]'.format(spectrum_valid.unit))
ax_ccm89.set_xscale('log')
ax_ccm89.set_yscale('log')
ax_ccm89.legend(loc='best')
ax_ccm89.set_title('CCM89 Extinction Model')
plt.tight_layout()
plt.show()

# Individual plot for F99
fig_f99, ax_f99 = plt.subplots(figsize=(10, 6))
ax_f99.plot(wavelengths_valid, spectrum_valid, label='Original Spectrum', linewidth=2)
ax_f99.plot(wavelengths_valid, spectrum_ext_f99, label='Reddened Spectrum')
ax_f99.plot(wavelengths_valid, spectrum_noext_f99, 'k', label='De-reddened Spectrum')

# Set labels and scales for F99 plot
ax_f99.set_xlabel('$\lambda$ [{}]'.format(wavelengths_valid.unit))
ax_f99.set_ylabel('Flux [{}]'.format(spectrum_valid.unit))
ax_f99.set_xscale('log')
ax_f99.set_yscale('log')
ax_f99.legend(loc='best')
ax_f99.set_title('F99 Extinction Model')
plt.tight_layout()
plt.show()
