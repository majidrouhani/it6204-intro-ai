import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.01)

y = np.sin(x)

plt.title("y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)

plt.show()
