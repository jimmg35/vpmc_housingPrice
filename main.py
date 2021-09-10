
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


if __name__ == "__main__":

    # dealArrays = readFile("data/Taipei/a_lvr_land_a.csv", "Deal")
    # buildArrays = readFile("data/Taipei/a_lvr_land_a_build.csv", "Build")
    # landArrays = readFile("data/Taipei/a_lvr_land_a_land.csv", "Land")
    # parkArrays = readFile("data/Taipei/a_lvr_land_a_park.csv", "Park")

    # dealArrays = readFile("data/Taichung/b_lvr_land_a.csv", "Deal")
    # buildArrays = readFile("data/Taichung/b_lvr_land_a_build.csv", "Build")
    # landArrays = readFile("data/Taichung/b_lvr_land_a_land.csv", "Land")
    # parkArrays = readFile("data/Taichung/b_lvr_land_a_park.csv", "Park")

    dealArrays = readFile("data/Keelung/c_lvr_land_a.csv", "Deal")
    buildArrays = readFile("data/Keelung/c_lvr_land_a_build.csv", "Build")
    landArrays = readFile("data/Keelung/c_lvr_land_a_land.csv", "Land")
    parkArrays = readFile("data/Keelung/c_lvr_land_a_park.csv", "Park")


    holderArray: HolderArray = structureHolder(dealArrays, buildArrays, landArrays, parkArrays)
    holderArray.status()


    # for i in holderArray.contents:
    #     if i.totalLevelIsDeviant:
    #         try:
    #             print(i.parsedTotalLevel, i.deal.buildingState)
    #         except:
    #             continue

        








