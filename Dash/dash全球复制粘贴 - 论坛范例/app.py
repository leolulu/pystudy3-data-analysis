import dash
import dash_core_components as dcc
import dash_html_components as html
import random
from time import sleep

app = dash.Dash(__name__)

notepad_value = ''

with open('./database/records.txt', 'r', encoding='utf-8') as f:
	notepad_value = f.read()

notepad_value = ''

def get_layout():
    global notepad_value
    with open('./database/records.txt', 'r', encoding='utf-8') as f:
        notepad_value = f.read()
    
    return html.Div([
        html.Div([
            html.Button('save', id='button_save'),
            html.Button('load', id='button_load')
        ]),
        html.Div(dcc.Textarea(value=notepad_value, id='textarea1')),
        html.P(id='p1')
    ])

app.layout = get_layout

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
    global notepad_value
    notepad_value = value
    global total_modify_num
    total_modify_num += 1
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
    global notepad_value
    with open('./database/records.txt', 'r', encoding='utf-8') as f:
        notepad_value = f.read()
    return notepad_value

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(debug=False, port=1122, host='0.0.0.0')