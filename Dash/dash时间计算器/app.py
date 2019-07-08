import dash
import dash_core_components as dcc
import dash_html_components as html
import random
from datetime import datetime, timedelta

app = dash.Dash(__name__)


def randomtimes():
    if int(datetime.now().strftime('%H')) < 18:
        time_tuple = (
            '{} 18:05'.format((datetime.now()+timedelta(days=0)).strftime('%Y-%m-%d')),
            '{} 19:00'.format((datetime.now()+timedelta(days=0)).strftime('%Y-%m-%d'))
        )
    else:
        time_tuple = (
            '{} 8:45'.format((datetime.now()+timedelta(days=1)).strftime('%Y-%m-%d')),
            '{} 9:05'.format((datetime.now()+timedelta(days=1)).strftime('%Y-%m-%d'))
        )
    start, end = time_tuple
    frmt = '%Y-%m-%d %H:%M'
    stime = datetime.strptime(start, frmt)
    etime = datetime.strptime(end, frmt)
    return (random.random() * (etime - stime) + stime).strftime('%Y-%m-%d %H:%M:%S')


def get_time_interval(time_string):
    return (datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')-datetime.now()).seconds*1000


app.layout = html.Div([
    html.Div(
        dcc.Input(
            type='text',
            value=randomtimes(),
            id='input1'
        )
    ),
    html.Div(html.Button('Give me another TIME!', id='reflush')),
    html.Div(html.P(id='p1'))
])


@app.callback(
    dash.dependencies.Output('input1', 'value'),
    [
        dash.dependencies.Input('reflush', 'n_clicks')
    ]
)
def reflush(value):
    return randomtimes()


@app.callback(
    dash.dependencies.Output('p1', 'children'),
    [
        dash.dependencies.Input('input1', 'value')
    ]
)
def get_result(value):
    return get_time_interval(value)


if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(debug=False, port=1124, host='0.0.0.0')
