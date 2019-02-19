import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        html.P(id='p1')
    ),
    html.Div(
        dcc.Slider(id='Slider1', min=0, max=100, step=0.1, value=50, updatemode='drag')
    ),
    html.Div(
        html.P(id='p2')
    ),
])


@app.callback(
    dash.dependencies.Output('p1', 'children'),
    [
        dash.dependencies.Input('Slider1', 'value')
    ]
)
def showProcessNum(value):
    return value


@app.callback(
    dash.dependencies.Output('p2', 'children'),
    [
        dash.dependencies.Input('Slider1', 'value')
    ]
)
def showProcessImg(rate):
    total_num = 50
    rate = int(rate / 100 * total_num)
    return '|' + '●' * rate + '○' * (total_num-rate) + '|'


if __name__ == '__main__':
    app.run_server(debug=True)
