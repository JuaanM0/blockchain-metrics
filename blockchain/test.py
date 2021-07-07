#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:53:48 2021

@author: juanmaxwell
"""

import blockchain


block = blockchain.blockchain_stats_currency()


data = block.total_bitcoins()

block.plot_data()



