from plotly.graph_objs import Scatter, Layout
from plotly import offline

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
data = [Scatter(x=rw.x_values, y=rw.y_values, mode='markers')]
x_axis_config = {'showgrid': False, 'zeroline': False, 'visible': False}
y_axis_config = {'showgrid': False, 'zeroline': False, 'visible': False}
my_layout = Layout(title='Random Walk', 
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='rw.html')