import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from datetime import timedelta

# set up labels
times_index = pd.date_range("2018-01-01", periods=5)
lons = np.linspace(-120, -60, 4)
lats = np.linspace(25, 55, 3)
xr_coord = [times_index, lats, lons]
xr_dims = ["time", "lat", "lon"]

# create random temperature data
rng = np.random.default_rng()
temp_data = 283.0 + 5.0 * rng.standard_normal((5, 3, 4))

temperature = xr.DataArray(temp_data, coords=xr_coord, dims=xr_dims)
temperature.attrs["units"] = "Kelvin"
temperature.attrs["standard_name"] = "air_temperature"

# create random pressure data
pressure_data = 1000.0 + 5.0 * rng.standard_normal((5, 3, 4))

pressure = xr.DataArray(pressure_data, coords=xr_coord, dims=xr_dims)
pressure.attrs["units"] = "hPa"
pressure.attrs["standard_name"] = "air_pressure"

# create Dataset
ds = xr.Dataset(data_vars=
    {
        "Temperature": temperature,
        "Pressure": pressure
    }
)

# selecting data
temperature[1, :, :] # numpy style
temperature.sel(time="2018-01-02") # .sel method
temperature.sel(lat=25, lon=-120)
temperature.sel(time="2018-01-07", method="nearest", tolerance=timedelta(days=2)) # select nearest
temperature.interp(lon=-105, lat=40, method="linear") # interpolating
temperature.sel(time=slice("2018-01-01", "2018-01-03"), lon=slice(-110, -70), lat=slice(25, 45)) # selecting by slice
temperature.loc["2018-01-01":"2018-01-03", 25:45, -110:-70] # select .loc (can't select with names)
