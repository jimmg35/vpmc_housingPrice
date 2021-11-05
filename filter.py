
# from src.holder import Holder
# from src.model.Deal import Deal
# from src.model.Build import Build
# from src.model.Land import Land
# from src.model.Park import Park

# from src.holder.Holder import Holder
# from src.holder.HolderArray import HolderArray 

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
    initCountyFolder("normalCases")
    outputCases("data", "normalCases", deviant=False) 

    

    # dealArrays = readFile("data/Taoyuan/deal.csv", "Deal")
    # buildArrays = readFile("data/Taoyuan/build.csv", "Build")
    # landArrays = readFile("data/Taoyuan/land.csv", "Land")
    # parkArrays = readFile("data/Taoyuan/park.csv", "Park")

    # holderArray: HolderArray = structureHolder(dealArrays, buildArrays, landArrays, parkArrays)
    # holderArray.status("Taoyuan")
    # holderArray.exportDeviantCases("deviantCases", "Taoyuan")

    


        








