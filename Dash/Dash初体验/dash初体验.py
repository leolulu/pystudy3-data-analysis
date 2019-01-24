import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
app.scripts.config.serve_locally = False

app.layout = html.Div([
    html.H1('Hello Dash',id='header1'),
    html.H2('第二个H',className='header2'),
    html.Div(' Dash: A web application framework for Python.'),
    dcc.Graph(
        id='first-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout':{
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.Img(src='/assets/image.jpg')
])

if __name__ == '__main__':
    app.run_server(port=16543, debug=True)
