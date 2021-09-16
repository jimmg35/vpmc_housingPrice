from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.layouts import row, column
from bokeh.models import Range1d
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure

def drawDeviantGraph(row, x_max):
    y = [0.5, 1.5, 2.5, 3.5, 4.5]
    right = [row[2], row[3], row[4], row[5], row[6]]
    fill_color = ["green", "red", "red", "red", "red"]
    y_label = ["正常交易量", "異常交易量", "建物型態異常", "夾層異常", "樓中樓異常"]

    graph = figure(title = row[1], y_range=y_label)
    graph.width = 450
    graph.height = 300
    graph.title.text_font_size = '16pt'
    graph.x_range = Range1d(0, x_max)
    # plotting the graph
    graph.hbar(
        y,
        height = 0.5,
        right = right,
        fill_color = fill_color
    )
    return graph