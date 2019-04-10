import numpy as np
import matplotlib.pyplot as plt

# variant 2
n = 1


def path_optimization(clr, s0=n, v=n, l=n, phi=np.pi * n / 25, epsilon=0.01, N=100, M=5):
    tau = (l / v) / N
    x1_star = l * np.cos(phi)
    x2_star = l * np.sin(phi)
    K = 10 ** M
    t_gen = 0

    t = np.zeros(M)
    for m in range(M):
        t[m] = tau * m

    def Phi(y_1, y_2):
        return (x1_star - y_1) ** 2 + (x2_star - y_2) ** 2

    x1 = np.zeros(1)
    x2 = np.zeros(1)
    z = 0
    while 1:
        y1 = np.zeros(1)
        y2 = np.zeros(1)
        y1[0] = x1[z]
        y2[0] = x2[z]
        p = 0

        for i in range(M - 1):
            psi = np.linspace(0, np.pi, K, endpoint=True)
            Phi_min = 0
            y1_min = 0
            y2_min = 0
            for k in range(len(psi)):
                y1_cur = y1[i] + s0 * tau * y2[i] + s0 * v * tau ** 2 * np.sin(psi[k]) + v * tau * np.cos(psi[k])
                y2_cur = y2[i] + v * tau * np.sin(psi[k])
                if k == 0:
                    Phi_min = Phi(y1_cur, y2_cur)
                if Phi(y1_cur, y2_cur) <= Phi_min:
                    Phi_min = Phi(y1_cur, y2_cur)
                    y1_min = y1_cur
                    y2_min = y2_cur

            y1 = np.append(y1, [y1_min], axis=0)
            y2 = np.append(y2, [y2_min], axis=0)
            p = i + 1

            if abs(y1[i + 1] - x1_star) <= epsilon and abs(y2[i + 1] - x2_star) <= epsilon:
                break

        x1 = np.append(x1, [y1[p]], axis=0)
        x2 = np.append(x2, [y2[p]], axis=0)
        t_gen += tau * p
        z += 1

        if abs(x1[z] - x1_star) <= epsilon and abs(x2[z] - x2_star) <= epsilon:
            plt.plot(y1, y2, c=clr, label='Оптимальна траєкторія для M = %d, t = %0.2f' % (M, t_gen))
            break

        plt.plot(y1, y2, c=clr)

    plt.scatter(x1_star, x2_star, c=clr)

    return x1, x2


x1, x2 = path_optimization('g', M=3)
plt.scatter(x1, x2, c='k', label='Кроки')
# x1, x2 = path_optimization('r', M=4)
# plt.scatter(x1, x2, c='k')
# x1, x2 = path_optimization('b', M=5)
# plt.scatter(x1, x2, c='k')
# x1, x2 = path_optimization('orange', M=6)
# plt.scatter(x1, x2, c='k')
# x1, x2 = path_optimization('violet', M=7)
# plt.scatter(x1, x2, c='k')
plt.legend()
plt.show()
