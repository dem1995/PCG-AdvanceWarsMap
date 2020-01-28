
from itertools import chain, combinations
from enum import Enum
import numpy as np

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


eastarr = np.array([-1, 0])
westarr = np.array([1, 0])
northarr = np.array([0, -1])
southarr = np.array([0, 1])

east = ("East: ", eastarr)
west = ("West: ", westarr)
north = ("North: ", northarr)
south = ("South: ", southarr)
northeast = ("Northeast", northarr+eastarr)
northwest = ("Northwest", northarr+westarr)
southeast = ("Southeast", southarr+eastarr)
southwest = ("Southwest", southarr+westarr)

