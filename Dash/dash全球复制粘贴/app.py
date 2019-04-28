import dash
import dash_core_components as dcc
import dash_html_components as html
import random
from time import sleep

app = dash.Dash(__name__)

the_value = ''

try:
    with open('./database/records.txt', 'r', encoding='utf-8') as f:
        the_value = f.read()
        print('start_value:' + the_value)
except Exception as e:
    print('发生错误：' + e)
    the_value = '默认初始值...'

app.layout = html.Div([
    html.Div([
        html.Button('保存', id='button_save'),
        html.Button('提取', id='button_load')
    ]),
    html.Div(dcc.Textarea(value=the_value, id='textarea1')),
    html.P(id='p1')
])

total_modify_num = 0





@app.callback(
    dash.dependencies.Output('p1', 'children'),
    [
        dash.dependencies.Input('button_save', 'n_clicks')
    ],
    [
        dash.dependencies.State('textarea1', 'value')
    ]
)
def infoSave(n_clicks, value):
    global the_value
    the_value = value
    print('infoSave内部的value：{}'.format(value))
    print('infoSave内部的the_value：{}'.format(the_value))
    global total_modify_num
    total_modify_num += 1
    sleep(5)
    with open('./database/records.txt', 'w', encoding='utf-8') as f:
        f.write(value)
    return total_modify_num







@app.callback(
    dash.dependencies.Output('textarea1', 'value'),
    [
        dash.dependencies.Input('button_load', 'n_clicks')
    ]
)
def infoLoad(n_clicks):
    global the_value
    with open('./database/records.txt', 'r', encoding='utf-8') as f:
        the_value = f.read()
    print('从文件读取了参数，参数值为：{}'.format(the_value))
    sleep(2)
    return the_value








if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(debug=False, port=1122, host='0.0.0.0')
