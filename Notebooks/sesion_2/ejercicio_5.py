import numpy as np

A = np.array([1, 2, 3, 8])
B = np.array([4, 5, 6, 8])

if (A.shape == B.shape):
    C = A * B
    #print(C)

D = np.random.random((5,5))
E = D < 0.2
#print(E)


A = np.array([[1, 2], [3, 4]], dtype=np.float32)
B = np.array([[5, 6], [7, 8]], dtype=np.float32)

A *= B


print(A)