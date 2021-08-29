
from ..model.Deal import Deal
from ..model.Build import Build
from ..model.Land import Land
from ..model.Park import Park

from typing import Dict, List


class Holder():
    deal: Deal
    ###
    builds: List[Build] = []
    lands: List[Land] = []
    parks: List[Park] = []
    ###
    dealIsDeviant: bool 
    ###
    transactionSignParsed: Dict
    transactionAmountParsed: Dict
    ###
    noteEnum: Dict

    def __init__(self, deal):
        self.deal = deal
        self.builds = []
        self.lands = []
        self.parks = []

        #########

        self.dealIsDeviant = False

        #########        

        self.transactionSignParsed = {
            "土地": False,
            "建物": False,
            "車位": False,
        }
        self.transactionAmountParsed = {
            "土地": 0,
            "建物": 0,
            "車位": 0,
        }

        #########   

        self.noteEnum = {
            "公共設施保留地之交易": ["公共設施保留地之交易", "公共設施保留地", "公共設施"],
            "公共設施交易": ["公共設施交易", "公共設施"],
            "受債權債務影響或債務抵償之交易": ["受債權債務影響或債務抵償之交易", "債權債務", "債權", "債務", "抵償", "債務抵償"],
            "向政府機關承購之案件": ["向政府機關承購之案件", "政府機關承購", "政府機關"],
            "土地及建物分次登記案件": ["土地及建物分次登記案件", "分次登記", "分次"],
            "建商地主合建案": ["建商地主合建案", "建商地主"],
            "急買急賣": ["急買急賣", "急買", "急賣"],
            "有夾層": ["有夾層", "夾層"],
            "有民情風俗因素之交易": ["有民情風俗因素之交易", "民情風俗", "民情", "風俗"],
            "法拍屋": ["法拍屋", "法拍"],
            "瑕疵物件之交易": ["瑕疵物件之交易", "瑕疵物件", "瑕疵"],
            "畸零地及合併使用之交易": ["畸零地及合併使用之交易", "畸零地", "合併使用"],
            "親友關係人交易": ["親友關係人交易", "親友關係人", "親友", "關係人"],
            "賣清買清(稅費議定誰負擔)": ["賣清買清(稅費議定誰負擔)", "賣清買清", "賣清", "買清"],
            "農地交易(興建農舍_375租約)": ["農地交易(興建農舍_375租約)", "375租約", "農地交易", "農地", "農舍"]
        }




    def parseTransactionSign(self):
        for i in ["土地", "建物", "車位"]:
            if i in self.deal.transactionSign:
                self.transactionSignParsed[i] = True

    def parseTransactionAmount(self):
        self.transactionAmountParsed["土地"] = int(self.deal.transactionAmount[self.deal.transactionAmount.index("土地") + 2 : self.deal.transactionAmount.index("建物")])
        self.transactionAmountParsed["建物"] = int(self.deal.transactionAmount[self.deal.transactionAmount.index("建物") + 2 : self.deal.transactionAmount.index("車位")])
        self.transactionAmountParsed["車位"] = int(self.deal.transactionAmount[self.deal.transactionAmount.index("車位") + 2 : ])

    def validateTransactionDetail(self):
        for i in ["土地", "建物", "車位"]:
            if self.transactionSignParsed[i]:
                if self.transactionAmountParsed[i] == 0:
                    self.dealIsDeviant = True
            else:
                if self.transactionAmountParsed[i] != 0:
                    self.dealIsDeviant = True
                
    ###################################

    def detectNote(self):
        for i in self.noteEnum.keys():
            for j in self.noteEnum[i]:
                if j in str(self.deal.note):
                    self.dealIsDeviant = True

    ###################################

    def startUp(self):
        self.parseTransactionSign()      # 解析交易標的
        self.parseTransactionAmount()    # 解析交易筆棟數
        self.validateTransactionDetail() # 比對上述兩者是否吻合

        ###

        self.detectNote()                # 利用關鍵字排除備註特殊交易



    def status(self):
        print(f" deal serial number : {self.deal.serialNumber}")
        print(f" build amount       : {len(self.builds)}")
        print(f" land amount        : {len(self.lands)}")
        print(f" park amount        : {len(self.parks)}")
