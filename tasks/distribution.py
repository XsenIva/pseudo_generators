import numpy as np
from utils import factor
def U(x, m):
    return x / m

def st(x, a, b, m):
    return a + U(x, m) * b

def tr(x, a, b, m):
    y = []
    for i in range(0, len(x)-1, 2):
        y.append(a + b * (U(x[i], m) + U(x[i+1], m) - 1))
    return np.array(y)

def ex(x, a, b, m):
    return a - b * np.log(U(x, m))

def nr(x, a, b, m):
    y = []
    for i in range(0, len(x)-1, 2):
        base = a + b * np.sqrt(-2 * np.log(1 - U(x[i], m)))
        trig_arg = 2 * np.pi * U(x[i+1], m)
        y.append(base * np.cos(trig_arg), base * np.sin(trig_arg))
    return np.array(y)

def gm(x, a, b, c, m):
    y = []
    u = U(x, m)
    if type(c) == type(1):
        for i in range(0, len(u), c):
            y.append(a - b  * np.log(np.prod(1 - u[i:i+c])))
    else:
        k = int(c - 0.5)
        for i in range(0, len(u), 2 * k + 2):
            z1, z2 = nr([x[i], x[i+1]], 0, 1, m)
            y.append(a + b * (z1 ** 2 / 2 - np.log(np.prod(1 - u[i+2:i+k+2]))))
            y.append(a + b * (z2 ** 2 / 2 - np.log(np.prod(1 - u[i+k+2:i+2*k+2]))))
    return np.array(y)

def ln(x, a, b, m):
    return a + np.exp(b - nr(x, 0, 1, m))

def ls(x, a, b, m):
    u = U(x, m)
    return a + b * np.log(u / (1 - u))

def bi(x, a, b, m):
    y = []
    u = U(x, m)
    for i in u:
        s, k = 0, 0
        while(True):
            s += (factor(b) / (factor(k) * factor(b - k)) * (a ** k) * ((1 - a) ** (b - k)))
            if s > i:
                y.append(k)
                break
            if k < b - 1:
                k += 1
                continue
            y.append(b)
    return np.array(y)

