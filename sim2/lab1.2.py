import matplotlib.pyplot as plt
import numpy as np
import scipy

e = 20
r = 4


def R(i):
    return 0.2 ** i + np.cos(i) - 4


x = np.arange(-1, 0, 0.001)
y = 0.2 ** x + np.cos(x) - 4
for i in range(len(x)):
    if abs(y[i]) <= 0.01:
        plt.plot(x[i], 0, 'o')
plt.plot(x, y)
plt.grid()
plt.show()
print(scipy.optimize.newton(R, -0.7, fprime=None, args=(),
                            tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0,
                            full_output=False, disp=True))

Y = np.array([0, -5, -68, -10])
X = np.array([0, 109, 152, 250])
xn = np.linspace(0, 250, 1000)
yn = []
for l in xn:
    y = 0
    for k in range(len(Y)):
        p = 1
        for m in range(len(X)):
            if k != m:
                p = p * (l - X[m]) / (X[k] - X[m])
        y = y + Y[k] * p
    yn.append(y)
plt.plot(xn[0:1000], yn[0:1000])
plt.show()
