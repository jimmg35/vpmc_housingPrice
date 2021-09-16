
from .Holder import Holder

import os
import numpy as np
import pandas as pd
from typing import List
from colorama import init, Fore, Back, Style
init(convert=True)

class HolderArray():
    contents: List[Holder]

    def __init__(self):
        self.contents = []
    
    def status(self, county):
        self.normal = []
        self.deviants = []
        self.totalLevelDeviants = []
        self.shiftingLevelMezzanineDeviants = []
        self.shiftingLevelDuplexDeviants = []
        for index, holder in enumerate(self.contents):
            if holder.dealIsDeviant:
                self.deviants.append(holder)
            else:
                self.normal.append(holder)
            
            if holder.totalLevelIsDeviant:
                self.totalLevelDeviants.append(holder)

            if holder.shiftingLevelMezzanineIsDeviant:
                self.shiftingLevelMezzanineDeviants.append(holder)

            if holder.shiftingLevelDuplexIsDeviant:
                self.shiftingLevelDuplexDeviants.append(holder)

        print(Style.RESET_ALL + Fore.WHITE + f"\n===================== {county} =====================" + Style.RESET_ALL)
        print(Style.RESET_ALL + Fore.GREEN + f" 正常交易量             : {len(self.normal)}" + Style.RESET_ALL)
        print(Style.RESET_ALL + Fore.RED + f" 異常交易量             : {len(self.deviants)}")
        print(f" 建物型態異常          : {len(self.totalLevelDeviants)}")
        print(f" 夾層異常               : {len(self.shiftingLevelMezzanineDeviants)}")
        print(f" 樓中樓異常             : {len(self.shiftingLevelDuplexDeviants)}" + Style.RESET_ALL)

    def exportDeviantStatistic(self, county):
        return {
            "county" : county,
            "data" : [
                len(self.normal),
                len(self.deviants),
                len(self.totalLevelDeviants),
                len(self.shiftingLevelMezzanineDeviants),
                len(self.shiftingLevelDuplexDeviants)
            ],
            "column" : [
                "縣市",
                "正常交易量",
                "異常交易量",
                "建物型態異常",
                "夾層異常",
                "樓中樓異常"
            ]
        }

    def exportDeviantCases(self, path, county):
        if os.path.exists(path) == False:
            os.mkdir(path)
        if os.path.exists(os.path.join(path, county)) == False:
            os.mkdir(os.path.join(path, county))
        
        dealTableData = []
        buildTableData = []
        landTableData = []
        parkTableData = []
        for index, holder in enumerate(self.contents):
            if holder.dealIsDeviant:

                dealTableData.append(
                    holder.deal.outputRow()
                )
                
                for build in holder.builds:
                    buildTableData.append(
                        build.outputRow()
                    )

                for land in holder.lands:
                    landTableData.append(
                        land.outputRow()
                    )

                for park in holder.parks:
                    parkTableData.append(
                        park.outputRow()
                    )
        
        try:
            deviantDeals = pd.DataFrame(np.array(dealTableData), columns=["鄉鎮市區","交易標的","土地位置建物門牌","土地移轉總面積平方公尺","都市土地使用分區","非都市土地使用分區","非都市土地使用編定","交易年月日","交易筆棟數","移轉層次",	"總樓層數",	"建物型態"	,"主要用途"	,"主要建材",	"建築完成年月",	"建物移轉總面積平方公尺",	"建物現況格局-房",	"建物現況格局-廳",	"建物現況格局-衛",	"建物現況格局-隔間",	"有無管理組織",	"總價元",	"單價元平方公尺",	"車位類別",	"車位移轉總面積(平方公尺)",	"車位總價元",	"備註",	"編號",	"主建物面積",	"附屬建物面積",	"陽台面積",	"電梯",	"移轉編號"])
            deviantDeals.to_csv(os.path.join(path, county, "deviantDeals_{}.csv".format(county)), encoding="utf-8-sig")
        except:
            print(county, "deal")
        
        try:
            deviantBuilds = pd.DataFrame(np.array(buildTableData), columns=["編號",	"屋齡",	"建物移轉面積平方公尺",	"主要用途",	"主要建材"	,"建築完成日期"	,"總層數"	,"建物分層"])
            deviantBuilds.to_csv(os.path.join(path, county, "deviantBuilds_{}.csv".format(county)), encoding="utf-8-sig")
        except:
            print(county, "build")

        try:
            deviantLands = pd.DataFrame(np.array(landTableData), columns=["編號",	"土地位置",	"土地移轉面積(平方公尺)",	"使用分區或編定",	"權利人持分分母"	,"權利人持分分子"	,"移轉情形",	"地號"])
            deviantLands.to_csv(os.path.join(path, county, "deviantLands_{}.csv".format(county)), encoding="utf-8-sig")
        except:
            print(county, "land")

        try:
            deviantParks = pd.DataFrame(np.array(parkTableData), columns=["編號"	,"車位類別",	"車位價格",	"車位面積平方公尺",	"車位所在樓層"])
            deviantParks.to_csv(os.path.join(path, county, "deviantParks_{}.csv".format(county)), encoding="utf-8-sig")
        except:
            print(county, "park")
             


            
