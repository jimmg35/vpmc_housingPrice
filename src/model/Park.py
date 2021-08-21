

class Park():
    serialNumber: str              # 編號 (UID)
    ###
    parkCategory: str              # 車位類別
    parkLevel: str                 # 車位所在樓層
    ###
    parkArea: float                # 車位面積平方公尺
    ###
    parkPrice: int                 # 車位價格

    def __init__(self, row):
        self.serialNumber = row["編號"]
        ###
        self.parkCategory = row["車位類別"]
        self.parkLevel = row["車位所在樓層"]
        ###
        self.parkArea = row["車位面積平方公尺"]
        ###
        self.parkPrice = row["車位價格"]