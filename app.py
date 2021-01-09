import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
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

# Spending table
df_transposed = df.T
df_transposed = df_transposed.reset_index()
df_transposed.columns = ['Category', 'Sep', 'Oct', 'Nov']
df_transposed['Avg'] = df_transposed.mean(axis=1).round(2)
df_transposed['Avg/y'] = df_transposed.mean(axis=1).round(2)  # TODO: Use real data instead of the same 3 months
print(df_transposed)

spending_graph = px.histogram(df_spending_transformed, x="Date", y="Value", color='Type',
                              barmode='group', title='Net spending last 6 months')
spending_graph.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
spending_graph.update_layout(legend_title_text='')
spending_graph.update_layout(yaxis_title='')
spending_graph.update_layout(xaxis_title='')

app.layout = html.Div(children=[
    html.Div(
        className="app-header",
        children=[
            html.Div('Personal Finance Dashboard v0.1.1', className="app-header--title")
        ]
    ),
    html.Div(className='row',  # Define the row element
             children=[
                 html.Div(className='five columns div-user-controls', children=[
                     html.Div(className='rounded-div negative-top-margin', children=[
                         html.H1('Hello, Juho!')
                         ]),
                     html.Div(className='rounded-div', children=[
                         html.Div('Your net income for last month was'),
                         html.Div(className='net-spending', children=[
                            html.Div(f"+{df_netspending_transformed.at[0, 'Value']}")
                         ]),
                         html.Div(className='total-amounts', children=[
                             html.Div(f"Total income: {df_spending_transformed.at[0, 'Value']} ",
                                      style={'width': '49%', 'display': 'inline-block'}),
                             html.Div(f"Total spending: {df_spending_transformed.at[1, 'Value']}",
                                      style={'width': '49%', 'display': 'inline-block'})
                         ])
                     ]),
                     html.Div(className='rounded-div-table', children=[
                        dcc.Graph(id='spending_graph', figure=spending_graph)
                     ])
                 ]),  # Define the left element
                 html.Div(className='six columns div-for-charts bg-grey rounded-div add-top-margin', children=[
                     dash_table.DataTable(

                         id='table',
                         columns=[{"name": i, "id": i}
                                  for i in df_transposed.columns],
                         data=df_transposed.to_dict('records'),
                         style_cell=dict(textAlign='center', font_size='20px'),
                         style_cell_conditional=[
                             {
                                 'if': {'column_id': 'Category'},
                                 'textAlign': 'left'
                             }
                         ],
                         style_header=dict(backgroundColor="#FFFFFF"),
                         style_data=dict(backgroundColor="#FFFFFF")
                     )
                 ])  # Define the right element
             ])
])

# app.layout = html.Div([
#     html.Div(
#         className="app-header",
#         children=[
#             html.Div('Personal Finance Dashboard v0.1', className="app-header--title")
#         ]
#     ),
#     html.Div(
#         children=html.Div([
#             html.H2('Hello, Juho!'),
#             html.Br(),
#             dcc.Markdown(f"Your net income for last month was **{df_netspending_transformed.at[0, 'Value']}**"),
#             # html.H2(f"{df_netspending_transformed.at[0, 'Value']}"),
#             html.Div(f"Total income: {df_spending_transformed.at[0, 'Value']} "),
#             html.Div(f"Total spending: {df_spending_transformed.at[1, 'Value']}")
#         ])
#     ),
#
#     html.Div(children=[
#         dcc.Graph(id='spending_graph', figure=spending_graph, style={'display': 'inline-block'}),
#         dash_table.DataTable(
#             id='table',
#             columns=[{"name": i, "id": i}
#                      for i in df_transposed.columns],
#             data=df_transposed.to_dict('records'),
#             style_cell=dict(textAlign='left'),
#             style_header=dict(backgroundColor="paleturquoise"),
#             style_data=dict(backgroundColor="lavender")
#         )
#     ])
# ])


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
