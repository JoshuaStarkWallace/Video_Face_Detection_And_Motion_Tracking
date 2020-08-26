from motiontracker import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=100, width=500, responsive=True, title="Motion Graph")
p.yaxis.minor_tick_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])

q = p.quad(left="Start", right="End", bottom=0, top=1, color="blue", source=cds)

output_file("Graph.html")
show(p)
