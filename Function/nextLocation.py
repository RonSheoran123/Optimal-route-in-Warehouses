import numpy as np
import pandas as pd
from ast import literal_eval

#next closest location
def nextLocation(start_loc,list_locs,y_low,y_high):
    #distance to every next points candidate
    list_dist=[distancePicking(start_loc,i,y_low,y_high) for i in list_locs]
    #minimum distance
    distance_next=min(list_dist)
    #location of minimum distance
    index_min=list_dist.index(min(list_dist))
    next_loc=list_locs[index_min]
    list_locs.remove(next_loc)
    
    return list_locs, start_loc, next_loc, distance_next
