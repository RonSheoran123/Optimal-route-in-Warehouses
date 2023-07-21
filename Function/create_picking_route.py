import numpy as np
import pandas as pd
from ast import literal_eval

#create total distance to travel for a list of locations
def create_picking_route(origin_loc,list_locs,y_low,y_high):
    wave_distance=0;
    start_loc=origin_loc
    #store routes
    list_chemin=[]
    list_chemin.append(start_loc)
    
    while len(list_locs)>0:
        #going to next location
        list_locs,start_loc,next_loc,distance_next=nextLocation(start_loc,list_locs,y_low,y_high)
        #update start_loc
        start_loc=next_loc
        list_chemin.append(start_loc)
        #update distance
        wave_distance=wave_distance+distance_next
    
    #final distance from last location to origin point
    wave_distance=wave_distance+distancePicking(start_loc,origin_loc,y_low,y_high)
    list_chemin.append(origin_loc)
    
    return wave_distance,list_chemin
