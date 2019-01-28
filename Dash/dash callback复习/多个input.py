import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


app.layout = html.Div([
    html.Div(html.P('init value', id='p1')),
    html.Div(dcc.Slider(id='slider1', min=-5, max=10, step=0.01, updatemode='drag'))
])


@app.callback(
    Output('p1', 'children'),
    [
        Input('slider1', 'value')
    ]
)
def updateValue(slider_value):
    return slider_value


if __name__ == '__main__':
    app.run_server(debug=True)
