import dash
import dash_core_components as dcc
import dash_html_components as html
import random

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(dcc.Textarea(placeholder='请输入候选项，每行一个...',id='textarea1')),
    html.Div(html.Button('开始选择',id='button1')),
    html.Div(html.P(id='p1'))
])




@app.callback(
    dash.dependencies.Output('p1', 'children'),
    [
        dash.dependencies.Input('button1', 'n_clicks')
    ],
    [
        dash.dependencies.State('textarea1','value')
    ]
)
def showProcessImg(n_clicks,value):
    line_list = value.split('\n')
    print(line_list)
    return random.sample(line_list,1)


if __name__ == '__main__':
    app.run_server(debug=True)
