#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:28:36 2021

@author: juannM
"""


import requests
import pandas as pd


def prefunction(name_type):
    
     url = 'https://api.blockchain.info/charts/'
     url = url+name_type
     payload = {'timespan'  : 'all','format':'json'}
     response = requests.get(url,params=payload)
     data = response.json()
     df = pd.DataFrame(data['values'])
     df.rename(columns={'y':data['name']},inplace = True)
     df['x'] = pd.to_datetime(df['x'],unit='s')
     df['timestamp'] = df['x'].dt.strftime('%Y-%m-%d')
     df.drop('x',inplace=True,axis=1)
     data = df
     return data
 
    
def prefunction_pool():
    
     url = 'https://api.blockchain.info/pools'
     days_pool = '7days'
     payload = {'timespan'  : days_pool,'format':'json'}
     response = requests.get(url,params=payload)
     data = response.json()
     df = pd.DataFrame([[key, data[key]] for key in data.keys()], columns=['Minner_Name', 'Blocks_mined'])
     return df
    
    
def prefunction_stats():
    
     url = 'https://api.blockchain.info/stats'
     days_pool = 'all'
     payload = {'timespan'  : days_pool,'format':'json'}
     response = requests.get(url,params=payload)
     data = response.json()
     df = pd.DataFrame([[key, data[key]] for key in data.keys()], columns=['Stat-Name', 'Value-mined'])
     return df
       
    
def prefunction_latstblock():
    
     url = 'https://blockchain.info/latestblock'
     payload = {'timespan'  : 'all','format':'json'}
     response = requests.get(url,params=payload)
     data = response.json()
     df = pd.DataFrame([[key, data[key]] for key in data.keys()], columns=['Stat-Name', 'Value-mined'])
     return df
       
    
def prefunction_balance_tx(tx_public):
    
     url = 'https://blockchain.info/balance?active='+tx_public
     payload = {'timespan'  : 'all','format':'json'}
     response = requests.get(url,params=payload)
     data = response.json()
     df = pd.DataFrame([[key, data[key]] for key in data.keys()], columns=['Stat-Name', 'Value-mined'])
     return df
    
    
def tickers_fiat():
    
     url = 'https://blockchain.info/es/ticker'
     payload = {'timespan'  : 'all','format':'json'}
     response = requests.get(url,params=payload)
     data = response.json()
     df = pd.DataFrame([[key, data[key]] for key in data.keys()], columns=['Symbol-fiat', 'Value-mined'])
     return df

    