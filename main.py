
from src.holder import Holder

from src.model.Deal import Deal
from src.model.Build import Build
from src.model.Land import Land
from src.model.Park import Park

import pandas as pd 
import numpy as np 

from typing import List


def readDealFile(path: str) -> List[Deal]:
    output: List[Deal] = []
    data = pd.read_csv(path, encoding="utf8")
    for index, row in data.iterrows():
        output.append(Deal(row))
    return output


if __name__ == "__main__":

    dealArrays = readDealFile("data/a_lvr_land_a.csv")
        








