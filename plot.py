import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)  # Generating 1000 equally spaced points between 0 and 1

y1 = np.log2(1 + x)  # Function 1: log₂(1 + x)
y2 = x + 0.04504656  # Function 2: f(x) = x + 0.04504656

plt.plot(x, y1, label='log₂(1 + x)')
plt.plot(x, y2, label='f(x) = x + 0.04504656')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of log₂(1 + x) and f(x) = x + 0.04504656')
plt.xlim(0, 1)  # Adjusting the x-axis limits
plt.ylim(0, 1.1)  # Adjusting the y-axis limits
plt.grid(True)
plt.legend()
plt.show()
