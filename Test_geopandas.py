import geopandas
import matplotlib.pyplot as plt

# Returns names of available maps
geopandas.datasets.available
# Returns path of a particular map
geopandas.datasets.get_path('naturalearth_lowres')
# Opens the map as a GeoDataFrame
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# Subsets the GeoDataFrame
col = world[world.name == "Colombia"]
# Plots
col.plot()
plt.show()