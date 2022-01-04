# importing the modules
import numpy as np
import bokeh
from bokeh.plotting import figure, output_file, show
bokeh.sampledata.download()
from bokeh.sampledata.stocks import AAPL, FB, GOOG, IBM, MSFT


# the file to save the model
#output_file("te.html")
   
# instantiating the figure object
graph = figure(x_axis_type = "datetime", title = "Stock Closing Prices")
   
# x-axis
graph.xaxis.axis_label = 'Date'
   
# y-axis
graph.yaxis.axis_label = 'Price (in USD)'
   
# plotting AAPL
x_axis_coordinates = np.array(AAPL['date'], dtype = np.datetime64)
y_axis_coordinates = AAPL['adj_close']
color = "lightblue"
legend_label = 'AAPL'
graph.line(x_axis_coordinates,
        y_axis_coordinates,
        color = color,
        legend_label = legend_label)
   
# plotting FB
x_axis_coordinates = np.array(FB['date'], dtype = np.datetime64)
y_axis_coordinates = FB['adj_close']
color = "black"
legend_label = 'FB'
graph.line(x_axis_coordinates,
        y_axis_coordinates,
        color = color,
        legend_label = legend_label)
   
# plotting GOOG
x_axis_coordinates = np.array(GOOG['date'], dtype = np.datetime64)
y_axis_coordinates = GOOG['adj_close']
color = "orange"
legend_label = 'GOOG'
graph.line(x_axis_coordinates,
        y_axis_coordinates,
        color = color,
        legend_label = legend_label)
   
# plotting IBM
x_axis_coordinates = np.array(IBM['date'], dtype = np.datetime64)
y_axis_coordinates = IBM['adj_close']
color = "darkblue"
legend_label = 'IBM'
graph.line(x_axis_coordinates,
        y_axis_coordinates,
        color = color,
        legend_label = legend_label)
   
# plotting  MSFT
x_axis_coordinates = np.array(MSFT['date'], dtype = np.datetime64)
y_axis_coordinates = MSFT['adj_close']
color = "yellow"
legend_label = 'MSFT'
graph.line(x_axis_coordinates,
        y_axis_coordinates,
        color = color,
        legend_label = legend_label)
   
# relocating the legend table to 
# avoid abstruction of the graph
graph.legend.location = "top_left"
   
# displaying the model
show(graph)
