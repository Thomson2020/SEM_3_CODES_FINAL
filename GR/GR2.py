import numpy as np

from einsteinpy.geodesic import Geodesic, Timelike, Nulllike
from einsteinpy.plotting import GeodesicPlotter, StaticGeodesicPlotter, InteractiveGeodesicPlotter

# Initial Conditions
position = [4, np.pi/2, 10]
momentum = [10, 0.4, -1.5]
a = 0.5 # Schwarzschild Black Hole

geod = Timelike(
    metric = "Kerr",
    metric_params = (a,),
    position=position,
    momentum=momentum,
    steps=400,
    delta=0.5,
    return_cartesian=True
)
geod

gpl.clear() # In Interactive mode, `clear()` must be called before drawing another plot, to avoid overlap
gpl.plot2D(geod, coordinates=(1, 2), color="green")
gpl.show()

gpl.clear()
gpl.plot2D(geod, coordinates=(1, 3), color="green")
gpl.show()

gpl.clear()
gpl.parametric_plot(geod, colors=("red", "green", "blue"))
gpl.show()