import numpy as np

A = np.array([[1, 4, 5], [2, 1, 2], [3, 3, 4]], dtype=np.uint8)

print(A)
print(type(A))
print(A.dtype)
print(A.shape)
print(A.ndim)


B = np.ones((4, 6), dtype=np.int8)
print(B)
print(B.dtype)

C = np.arange(10, 20)
print(C)

C = np.array(range(10,20))
print(C)

A = np.ones((3, 5), dtype=np.uint8)
B = np.zeros((3, 4), dtype=np.uint8)

C = np.concatenate([A,B], axis=1)
print(C)

print(C.dtype)

C = C.astype(np.float32)
print(C)
print(C.dtype)

print("\n\n\n\n\n\n")
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)

B = np.ones_like(A)
print(B)


A = np.random.random((10, 3))
print(A)