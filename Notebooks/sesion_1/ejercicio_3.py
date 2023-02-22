import numpy as np

A = np.random.random((16,))
print(A)
print(A.shape)

#B = A.reshape(2,5)
#print(B)
#print(B.shape)


C = A.reshape(4, -1)
print(C)
print(C.shape)

D = C.ravel()
print(D)