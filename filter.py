
# from src.holder import Holder
# from src.model.Deal import Deal
# from src.model.Build import Build
# from src.model.Land import Land
# from src.model.Park import Park

# from src.holder.Holder import Holder
from src.holder.HolderArray import HolderArray 

# import pandas as pd 
# import numpy as np 

# from typing import List
# import os 
# from os import error, listdir

from src.util.util import readFile, structureHolder, outputCases, outputDeviantTable, initCountyFolder

       


if __name__ == "__main__":


    # 輸出異常交易報表與資料
    # totalStatsChunk = outputCases("data", "deviantCases", deviant=True)
    # outputDeviantTable(totalStatsChunk, "deviantStats", "deviantStats.csv")

    # 輸出正常交易資料
    # initCountyFolder("data/normalCases", useCountyName=False)
    # outputCases("data/mergeData", "normalCases", deviant=False) 

    

    dealArrays = readFile("data/mergeData/a/deal.csv", "Deal")
    buildArrays = readFile("data/mergeData/a/build.csv", "Build")
    landArrays = readFile("data/mergeData/a/land.csv", "Land")
    parkArrays = readFile("data/mergeData/a/park.csv", "Park")

    holderArray: HolderArray = structureHolder(dealArrays, buildArrays, landArrays, parkArrays)
    holderArray.status("a")
    # holderArray.exportDeviantCases("deviantCases", "Taoyuan")

    


        








