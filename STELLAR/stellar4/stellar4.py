from astroquery.simbad import Simbad
import astropy.units as u
from astropy.coordinates import SkyCoord
import numpy as np
import matplotlib.pyplot as plt

# Define the function to query SIMBAD for a star cluster
def query_simbad(cluster_name, radius=1.0):
    custom_simbad = Simbad()
    custom_simbad.add_votable_fields('parallax', 'flux(V)', 'flux(B)')

    # Perform the query
    result = custom_simbad.query_region(SkyCoord.from_name(cluster_name),
                                        radius=radius * u.deg)
    return result

# Function to calculate luminosity and temperature
def calculate_luminosity_temperature(data):
    # Extract necessary columns from the data
    parallax = data['PLX_VALUE']
    v_mag = data['FLUX_V']

    # Calculate distance in parsecs
    distance_pc = 1000 / parallax

    # Calculate absolute magnitude
    abs_mag = v_mag - 5 * (np.log10(distance_pc) - 1)

    # Luminosity calculation (assuming a solar magnitude of 4.83 for the Sun)
    luminosity = 10 ** ((4.83 - abs_mag) / 2.5)

    # Temperature estimation (using a placeholder here; proper method depends on available data)
    # For now, using a simple formula based on B-V color index if available
    bv_color = data['FLUX_B'] - v_mag
    temperature = 4600 * ((1 / (0.92 * bv_color + 1.7)) + (1 / (0.92 * bv_color + 0.62)))

    return temperature, luminosity, bv_color, v_mag

# Function to plot HR diagram
def plot_hr_diagram(temperature, luminosity):
    plt.figure(figsize=(10, 6))
    plt.scatter(temperature, luminosity, c='blue', s=10)
    plt.xscale('log')
    plt.yscale('log')
    plt.gca().invert_xaxis()
    plt.xlabel('Temperature (K)')
    plt.ylabel('Luminosity (L/Lsun)')
    plt.title('Hertzsprung-Russell Diagram')
    plt.grid(True)
    plt.show()

# Function to plot Color-Magnitude diagram
def plot_color_magnitude_diagram(bv_color, v_mag):
    plt.figure(figsize=(10, 6))
    plt.scatter(bv_color, v_mag, c='red', s=10)
    plt.gca().invert_yaxis()
    plt.xlabel('Color Index (B-V)')
    plt.ylabel('Magnitude (V)')
    plt.title('Color-Magnitude Diagram')
    plt.grid(True)
    plt.show()

# Query SIMBAD for Hyades and Pleiades clusters
hyades_data = query_simbad('Hyades')
pleiades_data = query_simbad('Pleiades')

# Calculate luminosity and temperature for Hyades
hyades_temp, hyades_lum, hyades_bv, hyades_vmag = calculate_luminosity_temperature(hyades_data)

# Calculate luminosity and temperature for Pleiades
pleiades_temp, pleiades_lum, pleiades_bv, pleiades_vmag = calculate_luminosity_temperature(pleiades_data)

# Plot HR diagram for Hyades
plot_hr_diagram(hyades_temp, hyades_lum)

# Plot HR diagram for Pleiades
plot_hr_diagram(pleiades_temp, pleiades_lum)

# Plot Color-Magnitude diagram for Hyades
plot_color_magnitude_diagram(hyades_bv, hyades_vmag)

# Plot Color-Magnitude diagram for Pleiades
plot_color_magnitude_diagram(pleiades_bv, pleiades_vmag)
