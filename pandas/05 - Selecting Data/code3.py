import pandas as pd
import numpy as np

arr = np.arange(9).reshape(3,3)

df = pd.DataFrame(
    arr,
    columns=['c1', 'c2', 'c3'],
    index=['r1', 'r2', 'r3']
)

print(df)

ser = pd.Series([-10, -20], index=['r1', 'n2'])

print("\n--- 初始 Series 'ser' ---")
print(ser)

df.iloc[0:2 , 0:2 ] = ser

print(df)