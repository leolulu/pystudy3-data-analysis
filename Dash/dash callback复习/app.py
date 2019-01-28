import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [dcc.Input(id='input1', placeholder='input something', type='text')]
    + [html.Br() for i in range(10)]
    + [html.Div([
        html.P(id='p1')
    ])]
    + [
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='FUCKL',
            id='dropdown1',
            multi=True
        )
    ]
    + [html.P(id='p2')]
)


@app.callback(
    Output('p1', 'children'),
    [Input('input1', 'value')]
)
def updateP(value):
    return value

@app.callback(
    Output('p2', 'children'),
    [Input('dropdown1', 'value')]
)
def updateP(value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)
