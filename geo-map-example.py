import plotly.express as px
import pprint
import json

df = px.data.election()
geojson = px.data.election_geojson()

print(df)
print('-------------------------------------------------------\n')

#pprint.pprint(geojson)
print('-------------------------------------------------------\n')

fig = px.choropleth(df, geojson=geojson, color="Bergeron",
                    locations="district", featureidkey="properties.district",
                    projection="mercator"
                   )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()