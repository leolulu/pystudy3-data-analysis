import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from readdb import getData

app = dash.Dash(__name__)

data = getData("SELECT * FROM `new_stock`")

app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in data.columns],
        data=data.to_dict('records')
    )
])

if __name__ == '__main__':
    app.run_server()