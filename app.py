import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

app = dash.Dash(__name__)
server = app.server

app.title = 'Personal Finance Dashboard'

df = pd.read_csv('ExampleCleaned.csv', ';', index_col=0, parse_dates=True)  # Set file location
print(df)

# Net spending information
df_net_spending = df[['Personal']]
df_net_spending_transformed = pd.DataFrame(df_net_spending.stack()).reset_index()
df_net_spending_transformed.columns = ['Date', 'Type', 'Value']
print(df_net_spending_transformed)

# Spending graph
df_spending = df.tail(6)
df_spending = df_spending[['Total income', 'Total spent']]
df_spending_transformed = pd.DataFrame(df_spending.stack()).reset_index()
df_spending_transformed.columns = ['Date', 'Type', 'Value']
print(df_spending_transformed)

# Income table
df_income_table = df.tail(3).T  # Grab the last 3 months and transpose the table
df_income_table = df_income_table.reset_index()
df_income_table = df_income_table[3:6]  # Grab the income related entries
df_copy = df.tail(3)
df_income_table.columns = ['Income', pd.to_datetime(df_copy.index[0]).strftime('%b'), pd.to_datetime(df_copy.index[1])
    .strftime('%b'), pd.to_datetime(df_copy.index[2]).strftime('%b')]
df_income_table['Avg'] = df_income_table.mean(axis=1).round(2)  # Calculate the averages for the three months
df_income_table['Avg/y'] = df.tail(12).T.reset_index().mean(axis=1).round(2)  # Calculate averages for the whole year
print(df_income_table)

# Spending table
df_transposed = df.tail(3).T
df_transposed = df_transposed.reset_index()
df_transposed = df_transposed.tail(8)
df_transposed.columns = ['Spending', pd.to_datetime(df_copy.index[0]).strftime('%b'), pd.to_datetime(df_copy.index[1])
    .strftime('%b'), pd.to_datetime(df_copy.index[2]).strftime('%b')]
df_transposed['Avg'] = df_transposed.mean(axis=1).round(2)
df_transposed['Avg/y'] = df.tail(12).T.reset_index().mean(axis=1).round(2)
print(df_transposed)

spending_graph = px.histogram(df_spending_transformed, x="Date", y="Value", color='Type',
                              barmode='group', title='', nbins=6)
spending_graph.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), legend_title_text='', yaxis_title='', xaxis_title='', margin=dict(t=0, b=0, l=0, r=30))

app.layout = html.Div(children=[
    html.Div(
        className="app-header",
        children=[
            html.Div(children=[
                html.Div('Personal Finance Dashboard v0.3.1', className="app-header--title",
                         style={'display': 'inline-block'}),
                html.Div('(Python, Pandas & Dash)',
                         style={'display': 'inline-block', 'padding-left': '5px'})
            ])
        ]
    ),
    html.Div(className='row',  # Define the row element
             children=[
                 html.Div(className='five columns div-user-controls', children=[  # Left side
                     html.Div(className='rounded-div negative-top-margin', children=[
                         html.H1('Hello, Juho!')
                     ]),
                     html.Div(className='rounded-div', children=[
                         html.Div('Your personal spending for last month was'),
                         html.Div(className='net-spending', children=[
                             html.Div(f"-{df_net_spending_transformed['Value'].iloc[-1]}")
                         ]),
                         html.Div(className='total-amounts', children=[
                             html.Div(
                                 f"Total income: {df_spending_transformed['Value'].iloc[len(df_spending_transformed) - 2]} ",
                                 style={'width': '49%', 'display': 'inline-block'}),
                             html.Div(f"Total spending: {df_spending_transformed['Value'].iloc[-1]}",
                                      style={'width': '49%', 'display': 'inline-block'})
                         ])
                     ]),
                     html.Div(className='rounded-div-graph', children=[
                         html.H2('Net spending last 6 months', className='graph-title'),
                         dcc.Graph(id='spending_graph', figure=spending_graph)
                     ])
                 ]),
                 html.Div(className='six columns div-for-charts add-top-margin', children=[  # Right side
                     html.Div(className='rounded-div', children=[
                         html.Div(children=[
                             dash_table.DataTable(

                                 id='income-table',
                                 columns=[{"name": i, "id": i}
                                          for i in df_income_table.columns],
                                 data=df_income_table.to_dict('records'),
                                 style_cell=dict(textAlign='center', font_size='20px'),
                                 style_cell_conditional=[
                                     {
                                         'if': {'column_id': 'Income'},
                                         'font-family': "sans-serif",
                                         'textAlign': 'left',
                                         'width': '180px'
                                     }
                                 ],
                                 style_header=dict(backgroundColor="#FFFFFF", font_family='sans-serif',
                                                   fontWeight='bold'),
                                 style_data=dict(backgroundColor="#FFFFFF", font_family='sans-serif'),
                                 cell_selectable=False
                             )
                         ]),
                         html.Br(),
                         html.Div(children=[
                             dash_table.DataTable(

                                 id='spending-table',
                                 columns=[{"name": i, "id": i}
                                          for i in df_transposed.columns],
                                 data=df_transposed.to_dict('records'),
                                 style_cell=dict(textAlign='center', font_size='20px'),
                                 style_cell_conditional=[
                                     {
                                         'if': {'column_id': 'Spending'},
                                         'font-family': "sans-serif",
                                         'textAlign': 'left',
                                         'width': '180px'
                                     }
                                 ],
                                 style_header=dict(backgroundColor="#FFFFFF", font_family='sans-serif',
                                                   fontWeight='bold'),
                                 style_data=dict(backgroundColor="#FFFFFF", font_family='sans-serif'),
                                 cell_selectable=False
                             )
                         ])
                     ]),
                     html.Div(className='rounded-div', children=[
                         html.P(['This is a demo version of the dashboard. The data shown is gathered from a student '
                                 'household. The dashboard tracks the household account so personal income here stands '
                                 'for the amount of money that one has transferred to the household account from his '
                                 'personal account. Thus, the personal spending meter is a bit useless in this '
                                 'scenario but it exists for other use cases.', html.Br(), html.Br(), html.Br(),
                                 'Check out my Github for other projects at ', html.Br(),
                                 html.A('https://github.com/Eltore', href='https://github.com/Eltore')
                                 ]),
                     ])
                 ])
             ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
