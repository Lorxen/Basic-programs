# Show a graphic of the information

import matplotlib.pyplot as plt

x1 = [2, 4, 5]
y1 = [2, 3, 6]

plt.plot(x1, y1, label='Line 1')

x2 = [1, 4, 7]
y2 = [1, 2, 3]

plt.plot(x2, y2, label='Line 2')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Two lines')

plt.legend()

plt.show()
