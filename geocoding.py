from src.model.Deal import Deal
from src.util.util import readFile, initCountyFolder
from src.geocoding.Geocoding import GeoCoder
import pandas as pd
import numpy as np
import os

if __name__ == "__main__":

    dealOutputCsvColumn = ["鄉鎮市區","交易標的","土地位置建物門牌","土地移轉總面積平方公尺","都市土地使用分區","非都市土地使用分區","非都市土地使用編定","交易年月日","交易筆棟數","移轉層次",	"總樓層數",	"建物型態"	,"主要用途"	,"主要建材",	"建築完成年月",	"建物移轉總面積平方公尺",	"建物現況格局-房",	"建物現況格局-廳",	"建物現況格局-衛",	"建物現況格局-隔間",	"有無管理組織",	"總價元",	"單價元平方公尺",	"車位類別",	"車位移轉總面積(平方公尺)",	"車位總價元",	"備註",	"編號",	"主建物面積",	"附屬建物面積",	"陽台面積",	"電梯",	"移轉編號", "longitude", "latitude"]

    initCountyFolder("geocodedCases")

    myCoder = GeoCoder("./config/geocoding.json")

    dealArrays = readFile("data/Taoyuan/deal.csv", "Deal")


    dealTableData = []
    for deal in dealArrays:
        x, y = myCoder.address2Geolocation(deal.address)
        deal.longitude = x
        deal.latitude = y
        
        dealTableData.append(
            deal.outputRow_geocoded()
        )
        print(x, y, deal.address)
    
    # 輸出geocoded的表
    deviantDeals = pd.DataFrame(np.array(dealTableData), columns=dealOutputCsvColumn)
    deviantDeals.to_csv(os.path.join("geocodedCases", "Taoyuan", "geocodedCases.csv"), encoding="utf-8-sig")
    

