import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'tf-data.xlsx'  # Corrected path to the file
df = pd.read_excel(file_path)

# Correct the H I line width (Wi) for inclination
df['Wi'] = df['Line width'] / np.sin(np.radians(df['Inclination']))

# Account for self-extinction
df['Correction factor'] = (1.57 + 2.75 * (np.log10(df['Wi']) - 2.5)) * df['log(a/b)']

# Apply the correction factor to the apparent magnitude
df['Corrected apparent magnitude'] = df['Apparent magnitude'] + df['Galactic extinction'] + df['Correction factor']

# Determine the distance using the corrected apparent magnitude
df['Distance (Mpc)'] = 10 ** ((df['Corrected apparent magnitude'] - df['Absolute magnitude']) / 5 + 1) / 1e6  # Convert to Mpc

# Ensure no NaNs or infinite values are present in Wi or Absolute Magnitude
df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['Wi', 'Absolute magnitude'])

# If the Tully-Fisher relation should be logarithmic, use log(Wi)
log_Wi = np.log10(df['Wi'])

# Fit a line to the log(Wi) vs Absolute Magnitude
slope, intercept = np.polyfit(log_Wi, df['Absolute magnitude'], 1)

# Create an array of x values for the fitted line
x_fit = np.linspace(min(log_Wi), max(log_Wi), 100)
y_fit = slope * x_fit + intercept

# Plot the Tully-Fisher relation
plt.errorbar(log_Wi, df['Absolute magnitude'], yerr=df['Error.4'], fmt='o', label='Data points')

# Plot the fitted line
plt.plot(x_fit, y_fit, 'r--', label='Fitted line')

plt.xlabel('Log(Corrected Line Width) (log(Wi))')
plt.ylabel('Absolute Magnitude')
plt.title('Tully-Fisher Relation')
plt.gca().invert_yaxis()  # Magnitude scale is inverted
plt.legend()
plt.grid(True)
plt.show()

# Print the slope and intercept of the Tully-Fisher relation
print(f'Slope of the Tully-Fisher relation: {slope:.2f}')
print(f'Intercept of the Tully-Fisher relation: {intercept:.2f}')

# Print the distances in Mpc
print("Distances to galaxies (in Mpc):")
print(df[['Name', 'Distance (Mpc)']])
