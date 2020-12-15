# import plotly.io as pio
# import plotly.express as px
# import plotly.graph_objects as go
# import plotly.figure_factory as ff
# from plotly.subplots import make_subplots
# from plotly.validators.scatter.marker import SymbolValidator
# import numpy as np
import pandas as pd
# import json
# from urllib.request import urlopen
#
# from mapboxgl.utils import *
# from mapboxgl.viz import *

df = pd.read_excel(r'C:\my_develop\my_visual\source\loca_info.xlsx')
# print(df.info())
#
# px.set_mapbox_access_token(open(".mapbox_token").read())
#
# # token = open(".mapbox_token").read()
#
# fig = px.scatter_mapbox(df, lat='ycoord', lon='xcoord',
#                       hover_name='build', hover_data=["person"],
#                        color_discrete_sequence=["fuchsia"], zoom=3, height=400)
# fig.update_layout(mapbox_style = "open-street-map")
# fig.update_layout(margin = {'r':0, 't':0, 'l':0, 'b':0})
# fig.show()


# import pandas as pd
# us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
#
# print(us_cities.info())
# import plotly.express as px
#
# fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
#                         color_discrete_sequence=["fuchsia"], zoom=3, height=300)
# fig.update_layout(mapbox_style="open-street-map")
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()


# token = open(".mapbox_token").read() # you will need your own token
#
# import pandas as pd
# us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
#
# import plotly.express as px
#
# fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
#                         color_discrete_sequence=["fuchsia"], zoom=3, height=300)
# fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()


import pandas as pd
# us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px

fig = px.scatter_mapbox(df, lat="xcoord", lon="ycoord", hover_name="build", hover_data=["person"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()