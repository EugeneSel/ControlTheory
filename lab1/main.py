import numpy as np
import matplotlib.pyplot as plt

# variant 13
n = 13

def path_definition(N = 100, K = 300, s0 = n, v = n, l = n, phi = np.pi * n / 25):
    tau = l / v / N
    x1_star = l * np.cos(phi)
    x2_star = l * np.sin(phi)

    t = np.zeros(K)
    for k in range(K):
        t[k] = tau * k

    def f(x):
        return x ** 2

    x1 = np.zeros(K)
    x2 = np.zeros(K)
    u1 = np.zeros(K)
    u2 = np.zeros(K)
    lamb = np.zeros(K)
    s = np.zeros(K)

    for i in range(K - 1):
        s[i] = s0 * f(x2[i])
        lamb[i] = ((x1_star - x1[i] - s[i] * tau) ** 2 + (x2_star - x2[i]) ** 2) ** (1 / 2) * v * tau - v ** 2 * tau ** 2
        u1[i] = (x1_star - x1[i] - s[i] * tau) * v * tau / (lamb[i] + v ** 2 * tau ** 2)
        u2[i] = (x2_star - x2[i]) * v * tau / (lamb[i] + v ** 2 * tau ** 2)
        x1[i + 1] = x1[i] + (s[i] + v * u1[i]) * tau
        x2[i + 1] = x2[i] + v * u2[i] * tau

    return x1, x2, x1_star, x2_star


x1, x2, x1_star, x2_star = path_definition()
plt.plot(x1, x2, label='Графік траекторії судна')
plt.title('Графік траекторії судна')
plt.xlabel('$x1$')
plt.ylabel('$x2$')
plt.legend()
plt.scatter(x1_star, x2_star, color='red')
plt.show()

for i in range(-5, 6):
    x1, x2, x1_star, x2_star = path_definition(phi = np.pi * i / 25)
    plt.plot(x1, x2, label='phi = %f' %(np.pi * i /25))
    plt.scatter(x1_star, x2_star, color='red')
plt.title('Графік траекторії судна зі змінним параметром phi (n від -5 до 5)')
plt.xlabel('$x1$')
plt.ylabel('$x2$')
plt.legend()
plt.show()

for i in range(5, 15):
    x1, x2, x1_star, x2_star = path_definition(l = i)
    plt.plot(x1, x2, label='l = %d' %i)
    plt.scatter(x1_star, x2_star, color='red')
plt.title('Графік траекторії судна зі змінним параметром l (l від 5 до 14)')
plt.xlabel('$x1$')
plt.ylabel('$x2$')
plt.legend()
plt.show()

for i in range(5, 15):
    x1, x2, x1_star, x2_star = path_definition(s0 = i)
    plt.plot(x1, x2, label='s0 = %d' %i)
    plt.scatter(x1_star, x2_star, color='red')
plt.title('Графік траекторії судна зі змінним параметром s0 (s0 від 5 до 14)')
plt.xlabel('$x1$')
plt.ylabel('$x2$')
plt.legend()
plt.show()

for i in range(5, 15):
    x1, x2, x1_star, x2_star = path_definition(v = i)
    plt.plot(x1, x2, label='v = %d' %i)
    plt.scatter(x1_star, x2_star, color='red')
plt.title('Графік траекторії судна зі змінним параметром v (v від 5 до 14)')
plt.xlabel('$x1$')
plt.ylabel('$x2$')
plt.legend()
plt.show()

for i in np.arange(100, 500, 50):
    x1, x2, x1_star, x2_star = path_definition(N = i, K = 1000)
    plt.plot(x1, x2, label='N = %d' %i)
    plt.scatter(x1_star, x2_star, color='red')
plt.title('Графік траекторії судна зі змінним параметром N (N від 100 до 500 з кроком 50)')
plt.xlabel('$x1$')
plt.ylabel('$x2$')
plt.legend()
plt.show()
