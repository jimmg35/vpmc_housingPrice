
from ..model.Deal import Deal
from ..model.Build import Build
from ..model.Land import Land
from ..model.Park import Park

from typing import List

class Holder():
    deal: Deal
    ###
    builds: List[Build]
    lands: List[Land]
    parks: List[Park]


