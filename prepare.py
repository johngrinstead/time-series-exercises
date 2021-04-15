import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")



#################################################################################################################################

def prep_sales():
    
    df = pd.read_csv('complete_data.csv')
    
    df = df.drop(columns = 'Unnamed: 0')
    
    # convert our date column to datetime type
    df.sale_date = pd.to_datetime(df.sale_date)
    
    # set date as index
    df = df.set_index('sale_date').sort_index()
    
    # add month and day of week to table
    df['month'] = df.index.month
    df['day_of_week'] = df.index.dayofweek
    
    # add sales total to table
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

#################################################################################################################################

def prep_power():
    df = pd.read_csv('power.csv')

    df = df.drop(columns = 'Unnamed: 0')

    df.columns = ['date', 'consumption', 'wind', 'solar', 'wind_and_solar']
    
    # convert our date column to datetime type
    df.date = pd.to_datetime(df.date)
    
    df = df.set_index('date').sort_index()
    
    df['month'] = df.index.month
    df['year'] = df.index.year
    
    df = df.fillna(0)
    
    return df

#################################################################################################################################

