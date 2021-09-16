import pandas as pd 
import numpy as np 
from src.visualize.Draw import drawDeviantGraph
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.layouts import row, column
from bokeh.models import Range1d
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure


totalGraph = []
df = pd.read_csv("deviantStats/deviantStats.csv")
df = df.sort_values(by=["正常交易量"], ascending=False)

for i in range(df.shape[0]):
    graph = drawDeviantGraph(df.iloc[i,:], df["正常交易量"].max())
    totalGraph.append(graph)


total = []
counts = 0
for i in range(0, 6):
    myRow = []
    for j in range(0, 4):
        try:
            myRow.append(totalGraph[counts])
            counts+=1
        except:
            continue
    total.append(row(myRow))
show(column(total))