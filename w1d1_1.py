import numpy as np
import pandas as pd
import xarray as xr

# create a random array of temperature data
rng = np.random.default_rng()
rand_data = 283.0 + 5.0 * rng.standard_normal((5, 3, 4))

# create a DataArray
temperature = xr.DataArray(rand_data)

# create DataArray with dimension names
temperature = xr.DataArray(rand_data, dims=["time", "lat", "lon"])

# make an array of datetime data
times_index = pd.date_range("2018-01-01", periods=5)

# longitude/latitude coordinates
lons = np.linspace(-120, -60, 4)
lats = np.linspace(25, 55, 3)

# create DataArray with dimension names and coordinate info
temperature = xr.DataArray(rand_data, coords=[times_index, lats, lons], dims=["time", "lat", "lon"])

# set attributes
temperature.attrs["units"] = "Kelvin"
temperature.attrs["standard_name"] = "air_temperature"

# attributes are not kept after operations
temperature_in_celsius = temperature - 273.15

# create a pressure DataArray with same coordinates
pressure_data = 1000.0 + 5.0 * rng.standard_normal((5, 3, 4))
pressure = xr.DataArray(pressure_data, coords=[times_index, lats, lons], dims=["time", "lat", "lon"])
pressure.attrs["units"] = "hPa"
pressure.attrs["standard_name"] = "air_pressure"

# create a Dataset to contain the DataArrays
ds = xr.Dataset(
    data_vars = 
    {
        "Temperature": temperature,
        "Pressure": pressure
    }
)

# accessing arrays
ds.Pressure
ds["Pressure"]
