
from src.holder import Holder

from src.model.Deal import Deal
from src.model.Build import Build
from src.model.Land import Land
from src.model.Park import Park

from src.holder.Holder import Holder
from src.holder.HolderArray import HolderArray 

import pandas as pd 
import numpy as np 

from typing import List
import os 
from os import error, listdir


def readFile(path: str, type: str) -> List[Deal]:
    output: List[Deal] = []
    data = pd.read_csv(path, encoding="utf8")
    for index, row in data.iterrows():
        instance = None
        if type == "Deal":
            instance = Deal(row)
        elif type == "Build":
            instance = Build(row)
        elif type == "Land":
            instance = Land(row)
        elif type == "Park":
            instance = Park(row)
        output.append(instance)
    return output

def structureHolder(dealArrays: List[Deal], buildArrays: List[Build],
                    landArrays: List[Land], parkArrays: List[Park]) -> List[Holder]:
    output: HolderArray = HolderArray()
    # output: List[Holder] = []
    for deal in dealArrays:
        holder = Holder(deal)
        for build in buildArrays:
            if build.serialNumber == deal.serialNumber:
                holder.builds.append(build)
        for land in landArrays:  
            if land.serialNumber == deal.serialNumber:
                holder.lands.append(land)
        for park in parkArrays:  
            if park.serialNumber == deal.serialNumber:
                holder.parks.append(park)
        holder.startUp()
        output.contents.append(holder)
    return output

def readBatchFile(path: str):
    totalStatsChunk = []
    for county in listdir(path):
        countyFilePath = os.path.join(path, county)
        entityDict = {}
        # reading four essential files
        for filename in listdir(countyFilePath):
            filePath = os.path.join(countyFilePath, filename)
            fileType = "Deal"
            if "build" in filename:
                fileType = "Build"
            if "land" in filename:
                fileType = "Land"
            if "park" in filename:
                fileType = "Park"
            # print(filePath, fileType)
            entityArray = readFile(filePath, fileType)
            entityDict[fileType] = entityArray
        # pack into holder array
        holderArray: HolderArray = structureHolder(entityDict["Deal"], entityDict["Build"], entityDict["Land"], entityDict["Park"])
        holderArray.status(county)
        statsChunk = holderArray.exportDeviantStatistic(county)
        holderArray.exportDeviantCases("deviantCases", county)
        totalStatsChunk.append(statsChunk)
    return totalStatsChunk
        
def outputDeviantTable(data, path, filename):
    if os.path.exists(path) == False:
        os.mkdir(path)
    
    countyEngZhDict = {
        "Changhua": "彰化",
        "ChiayiCity": "嘉義市",
        "ChiayiCounty": "嘉義縣",
        "HsinchuCity": "新竹市",
        "HsinchuCounty": "新竹縣",
        "Hualien": "花蓮",
        "Kaohsiung": "高雄",
        "Keelung": "基隆",
        "Kinmen": "金門",
        "Miaoli": "苗栗",
        "Nantou": '南投',
        "NewTaipei": "新北",
        "Penghu": "澎湖", 
        "Pingtung": "屏東",
        "Taichung": "臺中",
        "Tainan": "臺南",
        "Taipei": "臺北",
        "Taitung":"臺東",
        "Taoyuan":"桃園",
        "Yilan":"宜蘭",
        "Yunlin":"雲林",
    }

    sheet = []
    for row in data:
        sheet.append([
            countyEngZhDict[row["county"]], 
            row["data"][0], 
            row["data"][1], 
            row["data"][2], 
            row["data"][3], 
            row["data"][4]
        ])
    
    np_sheet = np.array(sheet)
    df = pd.DataFrame(data=np_sheet, columns=data[0]["column"])
    df.to_csv(os.path.join(path, filename), encoding="utf-8-sig")
            


if __name__ == "__main__":
    totalStatsChunk = readBatchFile("data")
    outputDeviantTable(totalStatsChunk, "deviantStats", "deviantStats.csv")








































    
    # dealArrays = readFile("data/Taipei/a_lvr_land_a.csv", "Deal")
    # buildArrays = readFile("data/Taipei/a_lvr_land_a_build.csv", "Build")
    # landArrays = readFile("data/Taipei/a_lvr_land_a_land.csv", "Land")
    # parkArrays = readFile("data/Taipei/a_lvr_land_a_park.csv", "Park")

    # dealArrays = readFile("data/Taichung/b_lvr_land_a.csv", "Deal")
    # buildArrays = readFile("data/Taichung/b_lvr_land_a_build.csv", "Build")
    # landArrays = readFile("data/Taichung/b_lvr_land_a_land.csv", "Land")
    # parkArrays = readFile("data/Taichung/b_lvr_land_a_park.csv", "Park")

    # dealArrays = readFile("data/Keelung/deal.csv", "Deal")
    # buildArrays = readFile("data/Keelung/build.csv", "Build")
    # landArrays = readFile("data/Keelung/land.csv", "Land")
    # parkArrays = readFile("data/Keelung/park.csv", "Park")

    # holderArray: HolderArray = structureHolder(dealArrays, buildArrays, landArrays, parkArrays)
    # holderArray.status("Keelung")
    # holderArray.exportDeviantCases("deviantCases", "Keelung")

    


        








