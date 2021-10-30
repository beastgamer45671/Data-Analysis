import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data_csv")

print(df.groupby("Level")["Attempt"].mean())

fig = go.Figure(go.Scatter(
    x = df.groupby("Level")["Attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = 'h'))

fig.show()