import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
import matplotlib.pyplot as plt
from matplotlib import rc
rc('mathtext', default='regular')
import seaborn as sns
sns.set_style('white')
from matplotlib import dates
import matplotlib as mpl
%matplotlib inline
# myfont = mpl.font_manager.FontProperties(
    # fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.rcParams["figure.figsize"] = (20, 10)


dw = ts.get_k_data("600600")
dw = dw[300:]
dw.index = range(len(dw))
close = dw.close.values
dw["rsi"] = ta.RSI(close, timeperiod=14)
#dw[["close","rsi"]].plot()
fig = plt.figure(figsize=(20, 10))
fig.set_tight_layout(True)
ax1 = fig.add_subplot(111)
#fig.bar(dw.index, dw.volume, align='center', width=1.0)
ax1.plot(dw.index, dw.close, '-', color='g')

ax2 = ax1.twinx()
ax2.plot(dw.index, dw.rsi, '-', color='r')
ax2.plot(dw.index, [70] * len(dw), '-', color='r')
ax2.plot(dw.index, [30] * len(dw), '-', color='r')

ax1.set_ylabel(u"股票价格(绿色)", fontproperties=myfont, fontsize=16)
ax2.set_ylabel(u"RSI参数", fontproperties=myfont, fontsize=16)
ax1.set_title(u"绿色是股票价格，红色（右轴）为RSI参数", fontproperties=myfont, fontsize=16)
# plt.xticks(bar_data.index.values, bar_data.barNo.values)
ax1.set_xlabel(u"RSI参数图", fontproperties=myfont, fontsize=16)
ax1.set_xlim(left=-1, right=len(dw))
ax1.grid()

# 作者：readilen
# 链接：https: // www.jianshu.com / p / 9d7273a6a7ca
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
