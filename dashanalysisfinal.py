import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample Data
df = px.data.gapminder()

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Gapminder Data Dashboard"),
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': c, 'value': c} for c in df['continent'].unique()],
        value='Asia'
    ),
    dcc.Graph(id='life-exp-vs-gdp'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

# Define callbacks
@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    [Input('continent-dropdown', 'value'),
     Input('year-slider', 'value')]
)
def update_graph(selected_continent, selected_year):
    filtered_df = df[(df['continent'] == selected_continent) & (df['year'] == selected_year)]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop', color='country',
                     hover_name='country', log_x=True, size_max=55,
                     title=f'Life Expectancy vs GDP per Capita ({selected_year})')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
