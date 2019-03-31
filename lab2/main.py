import numpy as np
import matplotlib.pyplot as plt

# variant 13
n = 13


def path_optimization(N = 100, K = 300, s0 = n, v = n, l = n, phi = np.pi * n / 25):
    tau = (l / v) / N
    x1_star = l * np.cos(phi)
    x2_star = l * np.sin(phi)

    x1 = np.zeros(K)
    x2 = np.zeros(K)

    return x1, x2
