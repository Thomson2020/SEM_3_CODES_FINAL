import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the Excel file
file_path = 'tf-data.xlsx'
df = pd.read_excel(file_path)

# Print the dataframe to understand its structure and identify the correct column names
print(df.head())

# Select the first twenty spiral galaxies
# Assuming there's a way to identify spiral galaxies, we'll need a placeholder here
# For now, let's assume we take the first twenty entries as spiral galaxies
spiral_galaxies = df.head(20)

# Correct the H I line width based on inclination
spiral_galaxies['Wi'] = spiral_galaxies['Line width'] / np.sin(np.radians(spiral_galaxies['Inclination']))

# Account for self-extinction due to dust and gas
spiral_galaxies['extinction_correction'] = (1.57 + 2.75 * np.log10(spiral_galaxies['Wi'] - 2.5)) * spiral_galaxies['log(a/b)']

# Correct the apparent magnitude for both self-extinction and Galactic extinction
spiral_galaxies['corrected_magnitude'] = spiral_galaxies['Apparent magnitude'] - spiral_galaxies['extinction_correction'] - spiral_galaxies['Galactic extinction']

# Determine the distance using the distance modulus relation
spiral_galaxies['distance_modulus'] = spiral_galaxies['corrected_magnitude'] - spiral_galaxies['Absolute magnitude']
spiral_galaxies['distance'] = 10 ** ((spiral_galaxies['distance_modulus'] + 5) / 5) / 1e6  # Convert to Mpc

# Plot the Tully-Fisher relation and determine the slope
plt.errorbar(spiral_galaxies['Wi'], spiral_galaxies['Absolute magnitude'], yerr=0.1, fmt='o')  # Assuming 0.1 mag uncertainty

# Perform linear regression to find the slope
slope, intercept, r_value, p_value, std_err = linregress(np.log10(spiral_galaxies['Wi']), spiral_galaxies['Absolute magnitude'])

# Plot the regression line
x = np.log10(spiral_galaxies['Wi'])
y = slope * x + intercept
plt.plot(10**x, y, label=f'Slope: {slope:.2f}')

# Set labels and title
plt.xlabel('Corrected H I Line Width (Wi)')
plt.ylabel('Absolute Magnitude')
plt.title('Tully-Fisher Relation')
plt.legend()
plt.gca().invert_yaxis()
plt.show()

print(f"Slope of the Tully-Fisher relation: {slope:.2f}")
