import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pymysql
import pandas as pd

conn = pymysql.connect('132.232.0.240', 'yxy', 'test', 'mydb')
cursor = conn.cursor()

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions'] = True
df = pd.DataFrame()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Link('录入', href='/input'),
    dcc.Link('表格', href='/showtable'),
    html.Div(id='app')
])

input_view = html.Div([
    html.Div(
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in ['吃饭', '玩耍', '恋爱']],
            clearable=False,
            placeholder="消费项目",
            id='cata',
            value=''
        )
    ),
    html.Div(
        dcc.Input(
            placeholder='消费金额',
            type='text',
            id='money',
            value=''
        )
    ),
    html.Div([
        html.Button('提交', id='submit'),
        html.P(id='showresult')
    ])
])

showtable_view = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows")
    )
])


@app.callback(
    dash.dependencies.Output('showresult', 'children'),
    [
        dash.dependencies.Input('submit', 'n_clicks')
    ],
    [
        dash.dependencies.State('cata', 'value'),
        dash.dependencies.State('money', 'value')
    ]
)
def input(n_clicks, cata, money):
    return '{},{}'.format(cata, money)


@app.callback(
    dash.dependencies.Output('app', 'children'),
    [
        dash.dependencies.Input('url', 'pathname')
    ]
)
def router(pathname):
    global df
    if pathname == '/':
        return html.H1('主页')
    elif pathname == '/input':
        return input_view
    elif pathname == '/showtable':
        df = pd.read_sql("SELECT * FROM my_account", conn)
        return showtable_view
    elif pathname != '/':
        return html.H1('404 page not found!')


if __name__ == '__main__':
    app.run_server(debug=True)
