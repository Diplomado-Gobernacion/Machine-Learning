import numpy as np

x = np.array([[4, 3, 4], [20, 75, 3], [8, 3, 12]])
print(x)

print(x.sum())
print(x.sum(axis=0))
print(x.sum(axis=1))
print(x.sum(axis=1, keepdims=True))


