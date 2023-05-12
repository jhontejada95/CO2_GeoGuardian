import os
import pymysql
import pandas as pd
import plotly.express as px

DRIVER = os.environ["DRIVER"]
SERVER = os.environ["SERVER"]
DATABASE = os.environ["DATABASE"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class plotGps:

    def __init__(self, rows: int = 45):
        with pymysql.connect(host=SERVER,
                             port=3306,
                             user=USERNAME,
                             passwd=PASSWORD,
                             database=DATABASE) as conn:
            sql_query = f'SELECT * FROM sys.co2Storage ORDER BY date_c DESC LIMIT {rows}'
            self.df = pd.read_sql(sql_query, conn)

    def plot(self):
        fig = px.density_mapbox(self.df,
                                lat='lat',
                                lon='lon',
                                z='co2',
                                radius=20,
                                zoom=14,
                                height=320,
                                color_continuous_scale=["#e6007a", "#cf006d", "#b80061", "#a10055", "#8a0049",
                                                        "#73003d", "#5c0030", "#450024", "#2e0018", "#17000c",
                                                        "#000000"],
                                mapbox_style="open-street-map")
        # fig.show()
        fig.update_layout(margin=dict(l=10, r=10, t=10, b=10),
)
        # convert it to JSON
        fig_json = fig.to_json()

        # a simple HTML template
        template = 'var plotly_data2 = {}'

        # write the JSON to the HTML template
        with open('templates/plots/map.txt', 'w', encoding='utf-8') as f:
            f.write(template.format(fig_json))


if __name__ == '__main__':
    plotGps().plot()
