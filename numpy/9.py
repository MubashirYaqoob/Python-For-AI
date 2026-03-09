import numpy as np 

arr = np.array([1,2,3])
print(arr)

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

print(matrix)

#np.zeros((2,2))

#matrix = np.arange(0,10,2)
print(matrix)

#matrix = np.random.randint(1,100,5)

print(matrix)
print(matrix.shape)

print(matrix.size)
print(matrix.dtype)

print(matrix.ndim)

print(matrix + 3)

np.sum(matrix)

np.min(matrix)
np.mean(matrix)
np.sort(matrix)