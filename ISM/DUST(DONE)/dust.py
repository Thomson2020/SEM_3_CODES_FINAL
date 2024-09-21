import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
from dust_extinction.parameter_averages import CCM89, F99

# Create wavelengths array
wav = np.arange(0.1, 3.0, 0.001) * u.micron

# Initialize the figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot for CCM89
ax1 = axes[0]
for R in (2.0, 3.0, 4.0):
    ext_ccm89 = CCM89(Rv=R)
    ax1.plot(1/wav, ext_ccm89(wav), label='CCM89 R=' + str(R))

ax1.set_xlabel('$\lambda^{-1}$ ($\mu$m$^{-1}$)')
ax1.set_ylabel('A($\lambda$) / A(V)')
ax1.legend(loc='best')
ax1.set_title('CCM89 Extinction Law')

# Plot for F99
ax2 = axes[1]
for R in (2.0, 3.0, 4.0):
    ext_f99 = F99(Rv=R)
    ax2.plot(1/wav, ext_f99(wav), label='F99 R=' + str(R))

ax2.set_xlabel('$\lambda^{-1}$ ($\mu$m$^{-1}$)')
ax2.set_ylabel('A($\lambda$) / A(V)')
ax2.legend(loc='best')
ax2.set_title('F99 Extinction Law')

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
