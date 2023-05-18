import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as mp



xdata = np.random.randint(1,30,50)
ydata = np.random.randint(1,30,50)

fig = go.Figure(data= go.Bar(x=xdata, y=ydata))
fig.show()