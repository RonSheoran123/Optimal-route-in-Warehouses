import numpy as np
import pandas as pd
from ast import literal_eval

#getting storage locations to cover for a wave of orders
def locations_listing(df_orderlines,wave_id):
    #filter by wave id
    df=df_orderlines[df_orderlines.WaveID==wave_id]
    #create cordinates listing
    list_locs=list(df['Coord'].apply(lambda t: literal_eval(t)).values)
    list_locs.sort()
    #get unique UniqueCordinates
    list_locs = list(k for k,_ in itertools.groupby(list_locs))
    n_locs = len(list_locs)
    
    return list_locs,n_locs
