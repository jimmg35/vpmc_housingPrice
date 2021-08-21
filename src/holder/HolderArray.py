
from ..model.Deal import Deal
from ..model.Build import Build
from ..model.Land import Land
from ..model.Park import Park
from .Holder import Holder

from typing import List

class HolderArray():
    contents: List[Holder]

    def __init__(self):
        self.contents = []
    
    def status(self):
        normal = []
        deviants = []
        for index, holder in enumerate(self.contents):
            if holder.dealIsDeviant:
                deviants.append(holder)
            else:
                normal.append(holder)
        print(f"normal case  : {len(normal)}")
        print(f"deviant case : {len(deviants)}")