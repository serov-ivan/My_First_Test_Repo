import numpy as np
a = np.ones((10, 1)) * 10
for i in range(1, 5):
    b = np.ones((10, 1)) * (10 - i)
    b[-1: (-1 - i): - 1] = 0
    a = np.column_stack((a, b))
for i in range(1, 6):
    c = np.zeros((10, 1))
    c[5:(5 - i):-1] = i
    a = np.column_stack((a, c))
print(a)