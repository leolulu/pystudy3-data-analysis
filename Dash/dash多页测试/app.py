import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import requests
from lxml import etree

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Link('页面1 ', href='/page1'),
    dcc.Link('页面2', href='/page2'),
    html.H1(id='show'),
])

layout_page1 = html.Div([
    html.H1('这个是页面1的页面'),

    html.Div(
        dcc.Input(id='input-box', type='text'),
    ),
    html.Button('Submit', id='sbutton', title='点击提交!'),
    html.Div(id='page1-info')
])

layout_page2 = html.Div([
    html.H1('这个是页面2的页面'),

    html.Div(dcc.Textarea(id='textarea1')),    
    dcc.Input(id='input2',type='text'),
    html.Button('Submit', id='button2', title='点击获取资料'),
    html.Div(html.P(id='thep'))

])

@app.callback(
    dash.dependencies.Output('textarea1','value'),
    [dash.dependencies.Input('button2','n_clicks')],
    [dash.dependencies.State('input2','value')],
)
def diyBaidu(n_clicks,keyword):
    url = "http://www.baidu.com/s?wd={}".format(keyword)
    content = requests.get(url).content
    result = etree.HTML(content).xpath("//div[contains(@class,'result c-container')]/h3/a/text()")
    return result


@app.callback(
    dash.dependencies.Output('page1-info','children'),
    [dash.dependencies.Input('sbutton','n_clicks')]
)
def showPage1Ifno(info1):
    return info1



@app.callback(
    dash.dependencies.Output('show', 'children'),
    [dash.dependencies.Input('url', 'pathname')]
)
def showurl(pathname):
    if pathname == '/':
        return html.H1('这是主页')
    if pathname == '/page1':
        return layout_page1
    if pathname == '/page2':
        return layout_page2
    else:
        return html.H1('404 note found!')


app.run_server(debug=True)
