import pandas as pd
import requests
from io import StringIO

def items_():
    
    '''This function brings in the items content dictionary from all pages at the 
       specified website, and then transforms it to a dataframe which it then returns'''
    
    items_list = []
    url = "https://python.zach.lol/api/v1/items"

    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']


    for i in range(1, n+1):
        new_url = url+ '?page=' + str(i)
        response = requests.get(new_url)
        data = response.json()
        page_items = data['payload']['items']
        items_list += page_items
        
    items = pd.DataFrame.from_dict(items_list)
    
    return items

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def stores_():
    
    '''This function brings in the stores content dictionary from all pages at the 
       specified website, and then transforms it to a dataframe which it then returns'''
    
    stores_list = []
    url = "https://python.zach.lol/api/v1/stores"

    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']


    for i in range(1, n+1):
        new_url = url+ '?page=' + str(i)
        response = requests.get(new_url)
        data = response.json()
        page_stores = data['payload']['stores']
        stores_list += page_stores
    
    stores = pd.DataFrame.from_dict(stores_list)
    
    return stores

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sales_acquire():
    sales_list = []
    url = "https://python.zach.lol/api/v1/sales"

    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']


    for i in range(1, n+1):
        new_url = url+ '?page=' + str(i)
        response = requests.get(new_url)
        data = response.json()
        page_sales = data['payload']['sales']
        sales_list += page_sales
        
        
        
        
    sales_df = pd.DataFrame.from_dict(sales_list)
        
    sales_df.to_csv('zachsales_df.csv')
        
    return sales_df

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def pull_csv(url):
    
    '''
    This function pulls a .csv from a specified URL and returns a dataframe.
    '''
    
    
    req = requests.get(url)
    data = StringIO(req.text)
    df = pd.read_csv(data)
    df = pd.DataFrame(df)
    
    return df

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def merge_dataframes():
    
    '''This function takes in the previous 3 functions above, renames the sales column to give a common id of "store_id"
    and then merges the sales and items data frames followed by a merge of the newly formed sales_merge data frame and store data frames.
    A new data frame called store_item_sales is return'''
    
     
    
    items = items_()
    stores = stores_()
    sales = sales_()
  
    sales.columns = ['item_id', 'sale_amount', 'sale_date', 'sale_id', 'store_id']
    
    sales_merge = pd.merge(items, sales, how='left', on=['item_id'], suffixes=['', '_'])
    cols = ['item_id', 'item_brand', 'item_name', 'item_price', 'sale_amount', 'sale_date', 'sale_id', 'store_id', 'item_upc12', 'item_upc14']
    sales_merge = sales_merge[cols]
    
    store_item_sales = pd.merge(stores, sales_merge, how='left', on=['store_id'], suffixes=['', '_'])
    cols = ['item_id', 'item_brand', 'item_name', 'item_price', 'sale_amount', 'sale_date', 'sale_id', 'item_upc12', 'item_upc14', 'store_address', 
    'store_city', 'store_state', 'store_zipcode', 'store_id']
    store_item_sales = store_item_sales[cols]
    
    
    return store_item_sales

