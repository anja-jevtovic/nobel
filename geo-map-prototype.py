import plotly.express as px
import pprint
import pandas as pd
import numpy as np
import json
#import geopandas as gpd

df = pd.read_csv("pop.csv", delimiter=';')
df["Population"] = df["Population"].astype(int)

print(df)
print('\n')

geojson = None
with open('custom.geo.json', 'r') as f:
    data = f.read()
    geojson = json.loads(data)

#pprint.pprint(geojson)

'''
geojson_pd = None
with open('custom.geo.json', 'r') as f:
    geojson_pd = geopandas.read_file(f)

pprint.pprint(geojson_pd)
'''

fig = px.choropleth(df, geojson=geojson, color="Population", color_continuous_scale=px.colors.sequential.Plasma, range_color=[0, 70000000],
                    locations="name", featureidkey="properties.brk_name",
                    projection="mercator"
                   )

fig.update_geos(scope="europe", resolution=50, showcountries=True, fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()