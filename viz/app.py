import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from etl.load import get_data

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("API Data Dashboard"),
    
    # Dropdown for selecting chart type
    dcc.Dropdown(
        id='chart-type',
        options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Pie Chart', 'value': 'pie'}
        ],
        value='bar'
    ),
    
    # Graph component
    dcc.Graph(id='data-chart'),
    
    # Data table
    html.H2("Data Table"),
    html.Div(id='data-table')
])

# Callback to update the chart
@app.callback(
    dash.Output('data-chart', 'figure'),
    dash.Input('chart-type', 'value')
)
def update_chart(chart_type):
    # Get data from database
    df = get_data()
    if df is None or df.empty:
        return px.scatter(title="No data available")
    
    # Create chart based on type (customize based on your data structure)
    if chart_type == 'bar':
        # Assuming 'id' and 'title' columns exist (from JSONPlaceholder example)
        if 'id' in df.columns and 'title' in df.columns:
            fig = px.bar(df, x='id', y=df.select_dtypes(include=[int, float]).columns[0] if len(df.select_dtypes(include=[int, float]).columns) > 0 else 'id', title="Bar Chart")
        else:
            fig = px.bar(df.head(), title="Sample Bar Chart")
    elif chart_type == 'line':
        fig = px.line(df, x=df.columns[0], y=df.select_dtypes(include=[int, float]).columns[:3] if len(df.select_dtypes(include=[int, float]).columns) >= 3 else df.columns[:3], title="Line Chart")
    elif chart_type == 'scatter':
        fig = px.scatter(df, x=df.columns[0], y=df.columns[1] if len(df.columns) > 1 else df.columns[0], title="Scatter Plot")
    elif chart_type == 'pie':
        fig = px.pie(df, names=df.columns[0], values=df.columns[1] if len(df.columns) > 1 else df.columns[0], title="Pie Chart")
    
    return fig

# Callback to update the data table
@app.callback(
    dash.Output('data-table', 'children'),
    dash.Input('chart-type', 'value')
)
def update_table(chart_type):
    df = get_data()
    if df is None:
        return html.P("No data available")
    
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), 10))  # Show first 10 rows
        ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)