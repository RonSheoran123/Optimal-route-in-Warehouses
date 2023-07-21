import numpy as np
import pandas as pd
from ast import literal_eval
import itertools

#mapping orders by wave number
def orderlines_mapping(df_orderlines,order_number):
    #order dataframe by times frame
    df_orderlines=df_orderlines.sort_values(by='DATE',ascending=True)
    #unique order numbers list
    list_orders=df_orderlines.OrderNumber.unique()
    #dictionary for mapping
    dict_map=dict(zip(list_orders,[i for i in range(1,len(list_orders))]))
    #order id mapping
    df_orderlines['OrderID']=df_orderlines['OrderNumber'].map(dict_map)
    #group orders by wave of orders_number
    df_orderlines['WaveID'] = (df_orderlines['OrderID']%orders_number == 0).shift(1).fillna(0).cumsum()
    #counting number of waves
    waves_number = df_orderlines.WaveID.max() + 1
    
    return df_orderlines,waves_number
