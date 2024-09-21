from pdrtpy.measurement import Measurement
from pdrtpy.tool.h2excitation import H2ExcitationFit, FitMap
from pdrtpy.plot.excitationplot import ExcitationPlot
import pdrtpy.pdrutils as utils
from pdrtpy.modelset import ModelSet
from pdrtpy.plot.modelplot import ModelPlot
from astropy.nddata import StdDevUncertainty, CCDData, NDData,NDDataArray,NDDataBase
import astropy.units as u
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from lmfit import Parameters, fit_report
from lmfit.model import Model, ModelResult

from pdrtools import Measurements, H2ExcitationFit, ExcitationPlot

# Step 1: Initialize the Measurements class and set intensities
measurements = Measurements()
intensities = [3e-5, 5e-4, 4e-4, 2e-3, 5e-4, 1e-3]  # Intensity values for S0 to S5
measurements.set_intensities(intensities)

# Step 2: Initialize H2ExcitationFit and fit the temperature
h2_fit = H2ExcitationFit()
temperature_fit = h2_fit.fit_temperature(measurements)
print("Fitted Temperature:", temperature_fit)

# Step 3: Initialize ExcitationPlot and plot excitation diagrams
excitation_plot = ExcitationPlot()
# Plot with single-component fit
excitation_plot.plot_single_component_fit(measurements, temperature_fit)
# Plot with two-component fit
excitation_plot.plot_two_component_fit(measurements, temperature_fit)

# Step 4: Determine ortho-to-para ratio
ortho_para_ratio = h2_fit.calculate_ortho_para_ratio()
print("Ortho-to-Para Ratio:", ortho_para_ratio)
