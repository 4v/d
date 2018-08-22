import datetime
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib
from IPython.display import HTML

today=datetime.datetime.now().strftime('%Y-%m-%d')
df = ts.get_k_data('600050' , start='2016-01-01', end=today)

datastr=''
for idx in df.index
    rowstr='[\'%s\',%s,%s,%s,%s]' % (df.ix[idx]['date'],
                                     df.ix[idx]['open'], 
                                     df.ix[idx]['close'], 
                                     df.ix[idx]['low'], 
                                     df.ix[idx]['high'])
    datastr += rowstr + ','
datastr = datastr[:-1]
name = ts.get_realtime_quotes('600050')['name'][0]

    