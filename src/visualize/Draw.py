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

    source = ColumnDataSource(data={
        'ya':y,
        'rights':right,
        'desc':['A', 'b', 'C', 'd', 'E'],
        'fill_color': fill_color
    })
    TOOLTIPS = [
        ("amount", "@rights"),
    ]

    graph = figure(title = row[1], y_range=y_label,
           toolbar_location=None, tools="hover", tooltips=TOOLTIPS)
    graph.width = 450
    graph.height = 300
    graph.title.text_font_size = '16pt'
    graph.x_range = Range1d(0, x_max)
    # plotting the graph
    graph.hbar(
        y = 'ya',
        right = 'rights',
        height = 0.5,
        fill_color = 'fill_color',
        source = source
    )
    return graph

def drawDeviantRank(countyArray, dataArray, type, color):
    y = [i + 0.5 for i in range(0, len(countyArray))]
    right = list(dataArray)
    fill_color = [color for i in range(0, len(countyArray))]
    y_label = list(countyArray)
    
    source = ColumnDataSource(data={
        'ya':y,
        'rights':right,
        'desc':['A', 'b', 'C', 'd', 'E'],
        'fill_color': fill_color
    })
    TOOLTIPS = [
        ("amount", "@rights"),
    ]

    graph = figure(title = type+"排行", y_range=y_label,
           toolbar_location=None, tools="hover", tooltips=TOOLTIPS)
    graph.width = 450
    graph.height = 800
    graph.title.text_font_size = '16pt'

    graph.yaxis.major_label_text_font_size = "12pt"
    graph.xaxis.major_label_text_font_size = "8pt"
    # plotting the graph
    graph.hbar(
        y = 'ya',
        right = 'rights',
        height = 0.5,
        fill_color = 'fill_color',
        source = source
    )
    return graph




# def drawDeviantGraph(row, x_max):
#     y = [0.5, 1.5, 2.5, 3.5, 4.5]
#     right = [row[2], row[3], row[4], row[5], row[6]]
#     fill_color = ["green", "red", "red", "red", "red"]
#     y_label = ["正常交易量", "異常交易量", "建物型態異常", "夾層異常", "樓中樓異常"]

#     graph = figure(title = row[1], y_range=y_label,
#            toolbar_location=None, tools="hover", tooltips="@$right")
#     graph.width = 450
#     graph.height = 300
#     graph.title.text_font_size = '16pt'
#     graph.x_range = Range1d(0, x_max)
#     # plotting the graph
#     graph.hbar(
#         y,
#         height = 0.5,
#         right = right,
#         fill_color = fill_color
#     )
#     return graph