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


intensity = dict()
intensity['H200S0'] = 3.00e-05
intensity['H200S1'] = 5.16e-04
intensity['H200S2'] = 3.71e-04
intensity['H200S3'] = 1.76e-03
intensity['H200S4'] = 5.28e-04
intensity['H200S5'] = 9.73e-04

a = []
for i in intensity:
    # For this example, set a largish uncertainty on the intensity.
    m = Measurement(data=intensity[i],uncertainty=StdDevUncertainty(intensity[i]),
                    identifier=i,unit="erg cm-2 s-1 sr-1")
    print(m)
    a.append(m)
h = H2ExcitationFit(a)
h.column_densities(line=False, norm=False)
hplot = ExcitationPlot(h,"H_2")
hplot.ex_diagram(ymax=21,xmax=5000)
h.run()
hplot.ex_diagram(show_fit=True,ymax=21,xmax=5000)

print(f"Ortho-to-para ratio (fixed) = {h.opr:.2f}")
h.run(components=2)

h.run(components=1)
hplot.ex_diagram(show_fit=True,ymax=21,xmax=5000)
h.run()
print(f'T(cold) = {h.tcold}')
print("T(hot) = {:>8.3f}".format(h.thot))
print(f'N(cold) = {h.cold_colden:3.2E}')
print('N(hot) = ',h.hot_colden)
print(f'N(total) = {h.total_colden:+.1e}')
print(f"Ortho-to-para ratio (fixed) = {h.opr:.2f}")

plt.show()