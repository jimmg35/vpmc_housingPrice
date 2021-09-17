import pandas as pd 
import numpy as np 
from src.visualize.Draw import drawDeviantGraph, drawDeviantRank
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.layouts import row, column
from bokeh.models import Range1d
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure


# # # # # # # # #
# 顯示各縣市交易紀錄情形
def visualizeDeviant():
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


# # # # # # # # #
# 顯示單一種類交易排行
def visualizeTypeRank(type, color):  #"正常交易量"
    df = pd.read_csv("deviantStats/deviantStats.csv")
    df = df.sort_values(by=[type], ascending=True)
    graph = drawDeviantRank(df["縣市"], df[type], type, color)
    return graph


if __name__ == "__main__":
    
    graphSet = [visualizeTypeRank(i[0], i[1]) for i in [
            ("正常交易量", "green"), 
            ("異常交易量", "red"), 
            ("建物型態異常", "red"), 
            ("夾層異常", "red"), 
            ("樓中樓異常", "red")
        ]
    ]
    show(row(graphSet))