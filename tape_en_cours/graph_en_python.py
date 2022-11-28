import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive

xs = np.linspace(-2 * np.pi, 2 * np.pi, 100)
ys = np.cos(xs)
figure = plt.figure()
axes = figure.add_subplot(111)
axes.plot(xs, ys, "o-")
plt.title("Super graph !")
interactive()
plt.show()

figure = plt.figure()
axes = figure.add_subplot(111)
axes.plot(xs, ys, "o-")
plt.title("Super graph !")
plt.show()
