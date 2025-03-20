print("Hello, World!")

# DESCRIPTION
#I began by creating a test environment with conda. It is called dash_env_test. I then activated it.
#I then created a new file called test-python.py
#I then installed dash and dependencies with "pip install dash pandas plotly"

import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "NYC", "NYC"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8050)




