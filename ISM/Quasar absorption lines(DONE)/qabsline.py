import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# Function to read FITS file, compute wavelength array, and save spectral data
def process_fits_file(fits_filename, output_data_filename, output_plot_filename):
    # Open the FITS file
    hdu_list = fits.open(fits_filename)

    # Display information about the HDUs
    hdu_list.info()

    # Access the primary HDU
    primary_hdu = hdu_list[0]

    # Get the header and data from the primary HDU
    header = primary_hdu.header
    data = primary_hdu.data

    # Perform the wavelength calibration
    crval1 = header['CRVAL1']  # Central wavelength of the first pixel in log-scale
    crpix1 = header['CRPIX1']  # Reference pixel
    cd1_1 = header['CD1_1']    # Wavelength increment per pixel in log-scale

    # Determine the number of pixels in the data
    num_pixels = data.shape[1]  # Assuming data is 2D, wavelength axis is the second dimension

    # Calculate the wavelength array
    wavelengths = 10 ** (crval1 + ((np.arange(num_pixels) + 1 - crpix1) * cd1_1))

    # Check the dimensions of the array before and after calibration
    print(f"Data shape: {data.shape}")
    print(f"Wavelength shape: {wavelengths.shape}")

    # Normalize the flux data (optional, based on use case)
    normalized_flux = data / np.max(data)

    # Combine the wavelength and normalized flux arrays
    combined_data = np.column_stack((wavelengths, normalized_flux[0]))  # Assuming 1D flux data

    # Save the combined data to a file
    np.savetxt(output_data_filename, combined_data, header='Wavelength Flux', comments='')

    # Plot the spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(wavelengths, normalized_flux[0], label='Spectrum')
    plt.xlabel('Wavelength')
    plt.ylabel('Normalized Flux')
    plt.title('Spectral Data')
    plt.legend()
    plt.grid(True)
    #plt.xlim(4.4, 5.2)  # Set x-axis limits
    #plt.ylim(-0.0002, 0.0006)  # Set y-axis limits
    plt.savefig(output_plot_filename)  # Save the plot to a file
    plt.show()

    # Close the FITS file after use
    hdu_list.close()

# File paths
fits_filename = 'J010104-285801.fits'
output_data_filename = 'spectral_data.txt'
output_plot_filename = 'spectrum_plot.png'

# Process the FITS file
process_fits_file(fits_filename, output_data_filename, output_plot_filename)
