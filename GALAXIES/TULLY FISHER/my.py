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
spiral_galaxies = df.head(20)

# Ensure no division by zero and check for valid inclinations
spiral_galaxies['Inclination'] = spiral_galaxies['Inclination'].replace(0, np.nan)
spiral_galaxies['Wi'] = spiral_galaxies['Line width'] / np.sin(np.radians(spiral_galaxies['Inclination']))

# Ensure Wi - 2.5 > 0 to avoid invalid values in log10
spiral_galaxies = spiral_galaxies[spiral_galaxies['Wi'] > 2.5]
spiral_galaxies['extinction_correction'] = (1.57 + 2.75 * np.log10(spiral_galaxies['Wi'] - 2.5)) * spiral_galaxies['log(a/b)']

# Correct the apparent magnitude for both self-extinction and Galactic extinction
spiral_galaxies['corrected_magnitude'] = spiral_galaxies['Apparent magnitude'] - spiral_galaxies['extinction_correction'] - spiral_galaxies['Galactic extinction']

# Determine the distance using the distance modulus relation
spiral_galaxies['distance_modulus'] = spiral_galaxies['corrected_magnitude'] - spiral_galaxies['Absolute magnitude']
spiral_galaxies['distance'] = 10 ** ((spiral_galaxies['distance_modulus'] + 5) / 5) / 1e6  # Convert to Mpc

# Perform linear regression to find the slope
log_Wi = np.log10(spiral_galaxies['Wi'])
slope, intercept, r_value, p_value, std_err = linregress(log_Wi, spiral_galaxies['Absolute magnitude'])

# Plot the Tully-Fisher relation with error bars
plt.errorbar(spiral_galaxies['Wi'], spiral_galaxies['Absolute magnitude'], yerr=0.1, fmt='o', label='Data')  # Assuming 0.1 mag uncertainty

# Plot the regression line
x = np.linspace(log_Wi.min(), log_Wi.max(), 100)  # Generate x values for the line
y = slope * x + intercept
plt.plot(10**x, y, label=f'Slope: {slope:.2f}', color='red')

plt.xlabel('Corrected H I Line Width (Wi)')
plt.ylabel('Absolute Magnitude')
plt.title('Tully-Fisher Relation')
plt.xscale('log')  # Set x-axis to logarithmic scale
plt.gca().invert_yaxis()  # Invert y-axis
plt.legend()
plt.grid(True)
plt.show()

print(f"Slope of the Tully-Fisher relation: {slope:.2f}")
