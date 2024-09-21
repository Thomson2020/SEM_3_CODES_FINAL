import numpy as np
import matplotlib.pyplot as plt
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
M_sun = 1.989e30  # mass of the Sun in kg
AU = 1.496e11  # 1 Astronomical Unit in meters
M1 = 1000 * M_sun  # Mass of primary star in kg
M2 = 100 * M_sun  # Mass of secondary star in kg
d = 1.2 * AU  # Semi-major axis in meters
e = 0.2  # Eccentricity (dimensionless)
#mu = (M1 * M2) / (M1 + M2)
P = 2 * np.pi * np.sqrt(d**3 / (G * (M1 + M2)))
t_primary = P * 0.25
sigma_primary = P * 0.03
delta_F_primary = 0.1
t_secondary = P * 0.65
sigma_secondary = P * 0.03
delta_F_secondary = 0.15
total_time = 2 * P  # observing two full orbital periods
num_points = 1000  # number of data points
time_vals = np.linspace(0, total_time, num_points)
def eclipse_brightness(time):
  brightness = np.ones_like(time)
  brightness -= delta_F_primary*np.exp(-0.5*((time-t_primary)/sigma_primary)**2)
  brightness -= delta_F_secondary*np.exp(-0.5*((time-t_secondary)/sigma_secondary)**2)
  return brightness

brightness = eclipse_brightness(time_vals)
time_vals_in_days = time_vals / (60 *60* 24)
plt.figure(figsize=(10, 6))
plt.plot(time_vals_in_days, brightness, color='black')
plt.xlabel('Time (days)')
plt.ylabel('Relative Brightness')
plt.title('Simulated Lightcurve of Eclipsing Binary Star System')
plt.grid(True)
plt.show()