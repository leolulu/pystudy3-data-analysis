import dash
import dash_core_components as dcc
import dash_html_components as html
from banner_generatror import generator
from flask import request
from timeprint import timeprint

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        dcc.Input(
            placeholder='请输入待转换的句子...',
            type='text',
            value='',
            id='input1',
            style={'width': '100%'}
        )
    ),
    html.Div(
        html.Button('转换', id='transfrom')
    ),
    html.Div(
        dcc.Textarea(
            id='p1',
            style={'width': '50%', 'height': '600px', 'minWidth': '300px'}

        )
    )
])


@app.callback(
    dash.dependencies.Output('p1', 'value'),
    [
        dash.dependencies.Input('transfrom', 'n_clicks')
    ],
    [
        dash.dependencies.State('input1', 'value')
    ]
)
def transfrom(n_clicks, value):
    result = generator(value)
    timeprint(request.remote_addr, '\n', value, '\n', request.user_agent, '\n')
    return result


if __name__ == '__main__':
    app.run_server(debug=False, port=3344, host='0.0.0.0')
