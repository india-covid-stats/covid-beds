from . import delhi
from . import durg
from . import gujarat
from . import nagpur
from . import tamilnadu


scrape = {
        'delhi'     : delhi.scrape,
        'durg'      : durg.scrape,
        'gujarat'   : gujarat.scrape,
        'nagpur'    : nagpur.scrape,
        'tamilnadu' : tamilnadu.scrape,
        }
