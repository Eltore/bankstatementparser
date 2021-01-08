import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv('.data/analyzerOutput.csv', ';', index_col=0, parse_dates=True)
print(df)

# Net spending information
df_netspending = df
df_netspending = df_netspending[['Net income']]
df_netspending_transformed = pd.DataFrame(df_netspending.stack()).reset_index()
df_netspending_transformed.columns = ['Date', 'Type', 'Value']
print(df_netspending_transformed)

# Spending graph
df_spending = df
df_spending = df_spending[['Total income', 'Total spent']]
df_spending_transformed = pd.DataFrame(df_spending.stack()).reset_index()
df_spending_transformed.columns = ['Date', 'Type', 'Value']
print(df_spending_transformed)

spending_graph = px.line(df_spending_transformed, x="Date", y="Value", color='Type', title='Net spending last 6 months')

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Personal Finance Dashboard v0.1', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H2('Hello, Juho!'),
            html.Br(),
            dcc.Markdown(f"Your net income for last month was **{df_netspending_transformed.at[0, 'Value']}**"),
            # html.H2(f"{df_netspending_transformed.at[0, 'Value']}"),
            html.Div(f"Total income: {df_spending_transformed.at[0, 'Value']} "),
            html.Div(f"Total spending: {df_spending_transformed.at[1, 'Value']}")
        ])
    ),

    dcc.Graph(id='spending_graph', figure=spending_graph)
])


# @app.callback(
#     [Output(component_id='output_container', component_property='children'),
#      Output(component_id='net_spending_graph', component_property='figure')],
#     [Input(component_id='slct_year', component_property='value')]
# )
# def update_graph():
#     dff = df.Copy()
#     dff = dff[dff['Total income', 'Total spent']]
#     df3 = pd.DataFrame(dff.stack()).reset_index()
#     df3.columns = ['Date', 'Type', 'Value']
#     fig = px.line(df, x="Date", y="Value", color='Type')
#
#     return fig


if __name__ == '__main__':
    app.run_server(debug=True)
