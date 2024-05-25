from utils import set_bit, get_bit, shift
from args_gen import args_for_gen


def lc(args=args_for_gen["lc"]):
    a = int(args[0])
    c = int(args[1])
    mod = int(args[2])
    x_n = int(args[3]) 
    while(True):
        x_n = (x_n * a + c) % mod
        yield x_n


def add(args=args_for_gen["add"]):
    mod, k, j = int(args[0]), int(args[1]), int(args[2])
    x = list(map(int, args[3:]))
    i = 55
    while(True):
        val = (x[i-k] + x[i-j]) % mod
        x.append(val)
        i += 1
        yield val



def fp(args=args_for_gen["fp"]):
    p, w, x = int(args[0]), int(args[4]), int(args[5])
    mask_w, mask_p = 0, 0
    list_par = list(map(int, args[1:4]))
    list_par.append(0)

    for i in range(w):
        mask_w = set_bit(mask_w, i, 1)
    for i in range(p):
        mask_p = set_bit(mask_p, i, 1)

    while(True):
        cur_bit = 0
        for i in list_par:
            cur_bit ^= get_bit(x, i)
        x = shift(x, p)
        x = set_bit(x, 0, cur_bit)
        x = x & mask_p
        yield x & mask_w



def lfsr(args=args_for_gen["lfsr"]):
    s, x, y = len(args[1]), int(args[0], 2), int(args[1], 2)
    while(True):
        current = 0
        for i in range(s):
            current ^= get_bit(x, i) * get_bit(y, i)
        y = shift(y, s)
        y = set_bit(y, 0, current)
        yield y



def nfsr(args=args_for_gen["nfsr"]):
    r1 = lfsr([args[0], args[3]])
    r2 = lfsr([args[1], args[4]])
    r3 = lfsr([args[2], args[5]])
    w1 = 0
    for i in range(int(args[6])):
        w1 = set_bit(w1, i, 1)
    while True:
        a = next(r1)
        b = next(r2)
        c = next(r3)
        yield (a ^ b + b ^ c + c) & w1

def rc4(args=args_for_gen["rc4"]):
    k = list(map(int, args[:-2]))
    w = int(args[-1])
    l = len(k)
    s = [i for i in range(l)]
    j = 0
    for i in range(l):
        j = (j + s[i] + k[i]) % l
        s[i], s[j] = s[j], s[i]
    i = 0
    while(True):
        num = 0
        for t in range(w):
            i = (i + 1) % l
            j = (j + s[i]) % l
            s[i], s[j] = s[j], s[i]
            num = set_bit(num, t, s[(s[i] + s[j]) % l] & 1)
        yield num

def rsa(args=args_for_gen["rsa"]):
    n = int(args[0])
    e = int(args[1])
    x = int(args[2])
    w = int(args[3])
    while(True):
        z = 0
        for i in range(w):
            x = x ** e % n
            z = set_bit(z, w - i - 1, x & 1)
        yield z

def bbs(args=args_for_gen["bbs"]):
    p, q = 127, 131
    n = p * q
    x, w = int(args[0]), int(args[1])
    while(True):
        z = 0
        for i in range(w):
            x = x * x % n
            z = set_bit(z, w - i - 1, x & 1)
        yield z

def mt(args=args_for_gen["mt"]):
    p, w, r, q, a, u, s, t, l, b, c = 624, 32, 31, 397, 2567483615, 11, 7, 15, 18, 2636928640, 4022730752
    mod = int(args[0])
    MT = [int(args[1])]
    lower_mask = (1 << r) - 1
    upper_mask = (~lower_mask * -1) & w1
    w1 = 0
    ind = p

    for i in range(w):
        w1 = set_bit(w1, i, 1)

    for i in range(1, p):
        MT.append((MT[i - 1] ^ (MT[i - 1] >> 30)) + i)

    while(True):
        if (ind >= p):
            for i in range(p):
                x = (MT[i] & upper_mask) + (MT[(i + 1) % p] & lower_mask)
                xA = x >> 1
                if (x & 1):
                    xA ^= a
                MT[i] = MT[(i + q) % p] ^ xA
            ind = 0
        y = MT[ind]
        ind += 1
        y ^= (y >> u)
        y ^= (y << s) & b
        y ^= (y << t) & c
        y ^= (y >> l)
        yield y % mod
