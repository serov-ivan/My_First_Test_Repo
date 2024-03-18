import numpy as np
with open('data2.txt') as f:
    data = f.read().split('\n')


def minor(im, jm, a):
    data = []
    for i in range(len(a)):
        if im == i:
            pass
        else:
            for j in range(len(a)):
                if jm == j:
                    pass
                else:
                    data.append(a[i][j])
    k = np.zeros((5, 5))
    z = 0
    for i in range(len(k)):
        for j in range(len(k)):
            k[i][j] = data[z]
            z += 1
    return np.linalg.det(k)

for i in range(len(data)):
    data[i] = list(map(int, data[i].split(' ')))
a = np.ones((6, 6))
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = a[i][j] * data[i][j]
b = np.ones((6, 1))
for i in range(len(b)):
    b[i] = data[i][-1]
deta = np.linalg.det(a)
c = np.zeros((6, 6))
for i in range(len(a)):
    for j in range(len(a)):
        c[i][j] = minor(i, j, a) * (-1 ** (i + j))
c = np.transpose(c) * (1/deta)
answer = c @ b
print(answer)
print(np.linalg.solve(a,b))