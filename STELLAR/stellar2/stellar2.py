from astroquery.vizier import Vizier
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np

# Set up the query to limit the number of rows
vizier = Vizier(columns=['RA_ICRS', 'DE_ICRS', 'gmag', 'SpObjID'], row_limit=100)  # Limiting to 100 rows

# Query the SDSS DR16 catalog (V/154/sdss16)
result = vizier.get_catalogs('V/154/sdss16')

# Extract the data
data = result[0]

# Check available columns
print("Available columns:", data.colnames)

# Check if 'RA_ICRS', 'DE_ICRS', 'gmag', and 'SpObjID' columns are available
if 'RA_ICRS' in data.colnames and 'DE_ICRS' in data.colnames and 'gmag' in data.colnames and 'SpObjID' in data.colnames:
    ra = np.array(data['RA_ICRS'], dtype=float)
    dec = np.array(data['DE_ICRS'], dtype=float)
    gmag = np.array(data['gmag'], dtype=float)
    spobjid = np.array(data['SpObjID'], dtype=str)  # Using str to accommodate possible alphanumeric IDs

    # Convert RA and DEC to Galactic Coordinates
    skycoord = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
    galactic = skycoord.galactic

    # Plot 1: Galactic Longitude vs Galactic Latitude with color representing gmag
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(galactic.l.degree, galactic.b.degree, c=gmag, cmap='viridis', alpha=0.6, s=30, edgecolor='k')
    plt.colorbar(label='gmag')
    plt.xlabel('Galactic Longitude (l)')
    plt.ylabel('Galactic Latitude (b)')
    plt.title('Galactic Coordinates with gmag')

    # Plot 2: Galactic Longitude vs Galactic Latitude with size representing SpObjID
    plt.subplot(1, 2, 2)
    # Mapping SpObjID to a range for size representation
    size_map = np.linspace(10, 100, len(np.unique(spobjid)))
    spobjid_unique = np.unique(spobjid)
    size_dict = {id_: size_map[i] for i, id_ in enumerate(spobjid_unique)}
    sizes = np.array([size_dict[id_] for id_ in spobjid])

    plt.scatter(galactic.l.degree, galactic.b.degree, c=gmag, cmap='viridis', alpha=0.6, s=sizes, edgecolor='k', alpha=0.7)
    plt.colorbar(label='gmag')
    plt.xlabel('Galactic Longitude (l)')
    plt.ylabel('Galactic Latitude (b)')
    plt.title('Galactic Coordinates with SpObjID size')

    plt.tight_layout()
    plt.show()
