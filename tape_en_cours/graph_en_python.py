import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-2 * np.pi, 2 * np.pi, 100)
ys = np.cos(xs)
plt.plot(xs, ys, "o-")
plt.title("Super graph !")
