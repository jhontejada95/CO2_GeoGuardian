import os
import pymysql
import geopandas
import pandas as pd
import matplotlib.pyplot as plt

SERVER = os.environ["SERVER"]
DATABASE = os.environ["DATABASE"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
DRIVER = os.environ["DRIVER"]
ROWS = 350

with pymysql.connect(host=SERVER,
                     port=3306,
                     user=USERNAME,
                     passwd=PASSWORD,
                     database=DATABASE) as conn:
    sql_query = f'SELECT * FROM sys.co2Storage ORDER BY date_c DESC LIMIT {ROWS}'
    df = pd.read_sql(sql_query, conn)

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
plt.savefig("img/map.jpg")
plt.show()