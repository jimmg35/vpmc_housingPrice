
from ..model.Deal import Deal
from ..model.Build import Build
from ..model.Land import Land
from ..model.Park import Park

from typing import List

class Holder():
    deal: Deal
    ###
    builds: List[Build] = []
    lands: List[Land] = []
    parks: List[Park] = []
    ###
    dealIsDeviant: bool 
    ###

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
                
    def startUp(self):
        self.parseTransactionSign()      # 解析交易標的
        self.parseTransactionAmount()    # 解析交易筆棟數
        self.validateTransactionDetail() # 比對上述兩者是否吻合

    def status(self):
        print(f" deal serial number : {self.deal.serialNumber}")
        print(f" build amount       : {len(self.builds)}")
        print(f" land amount        : {len(self.lands)}")
        print(f" park amount        : {len(self.parks)}")
