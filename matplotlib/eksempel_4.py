from matplotlib import pyplot as plt
import numpy as np

x=np.array(range(-5,6))

def f(x):
    return 2*x**2-4

plt.title('f(x)=2x^2-4')
plt.ylabel('Y akse')
plt.xlabel('X akse')

plt.plot(x,f(x))

plt.show()
