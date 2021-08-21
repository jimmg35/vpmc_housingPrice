

class Land():
    serialNumber: str              # 編號 (UID)
    ###
    shiftingStatus: str            # 移轉情形
    landPosition: str              # 土地位置
    landParcel: str                # 地號
    landUse: str                   # 使用分區或編定(都市土地使用分區)
    ###
    landShiftingArea: float        # 土地移轉面積(平方公尺)
    ###
    rightOwnerHoldsDenumerate: int # 權利人持分分母
    rightOwnerHoldsNumerate: int   # 權利人持分分子

    def __init__(self, row):
        self.serialNumber = row["編號"]
        ###
        self.shiftingStatus = row["移轉情形"]
        self.landPosition = row["土地位置"]
        self.landParcel = row["地號"]
        self.landUse = row["使用分區或編定"]
        ###
        self.landShiftingArea = row["土地移轉面積(平方公尺)"]
        ###
        self.rightOwnerHoldsDenumerate = row["權利人持分分母"]
        self.rightOwnerHoldsNumerate = row["權利人持分分子"]


