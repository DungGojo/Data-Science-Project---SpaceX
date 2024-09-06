# Import required libraries
import pandas as pd
import dash
from dash import dcc, html  # Updated imports for Dash v2+
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Extract unique Launch Sites
launch_sites = spacex_df['Launch Site'].unique()

# Create a Dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Add a dropdown list to enable Launch Site selection
    dcc.Dropdown(id='site-dropdown',
                 options=[{'label': 'All Sites', 'value': 'ALL'}] + 
                         [{'label': site, 'value': site} for site in launch_sites],
                 value='ALL',  # Default value is 'ALL'
                 placeholder="Select a Launch Site",
                 searchable=True),
    
    html.Br(),
    
    # TASK 2: Pie chart for total successful launches count
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    # TASK 3: Payload range slider
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(id='payload-slider',
                    min=min_payload, max=max_payload, step=100,
                    marks={int(i): str(int(i)) for i in range(int(min_payload), int(max_payload)+1, 1000)},
                    value=[min_payload, max_payload]),
    
    # TASK 4: Scatter chart for payload and success correlation
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2: Pie chart callback
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, 
                     values='class', 
                     names='Launch Site', 
                     title='Total Success Launches for All Sites')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        
        fig = px.pie(filtered_df, 
                     names='class',  
                     title=f"Success vs. Failed Launches for {entered_site}")
    return fig

# TASK 4: Scatter plot callback
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value'))
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & 
                            (spacex_df['Payload Mass (kg)'] <= high)]
    
    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]

    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                     color='Booster Version Category', 
                     title=f'Payload vs. Outcome for {entered_site if entered_site != "ALL" else "All Sites"}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(port=8080)


# Terminal : 
# python3.11 -m pip install pandas dash
# wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
# wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/spacex_dash_app.py"
# To run file : python3.11 spacex_dash_app.py