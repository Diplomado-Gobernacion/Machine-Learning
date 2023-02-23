import numpy as np

A = np.array([1, 2, 3, np.nan, 6])
#print(A)

B = np.isnan(A)
#print(B)

A = np.array([1, 2, 3, 4])
B = A[2:4]
B[0] = 2
#print(A)
#print(B)

A = np.array([1, 2, 3, np.nan, 6])
#print(A)
B = np.isnan(A)
#print(B)
C = A[B]
#print(C)

A = np.random.random((10,10))

B = A[A<0.5]
#print(A.shape)
#print(B.shape)

A[A<0.5] = 0
print(A)