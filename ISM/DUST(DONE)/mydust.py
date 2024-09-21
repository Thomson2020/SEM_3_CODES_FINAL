import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np
import astropy.units as u
from astropy.table import Table
from synphot import units, config
from synphot import SourceSpectrum,SpectralElement,Observation,ExtinctionModel1D
from synphot.models import BlackBodyNorm1D
from synphot.spectrum import BaseUnitlessSpectrum
from synphot.reddening import ExtinctionCurve
from astroquery.simbad import Simbad
from astroquery.mast import Observations
import astropy.visualization
from dust_extinction.parameter_averages import CCM89, F99,G23


ext = CCM89(Rv=3.1)


with fits.open('AV69.fits') as hdul:
    hdul.info()  # Display the structure of the FITS file
    primary_hdu = hdul[0]
    data = primary_hdu.data

t_lwr = Table.read('AV69.fits')
wavelengths = t_lwr['WAVELENGTH'][0]* u.AA  # Assuming wavelength is in Angstroms
spectrum = t_lwr['FLUX'][0] * (u.erg / (u.s * u.cm**2 * u.AA))  # Assuming flux units

spectrum_ext = spectrum * ext.extinguish(wavelengths, Ebv=0.4)

spectrum_noext = spectrum_ext / ext.extinguish(wavelengths, Av=1.55)
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(wavelengths, spectrum, label='Original Spectrum', linewidth=2)
ax.plot(wavelengths, spectrum_ext, label='Reddened Spectrum')
ax.plot(wavelengths, spectrum_noext, 'k', label='De-reddened Spectrum')

# Set labels and scales
ax.set_xlabel('$\lambda$ [{}]'.format(wavelengths.unit))
ax.set_ylabel('Flux [{}]'.format(spectrum.unit))
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(loc='best')
plt.tight_layout()
plt.show()