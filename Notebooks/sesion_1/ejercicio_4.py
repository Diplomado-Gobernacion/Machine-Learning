import numpy as np

A = np.arange(10).reshape(5,2)
print(A)

At = A.T
print(At)

np.savez('data.npz', transpuesta=At, matriz=A)

data = np.load('data.npz')
print(data)

matrixT = data['transpuesta']
matrix = data['matriz']

#print(matrix)
#print(matrixT)