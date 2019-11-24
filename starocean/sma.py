import backtrader as bt
import backtrader.indicators as btind
import datetime

import tushare as ts
import pandas as pd

class SMA_CrossOver(bt.Strategy):
    params = (('fast', 3), ('slow', 20))

    def __init__(self):
        self.buysig = {}
        for d in self.getdatanames():
            sma_fast = btind.SMA(self.getdatabyname(d), period=self.p.fast)
            sma_slow = btind.SMA(self.getdatabyname(d), period=self.p.slow)
            self.buysig[d] = btind.CrossOver(sma_fast, sma_slow)

    def next(self):
        for d in self.getdatanames():
            if self.getpositionbyname(d).size:
                if self.buysig[d] < 0:
                    self.sell(data=self.getdatabyname(d))

            elif self.buysig[d] > 0:
                self.buy(data=self.getdatabyname(d))


cerebro = bt.Cerebro()
cerebro.broker.setcommission(
    commission=0.002
)


# Create a data feed
df = ts.get_hist_data('600848')
print(len(df))
print(df.columns)
# print(df.head())
df.index = pd.to_datetime(df.index)
dt = df[['open', 'high', 'low', 'close', 'volume']]
data = bt.feeds.PandasData(dataname=dt, fromdate=datetime.datetime(2019, 1, 1), todate=datetime.datetime.now().date())

cerebro.adddata(data)  # Add the data feed
cerebro.addstrategy(SMA_CrossOver)
cerebro.run()
print(cerebro.broker.getvalue())
cerebro.plot()