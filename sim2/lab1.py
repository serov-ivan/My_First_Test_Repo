'f = x**3 + 3.5x**2 - 14.5x - 35'
import matplotlib.pyplot as plt
import numpy as np
import scipy


def proz(x):
    return 3*x**2 + 7*x-14.5


def func(x):
    return x**3+3.5*x**2-14.5*x-35


def fi(x):
    if proz(x) <= 0:
        return x - 0.001 * func(x)
    else:
        return x + 0.001 * func(x)




e = 0.1
xn = np.arange(-10, 10, 0.01)
resh = []
for i in xn:
    if abs(func(i)) <= e:
        resh.append(i)
print(resh)
print(scipy.optimize.newton(func, -10, fprime=None, args=(),
tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0,
full_output=False, disp=True))
print(scipy.optimize.newton(func, -3, fprime=None, args=(),
tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0,
full_output=False, disp=True))
print(scipy.optimize.newton(func, 1, fprime=None, args=(),
tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0,
full_output=False, disp=True))


x = np.arange(-5, 5, 0.01)
y = x**3 + 3.5*x**2 - 14.5*x - 35
plt.plot(x, y)
for i in range(len(x)):
    if abs(y[i]) <= 0.01:
        plt.plot(x[i], 0, 'o')
plt.grid()
plt.show()