import pandas as pd 
import plotly.express as px  

import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
from dash import no_update

def generate_graph(df, graph_choice, title, msg, x, y):
        if graph_choice == 'pie':
            # pie chart
            fig = px.pie(df, values=x, names=y, title=title, color_discrete_sequence=px.colors.sequential.RdBu, template="plotly_dark")
        elif graph_choice == 'bar':
            # graph bar
            fig = px.bar(df, x=x, y=y, title=title, height=400, template="plotly_dark")
        elif graph_choice == 'line':
            # line/density graph
            fig = px.line(df, x=x, y=y, title=title, template="plotly_dark")
        else:
        # bubble chart
            fig = px.scatter(df, x=x, y=y, title=title, size_max=60, template="plotly_dark")
        
        fig.update_layout(title_font_size=60, title_font_color="#f5bf42")

        return fig

app = dash.Dash(__name__)

df = pd.read_csv('data-set.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Data set must be uploaded in repl.it under following name: data-set.csv'),
    html.Label('Select data visual type'),
    dcc.Dropdown(id='graph_type',
        options=[
            {'label': 'pie chart', 'value': 'pie'},
            {'label': 'line graph', 'value': 'line'},
            {'label': 'bar graph', 'value': 'bar'},
            {'label':'bubble chart', 'value':'scatter'}
        ],
        value='pie',
        style={'width': '30%'}
    ),

    html.Label('Enter the title'),
    dcc.Input(id='title',type='text'),

    html.Label('Enter the message'),
    dcc.Textarea(id='msg',style={'width': '50%', 'height': 100}),

    html.Label('X-axis (pie chart -> values)'),
    dcc.Input(id='x',type='text'),
    
    html.Label('Y-axis (pie chart -> names)'),
    dcc.Input(id='y', type='text'),

    html.Br(),
    html.Br(),

    html.Button('Load Graph', id='btn', n_clicks=0),
    html.Br(),

    html.P(id='msg_cont', style={'text-align': 'center'}, children=[]),
    html.Br(),


    dcc.Graph(id='map', figure={})

])

@app.callback(
    Output('map', 'figure'),
    Output('msg_cont', 'children'),
    Input('btn', 'n_clicks'),
    Input('graph_type','value'),
    Input('title','value'),
    Input('msg', 'value'),
    Input('x','value'),
    Input('y','value')
)
def update_graph(n_clicks, graph_type, title, msg, x, y):
    if int(n_clicks)%2 != 0:
        fig = generate_graph(df, graph_type, title, msg, x, y)
        return fig, msg
    else:
        return no_update 

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')