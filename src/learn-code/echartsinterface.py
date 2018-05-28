import datetime
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib
from IPython.display import HTML

today=datetime.datetime.now().strftime('%Y-%m-%d')
df = ts.get_k_data('600050' , start='2016-01-01', end=today)
