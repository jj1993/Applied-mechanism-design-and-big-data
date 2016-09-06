import matplotlib
import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0.4, 30, 0.1)
P_t = 0
c = 299792458
f = 2.4
P_r = P_t - 20 * np.log10(c / (4* np.pi* f* r))
plt.plot(r, P_r)
plt.show()


