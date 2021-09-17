

class Deal():
    serialNumber: str             # 編號 (UID)
    ###
    nonMetroLandUseDistrict: str  # 非都市土地使用分區
    transactionAmount: str        # 交易筆棟數
    totalFloorNumber: str         # 總樓層數
    buildingMaterial: str         # 主要建材
    transactionSign: str          # 交易標的
    nonMetroLandUse: str          # 非都市土地使用編定
    transactionDate: str          # 交易年月日
    completionDate: str           # 建築完成年月
    shiftingLevel: str            # 移轉層次
    buildingState: str            # 建物型態
    parkCategory: str             # 車位類別
    shiftingCode: str             # 移轉編號
    mainUse: str                  # 主要用途
    address: str                  # 土地位置建物門牌
    landUse: str                  # 都市土地使用分區
    town: str                     # 鄉鎮市區
    note: str                     # 備註
    ###  
    buildingShiftingArea: float   # 建物移轉總面積平方公尺
    landShiftingArea: float       # 土地移轉總面積平方公尺
    mainBuildingArea: float       # 主建物面積
    parkShiftingArea: float       # 車位移轉總面積(平方公尺)
    subBuildingArea: float        # 附屬建物面積
    parkTotalPrice: float         # 車位總價元
    belconyArea: float            # 陽台面積
    totalPrice: float             # 總價元
    unitPrice: float              # 單價元平方公尺
    ###
    healthNumber: int             # 建物現況格局-衛
    roomNumber: int               # 建物現況格局-房
    hallNumber: int               # 建物現況格局-廳
    ###
    manageOrganization: bool      # 有無管理組織
    compartmented: bool           # 建物現況格局-隔間
    elevator: bool                # 電梯


    def __init__(self, row):
        self.serialNumber = row["編號"]
        ###
        self.nonMetroLandUseDistrict = row["非都市土地使用分區"]
        self.transactionAmount = row["交易筆棟數"]
        self.totalFloorNumber = row["總樓層數"]
        self.buildingMaterial = row["主要建材"]
        self.transactionSign = row["交易標的"]
        self.nonMetroLandUse = row["非都市土地使用編定"]
        self.transactionDate = row["交易年月日"]
        self.completionDate = row["建築完成年月"]
        self.shiftingLevel = row["移轉層次"]
        self.buildingState = row["建物型態"]
        self.parkCategory = row["車位類別"]
        self.shiftingCode = row["移轉編號"]
        self.mainUse = row["主要用途"]
        self.address = row["土地位置建物門牌"]
        self.landUse = row["都市土地使用分區"]
        self.town = row["鄉鎮市區"]
        self.note = row["備註"]
        ###
        self.buildingShiftingArea = row["建物移轉總面積平方公尺"]
        self.landShiftingArea = row["土地移轉總面積平方公尺"]
        self.mainBuildingArea = row["主建物面積"]
        self.parkShiftingArea = row["車位移轉總面積(平方公尺)"]
        self.subBuildingArea = row["附屬建物面積"]
        self.parkTotalPrice = row["車位總價元"]
        self.belconyArea = row["陽台面積"]
        self.totalPrice = row["總價元"]
        self.unitPrice = row["單價元平方公尺"]
        ###
        self.healthNumber = row["建物現況格局-衛"]
        self.roomNumber = row["建物現況格局-房"]
        self.hallNumber = row["建物現況格局-廳"]
        ###
        self.manageOrganization = row["有無管理組織"]
        self.compartmented = row["建物現況格局-隔間"]
        self.elevator = row["電梯"]

    def outputRow(self):
        return [
            self.town,
            self.transactionSign,
            self.address,
            self.landShiftingArea,
            self.landUse,
            self.nonMetroLandUseDistrict,
            self.nonMetroLandUse,
            self.transactionDate,
            self.transactionAmount,
            self.shiftingLevel,
            self.totalFloorNumber,
            self.buildingState,
            self.mainUse,
            self.buildingMaterial,
            self.completionDate,
            self.buildingShiftingArea,
            self.roomNumber,
            self.hallNumber,
            self.healthNumber,
            self.compartmented,
            self.manageOrganization,
            self.totalPrice,
            self.unitPrice,
            self.parkCategory,
            self.parkShiftingArea,
            self.parkTotalPrice,
            self.note,
            self.serialNumber,
            self.mainBuildingArea,
            self.subBuildingArea,
            self.belconyArea,
            self.elevator,
            self.shiftingCode
        ]

