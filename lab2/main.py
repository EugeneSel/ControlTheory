import numpy as np
import matplotlib.pyplot as plt

# variant 2
n = 1


def path_optimization(a2, clr, N = 100, K = 300, s0 = n, v = n, l = n, phi = np.pi * n / 25):
    tau = (l / v) / N
    x1_star = l * np.cos(phi)
    x2_star = l * np.sin(phi)
    epsilon = 0.03
    t_gen = 0

    t = np.zeros(K)
    for k in range(K):
        t[k] = tau * k

    def f(x):
        return x

    x1_old = x2_old = 0
    z = 0
    while 1:
        p = 0
        x1 = np.zeros(1)
        x2 = np.zeros(1)
        u1 = np.zeros(K)
        u2 = np.zeros(K)
        lamb = np.zeros(K)
        s = np.zeros(K)

        x1[0] = x1_old
        x2[0] = x2_old
        for i in range(K - 1):
            s[i] = a2 * s0 * f(x2[i])
            lamb[i] = ((x1_star - x1[i] - s[i] * tau) ** 2 + (x2_star - x2[i]) ** 2) ** (1 / 2) * v * tau - v ** 2 * tau ** 2
            u1[i] = (x1_star - x1[i] - s[i] * tau) * v * tau / (lamb[i] + v ** 2 * tau ** 2)
            u2[i] = (x2_star - x2[i]) * v * tau / (lamb[i] + v ** 2 * tau ** 2)
            x1_new= x1[i] + (s[i] + v * u1[i]) * tau
            x2_new = x2[i] + v * u2[i] * tau
            x1 = np.append(x1, [x1_new], axis=0)
            x2 = np.append(x2, [x2_new], axis=0)
            if abs(x1[i + 1] - x1_star) <= epsilon or abs(x2[i + 1] - x2_star) <= epsilon:
                x1_old = x1[i + 1]
                x2_old = x2[i + 1]
                t_gen += tau * (i + 1)
                break
            x1_old = x1[i + 1]
            x2_old = x2[i + 1]
            t_gen += tau * (i + 1)

        z += 1
        if abs(x1[p] - x1_star) / x1_star <= epsilon and abs(x2[p] - x2_star) / x2_star <= epsilon:
            plt.plot(x1, x2, color=clr, label='t = %0.2f, a2 = %d' % (t_gen, a2))
            break
        plt.plot(x1, x2, color=clr)

    return x1_star, x2_star, t_gen


x1, x2, t_gen = path_optimization(15, 'orange')
path_optimization(10, 'r')
path_optimization(5, 'g')
path_optimization(1, 'b')
path_optimization(-1, 'c')
path_optimization(-3, 'm')
path_optimization(-5, 'violet')
path_optimization(-7, 'y')
plt.scatter(x1, x2, c='k')
plt.legend()
plt.show()
