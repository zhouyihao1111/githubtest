# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:04:25 2020

@author: Administrator
"""

import csv
from statsmodels.tsa.stattools import adfuller
import numpy as np
import math

def read_csv(file):
    with open(file,'r',encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        daily_price = []
        for row in reader:
            daily_price.append(float(row['close']))
    return daily_price

def check_byADF(sequence):
    x = np.array(sequence)
    xx = np.diff(sequence)
    result = adfuller(xx)
    print(result)
    
def hurst(ts):
    lags = range(2,100)
    tau = [math.sqrt(np.std(np.subtract(ts[lag:],ts[:-lag]))) for lag in lags]
    poly = np.polyfit(np.log(lags),np.log(tau),1)
    return poly[0]*2    



if __name__ == "__main__":
    file = 'E:/zyh/rawdata/000875.csv'
    sequence = read_csv(file)
    check_byADF(sequence)
    gbm = np.random.randn(10000)
    print('Hurst 000875: %s'%hurst(seque))
    
    
