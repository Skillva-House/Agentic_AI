import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5, 6])
zeros = np.zeros((2, 3))
rng = np.arange(0, 10, 2)          # [0 2 4 6 8]
lin = np.linspace(0, 1, 5)
rand = np.random.rand(3, 3)

# Shape
m = a.reshape(2, 3)
print(m.shape, m.ndim, m.dtype)

# Indexing and slicing
print(m[0, 1])        # row 0, col 1
print(m[:, 1])        # whole column 1
print(m[1, :])        # whole row 1
print(m[:, :2])       # first 2 columns

# Vectorized ops (no loops!)
print(a * 2)
print(a + a)
print(a ** 2)

# Broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(matrix + row)   # row is added to every row

# Aggregations
print(a.sum(), a.mean(), a.std(), a.max(), a.argmax())
print(matrix.sum(axis=0))   # column sums
print(matrix.sum(axis=1))   # row sums

# Boolean masks
print(a[a > 3])
print(np.where(a % 2 == 0, "even", "odd"))

# ____________________________________________________
import numpy as np

# 1. Array of 1 to 20
x = np.arange(1, 21)
# 2. Only even numbers
print(x[x % 2 == 0])
# 3. Reshape to 4x5, sum each row
print(x.reshape(4, 5).sum(axis=1))
# 4. Normalize: (x - mean) / std
print((x - x.mean()) / x.std())
# 5. Replace values > 10 with 0
y = x.copy()
y[y > 10] = 0
print(y)
# 6. Dot product
print(np.dot([1, 2, 3], [4, 5, 6]))
# 7. Random 5x5, find the max position
r = np.random.rand(5, 5)
print(np.unravel_index(r.argmax(), r.shape))