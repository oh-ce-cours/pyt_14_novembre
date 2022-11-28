import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive

# interactive(True)
xs = np.linspace(-2 * np.pi, 2 * np.pi, 100)
ys = np.cos(xs)
figure = plt.figure()
axes = figure.add_subplot(111)
axes.plot(xs, ys, "o-")
plt.title("Super graph !")
plt.show()

figure = plt.figure()
axes = figure.add_subplot(111)
axes.plot(xs, ys ** 2, "o-")
plt.title("Super graph !")
interactive(False)
plt.show()
