

class Build():
    serialNumber: str             # 編號 (UID)
    ###
    buildingLamination: str       # 建物分層
    buildingMaterial: str         # 主要建材
    totalFloorNumber: str         # 總層數
    completionDate: str           # 建築完成日期
    mainUse: str                  # 主要用途
    ###
    buildingShiftingArea: float   # 建物移轉面積平方公尺
    ###
    buildingAge: int              # 屋齡

    def __init__(self, row):
        self.serialNumber = row["編號"]
        ###
        self.buildingLamination = row["建物分層"]
        self.buildingMaterial = row["主要建材"]
        self.totalFloorNumber = row["總層數"]
        self.completionDate = row["建築完成日期"]
        self.mainUse = row["主要用途"]
        ###
        self.buildingShiftingArea = row["建物移轉面積平方公尺"]
        ###
        self.buildingAge = row["屋齡"]

