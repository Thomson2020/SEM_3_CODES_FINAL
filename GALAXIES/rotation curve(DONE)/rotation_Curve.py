from galpy.potential import plotRotcurve, MWPotential2014 as mwp14
import matplotlib.pyplot as plt
from galpy.potential import vcirc, epifreq, verticalfreq, MWPotential2014 as mwp14


# Plot the total rotation curve for MWPotential2014
plotRotcurve(mwp14)

# Overplot individual components
plotRotcurve(mwp14[0], label='Bulge', overplot=True)  # Plot Bulge component
plotRotcurve(mwp14[1], label='Disk', overplot=True)   # Plot Disk component
plotRotcurve(mwp14[2], label='Halo', overplot=True)   # Plot Halo component

# Add a legend to the plot
plt.legend()

# Display the plot
plt.xlabel('Radius (kpc)')
plt.ylabel('Rotation Curve (km/s)')
plt.title('Milky Way Rotation Curve Components')
plt.grid(True)
plt.show()

radius = 8.0
circular_velocity = vcirc(mwp14, radius)
epicyclic_frequency = epifreq(mwp14, radius)
vertical_frequency = verticalfreq(mwp14, radius)

print(f"Circular Velocity at {radius} kpc: {circular_velocity:.2f} km/s")
print(f"Epicyclic Frequency at {radius} kpc: {epicyclic_frequency:.2f} /Gyr")
print(f"Vertical Frequency at {radius} kpc: {vertical_frequency:.2f} /Gyr")

from galpy.potential import plotRotcurve, MWPotential2014, MiyamotoNagaiPotential, KuzminDiskPotential, MN3ExponentialDiskPotential, HernquistPotential
import matplotlib.pyplot as plt

# Define the potentials
miyamoto_nagai_pot = MiyamotoNagaiPotential(amp=1.0, a=0.5, b=0.1, normalize=False)
kuzmin_pot = KuzminDiskPotential(amp=1.0, a=1.0, normalize=False)
edp = MN3ExponentialDiskPotential(amp=1.0, hr=1.0 / 3.0, hz=1.0 / 16.0, normalize=False)
hernquist_pot = HernquistPotential(a=0.6 / 8, normalize=False)

# Plot the rotation curves
plt.figure(figsize=(10, 6))

# Miyamoto-Nagai Potential
plotRotcurve(miyamoto_nagai_pot, linestyle='--', color='red', label='Miyamoto-Nagai')
plt.xlabel('Radius (kpc)')
plt.ylabel('Rotation Curve (km/s)')
plt.title('Miyamoto Nagai Potential')
plt.grid(True)
# Kuzmin Disk Potential
plotRotcurve(kuzmin_pot, linestyle='-.', color='green', label='Kuzmin Disk')
plt.xlabel('Radius (kpc)')
plt.ylabel('Rotation Curve (km/s)')
plt.title('Kuzmin Disk Potential')
plt.grid(True)
# MN3 Exponential Disk Potential
plotRotcurve(edp, linestyle=':', color='purple', label='Exponential Disk')
plt.xlabel('Radius (kpc)')
plt.ylabel('Rotation Curve (km/s)')
plt.title('MN3 Exponential Disl Potential')
plt.grid(True)
# Hernquist Potential
plotRotcurve(hernquist_pot, linestyle='-', color='orange', label='Hernquist')
plt.xlabel('Radius (kpc)')
plt.ylabel('Rotation Curve (km/s)')
plt.title('Hernquist Potential')
plt.grid(True)
plt.show()

# Add labels, legend, and title
plt.xlabel('Radius (kpc)')
plt.ylabel('Rotation Curve (km/s)')
plt.title('Comparison of Rotation Curves for Different Potentials')
plt.grid(True)

# Set the same x and y axis limits as used in the Hernquist plot
plt.xlim(0, 10)
plt.ylim(0, 2)

plotRotcurve(mwp14,label='MW Potential',linestyle='-',overplot=True)
plotRotcurve(miyamoto_nagai_pot, linestyle='--', color='red', label='Miyamoto-Nagai',overplot=True)
plotRotcurve(kuzmin_pot, linestyle='-.', color='green', label='Kuzmin Disk',overplot=True)
plotRotcurve(edp, linestyle=':', color='purple', label='Exponential Disk',overplot=True)
plotRotcurve(hernquist_pot, linestyle=(0, (3, 5, 1, 5)), color='orange', label='Hernquist',overplot=True)
plt.xlim(0,5)
plt.ylim(0,2)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
