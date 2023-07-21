import numpy as np
import pandas as pd
from ast import literal_eval

#minimum distance between two points
def distancePicking(Loc1,Loc2,y_low,y_high):
    #starting point
    x1, y1=Loc1[0],Loc1[1]
    #ending point
    x2, y2=Loc2[0],Loc2[1]
    #x-axis distance
    distance_x=abs(x2-x1)
    #y-axis distance
    if x1==x2:
        distance_y1=abs(y2-y1)
        distance_y2=distance_y1
    else:
        distance_y1=(y_high-y1)+(y_high-y2)
        distance_y2=(y1-y_low)+(y2-y_low)
    #y min
    distance_y=min(distance_y1,distance_y2)
    #total distance
    distance=distance_x+distance_y
    
    return distance
