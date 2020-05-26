from scipy.interpolate import interp1d
import numpy as np
from scipy.optimize import minimize

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=41, endpoint=True)

m = minimize(f2, [4], bounds=[[xnew.min(), xnew.max()]])

import matplotlib.pyplot as plt
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.plot(m.x, m.fun, 'X')
plt.axhline(m.fun)
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()
