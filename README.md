# q3inversesqrtnumpy
All credits to GPT3 for writing this code, I'm just the prompt guy


GPT3 prompt and response:

We need to plot the following:

1. log2(1 + x) 
2. f(x)=x +  0.04504656 

The range of the chart is 0 to 1

ChatGPT
Certainly! Here's the code to plot the functions "log₂(1 + x)" and "f(x) = x + 0.04504656" within the range 0 to 1:

python
Copy code
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
In this code, we generate 1000 equally spaced points between 0 and 1 using np.linspace(). Then, we compute the y-values for Function 1, which is "log₂(1 + x)", and Function 2, which is "f(x) = x + 0.04504656". Finally, we plot both functions on the same chart using plt.plot().

The resulting plot will display the curves for both functions within the specified range of 0 to 1. The x-axis represents the values of x, and the y-axis represents the corresponding values of each function.
