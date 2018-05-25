import numpy as np
import pandas as pd

a = np.random.standard_normal((9, 4))
b = pd.DataFrame(a)
b.columns = [['num1', 'num2', 'num3', 'num4']]

print(a)
print(b)


