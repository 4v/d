import numpy
import talib

close = numpy.random.random(100)*100
print(close)
output = talib.SMA(close,20)

print(output)

