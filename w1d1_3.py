import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from pathlib import Path

# opening a netCDF file/selecting data
ds = xr.open_dataset(Path("NARR_19930313_0000.nc"))
ds.isobaric1
ds_1000 = ds.sel(isobaric1=1000.0)
ds_1000.Temperature_isobaric

# standard deviation
u_winds = ds["u-component_of_wind_isobaric"]
u_winds.std(dim=["x", "y"])

# mean
temps = ds["Temperature_isobaric"]
co_temps = temps.sel(x=slice(-182, 424), y=slice(-1450, -990))
prof = co_temps.mean(dim=["x", "y"])

# plotting 1D
prof.plot(y="isobaric1", yincrease=False)
plt.show()

# plotting 2D
temps.sel(isobaric1=1000).plot()
plt.show()
