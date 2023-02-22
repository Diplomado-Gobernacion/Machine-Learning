import numpy as np

A = np.array([1,2,3])
B = np.array([1,2,0])

C = A + B

print(C)


A = np.array([1, 4.5, np.nan])
A = A.astype(np.int32)

C = A + B

print(C)
