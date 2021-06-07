import pandas as pd 
import plotly.express as px  

import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

# generate fig option function
# --------------------------------------------

def generate_discrete(option_selected, df):
    if option_selected==1:
        # pie chart
        fig = px.pie(df, values='NUMBER (million)', names='GAME', title='Most played games in the world', color_discrete_sequence=px.colors.sequential.RdBu, template="plotly_dark")
    elif option_selected==2:
        # graph bar
        fig = px.bar(df, x='GAME', y='NUMBER (million)', title='Most played games in the world', color='GAME', height=400, labels={'RELEASE DATE':'Release date'}, template="plotly_dark")
    elif option_selected==3:
        # line/density graph
        fig = px.line(df, x='NUMBER (million)', y='GAME', title='Most played games in the world', template="plotly_dark")
    else:
        # bubble chart
        fig = px.scatter(df, x='GAME', y='NUMBER (million)', title='Most played games in the world', size='RELEASE DATE', size_max=60, template="plotly_dark")
    
    fig.update_layout(title_font_size=20, title_font_color="#f5bf42")

    return fig


def generate_continuos(option_selected, df):
    if option_selected==1:
        # pie chart
        fig = px.pie(df, values='ACTIVE USERS (millions)', names='YEAR', title='Yearly growth of Instagram users', color_discrete_sequence=px.colors.sequential.RdBu, template="plotly_dark")
    elif option_selected==2:
        # graph barc
        fig = px.bar(df, x='YEAR', y='ACTIVE USERS (millions)', title='Yearly growth of Instagram users', color='ACTIVE USERS (millions)', height=400, labels={'ACTIVE USERS (millions)':'Active users'}, template="plotly_dark")
    elif option_selected==3:
        # line/density graph
        fig = px.line(df, x='YEAR', y='ACTIVE USERS (millions)', title='Yearly growth of Instagram users', template="plotly_dark")
    else:
        # bubble chart
        fig = px.scatter(df, x='YEAR', y='ACTIVE USERS (millions)', title='Yearly growth of Instagram users', color='ACTIVE USERS (millions)', size='ACTIVE USERS (millions)', size_max=60, template="plotly_dark")
    
    fig.update_layout(title_font_size=20, title_font_color="#f5bf42")

    return fig

# init web app
# --------------------------------------------
app = dash.Dash(__name__)

# Import and clean data
# --------------------------------------------

# data frame 
instagram_growth_df = pd.read_csv('instagram-users-growth.csv')
most_played_games_df = pd.read_csv('most-played-games.csv')

# app layout
# ------------------------------------------

app.layout = html.Div([

    html.H1('Web Application Dashboard with Dash', style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_graph",
                options=[
                    {"label": "pie chart", "value": 1},
                    {"label": "bar graph", "value": 2},
                    {"label": "line graph", "value": 3},
                    {"label": "bubble chart", "value": 4}],
                multi=False,
                value=1,
                style={'width': "40%"}
    ),
    
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='map', figure={})
])

# connecting plotly graphs with dash components
# -------------------------------------------------
@app.callback(
    [Output(component_id='output_container', component_property='children'),
    Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_graph', component_property='value')]
)


def update_graph(option_selected):
    print(option_selected)

    container = f'Chosen type of graph is {option_selected}'

    # plotly express

    fig = generate_discrete(option_selected, most_played_games_df)
    #fig = generate_continuos(option_selected, instagram_growth_df)
        
    return container, fig 

# run
# ------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')

