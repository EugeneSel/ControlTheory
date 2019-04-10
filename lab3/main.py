import numpy as np
import matplotlib.pyplot as plt

# variant 13
n = 1


def path_optimization(s0=n, v=n, l=n, phi=np.pi * n / 25):
    x_star = l * np.cos(phi)
    y_star = l * np.sin(phi)

    def s(y):
        return s0 * y

    def V(y_der, y):
        return np.sqrt((v ** 2 + s(y) ** 2 -
                        (2 * s(y) ** 2 * y_der ** 2 + 2 * v * s(y) * np.sqrt(1 + (1 - (s(y) / v) ** 2) * y_der ** 2)) / (1 + y_der ** 2)))

    # 1:
    T = 0
    x = np.zeros(1)
    y = np.zeros(1)
    x = np.append(x, [x_star], axis=0)
    y = np.append(y, [y_star], axis=0)

    T += l / V(y_star / x_star, 0)
    plt.plot(x, y, label='Траєкторія при s = 0, T = %0.2f' % T)

    # 2:
    T = 0
    x = np.zeros(1)
    y = np.zeros(1)
    x2 = x_star - n + 0.2
    x = np.append(x, [x2], axis=0)
    y = np.append(y, [y_star], axis=0)
    l_new = np.sqrt(y_star ** 2 + x2 ** 2)
    T += l_new / (V(y_star / x2, y_star) + s(y_star))
    x = np.append(x, [x_star], axis=0)
    y = np.append(y, [y_star], axis=0)
    l_new = x_star - x2
    T += l_new / s(y_star)
    plt.plot(x, y, label='Траєкторія при s = s0 * y1, T = %0.2f' % T)

    # 3:
    T = 0
    x = np.zeros(1)
    y = np.zeros(1)
    y2 = y_star - 0.1
    x = np.append(x, [x_star], axis=0)
    y = np.append(y, [y2], axis=0)
    l_new = np.sqrt(x_star ** 2 + y2 ** 2)
    T += l_new / (V(y2 / x_star, x_star) + s(x_star))
    x = np.append(x, [x_star], axis=0)
    y = np.append(y, [y_star], axis=0)
    l_new = y_star - y2
    T += l_new / (V(y_star / x_star, 0))
    plt.plot(x, y, label='Траєкторія при s = s0 * x1, T = %0.2f' % T)

    # 4:
    T = 0
    x = np.zeros(1)
    y = np.zeros(1)
    x2 = x_star - n + 0.2
    y2 = y_star - 0.05
    x = np.append(x, [x2], axis=0)
    y = np.append(y, [y2], axis=0)
    l_new = np.sqrt(x2 ** 2 + y2 ** 2)
    T += l_new / (V(y2 / x2, y2) + s(y2))
    x3 = x_star - n + 0.5
    y3 = y_star - 0.01
    x = np.append(x, [x3], axis=0)
    y = np.append(y, [y3], axis=0)
    l_new = np.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    T += l_new / (V(y3 / x3, y2) + s(y2))
    x = np.append(x, [x_star], axis=0)
    y = np.append(y, [y_star], axis=0)
    l_new = np.sqrt((x_star - x3) ** 2 + (y_star - y3) ** 2)
    T += l_new / (V(y_star / x_star, y2) + s(y2))
    plt.plot(x, y, label='Траєкторія при s = s0 * (y1 - 0.05), T = %0.2f' % T)

    # 5:
    T = 0
    x = np.zeros(1)
    y = np.zeros(1)
    x2 = x_star - n + 0.5
    y2 = y_star - 0.1
    x = np.append(x, [x2], axis=0)
    y = np.append(y, [y2], axis=0)
    l_new = np.sqrt(x2 ** 2 + y2 ** 2)
    T += l_new / (V(y2 / x2, 0))
    x3 = x_star - n + 0.9
    y3 = y_star - 0.05
    x = np.append(x, [x3], axis=0)
    y = np.append(y, [y3], axis=0)
    l_new = np.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    T += l_new / (V(y3 / x3, 0))
    x = np.append(x, [x_star], axis=0)
    y = np.append(y, [y_star], axis=0)
    l_new = np.sqrt((x_star - x3) ** 2 + (y_star - y3) ** 2)
    T += l_new / (V(y_star / x_star, 0))
    plt.plot(x, y, label='Траєкторія при s = 0, T = %0.2f' % T)

    plt.scatter(x_star, y_star, c='k')
    plt.legend()
    plt.show()

    return x, y


x, y = path_optimization()
