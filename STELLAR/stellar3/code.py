import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

# Function to retrieve, clean, and plot lightcurve
def get_cleaned_lightcurve(target_id):
    # Download the light curve
    lc = lk.search_lightcurvefile(target_id).download().PDCSAP_FLUX.remove_outliers().remove_nans()
    
    # Plot the light curve
    lc.scatter()
    plt.title(f"Lightcurve of {target_id}")
    plt.show()
    
    return lc

# Function to extract statistical parameters
def extract_statistics(lc):
    mean_flux = np.nanmean(lc.flux)
    std_flux = np.nanstd(lc.flux)
    skewness = skew(lc.flux, nan_policy='omit')
    kurt = kurtosis(lc.flux, nan_policy='omit')
    
    # Estimate the period using a Lomb-Scargle periodogram
    period = lc.to_periodogram().period_at_max_power.value
    
    return mean_flux, std_flux, skewness, kurt, period

# Define the target IDs and their classifications
targets = [
    {"id": "TIC 206669860", "classification": "Eclipsing Binary"},
    {"id": "TIC 25155310", "classification": "RR Lyrae"}
]

# Create an empty list to store the results
results = []

# Loop over each target to process
for target in targets:
    # Retrieve and clean the lightcurve
    lc = get_cleaned_lightcurve(target["id"])
    
    # Extract statistical parameters
    mean_flux, std_flux, skewness, kurt, period = extract_statistics(lc)
    
    # Append the results to the list
    results.append([target["id"], target["classification"], mean_flux, std_flux, skewness, kurt, period])

# Convert the results to a DataFrame for better visualization
df = pd.DataFrame(results, columns=["Target ID", "Classification", "Mean Flux", "Std Flux", "Skewness", "Kurtosis", "Period (days)"])

# Print the DataFrame
print(df)
