import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from readdb import getData

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def generate_table(dataframe):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(len(dataframe))]
    )


app.layout = html.Div([
    html.H3('各类数据库的结果'),

    generate_table(getData("select * from websites")),

    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=1,
        step=0.001
    ),

    dcc.Location(id='shit',refresh=True),
    dcc.Link('/shit',href='/shit',refresh=False),
    
],className='main')



app.run_server(debug=True)
