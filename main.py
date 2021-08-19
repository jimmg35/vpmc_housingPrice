from src.model import Deal, Build, Land, Park
from src.holder import Holder

import pandas as pd 
import numpy as np 


if __name__ == "__main__":
    data = pd.read_csv("data/a_lvr_land_a.csv", encoding="utf8")
    for index, row in data.iterrows():
        deal = Deal.Deal(row)
        # print(index)
        








