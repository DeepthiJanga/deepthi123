import matplotlib.pyplot as plt
import numpy as np
f=100
fs=1000
t=np.arange(0,100,0.1)
a=np.sin(2*np.pi*f*t/fs)
plt.plot(t,a)
plt.show()