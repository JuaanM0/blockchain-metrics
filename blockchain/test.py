#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:53:48 2021

@author: juannM
"""

from blockchain_metrics import blockchain_data

block = blockchain_data.blockchain_stats_currency()


#total bitcoins in circulation
dataframe_total_bitcoins = block.total_bitcoins()
block.plot_data()


#cost per transaction
block.cost_per_transaction()
block.plot_data()


#Mining pools and plot pir
block.pools()
block.plot_pools_pie()





