import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-2 * np.pi, 2 * np.pi, 100)
ys = np.cos(xs)
figure = plt.figure()
axes = figure.add_subplot(111)
axes[0].plot(xs, ys, "o-")
plt.title("Super graph !")
plt.show()
