import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# init web app
# -------------------------------------------------------------------------------------------
app = dash.Dash(__name__)

# Import and clean data
# -------------------------------------------------------------------------------------------
df = pd.read_csv('dataset_bees.csv')

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year',
                 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

# app layout
# -------------------------------------------------------------------------------------------
app.layout = html.Div([
    html.H1('Web Application Dashboard with Dash',
            style={'text-align': 'center'}),
    dcc.Dropdown(id="slct_year",
                 options=[{
                     "label": "2015",
                     "value": 2015
                 }, {
                     "label": "2016",
                     "value": 2016
                 }, {
                     "label": "2017",
                     "value": 2017
                 }, {
                     "label": "2018",
                     "value": 2018
                 }],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}),
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='bee_map', figure={})
])


# connecting plotly graphs with dash components
# -------------------------------------------------------------------------------------------
@app.callback([
    Output(component_id='output_container', component_property='children'),
    Output(component_id='bee_map', component_property='figure')
], [Input(component_id='slct_year', component_property='value')])
def update_graph(option_selected):
    print(option_selected)
    print(type(option_selected))

    container = f'The year chosen by user was {option_selected}'

    dff = df.copy()
    dff = dff[dff['Year'] == option_selected]
    dff = dff[dff['Affected by'] == 'Varroa_mites']

    # plotly express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope='usa',
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.ice,
        labels={'Pct of Colonies Impacted': 'precentage of Bee Colonies'},
        template='plotly_dark')

    return container, fig


# run
# -------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')

# challenge A:

#Use plotly express to plot a Bar chart instead of a choropleth map.
#X-axis should represent States
#Y-axis should represent % of bee colonies

# challenge B:

#Use plotly express to plot a Line chart instead of a choropleth map.
#X-axis should represent Year
#Y-axis should represent % of bee colonies
#Color should represent different State
#Drop-down should be list of things affecting bees
