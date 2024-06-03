import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pdf = PdfPages("allplots.pdf") 

def make_plot(size, mean_array, title, std_array, mat_o, kv_o):
    plt.rc('font', size=7)
    s= "\n" + title + "\n" + "M(X) = " + str(mat_o) + "\n" + "σ(X) = " + str(kv_o)
    plt.title(s)
    plt.plot(size, mean_array, label="M(X)", color="r")
    plt.plot(size, std_array, label="σ(X)", color="c")
    plt.legend()
    plt.ylabel("Оценка")
    plt.xlabel("Выборкa")
    pdf.savefig()
    plt.close()

def plot_distribution(nums, title, mat_o, kv_o):
    size = []
    mean_array = []
    std_array = []
    for i in range(len(nums)):
        size.append(i+1)
        mean_array.append(nums[:i+1].mean())
        std_array.append(nums[:i+1].std())
    make_plot(size, mean_array, title, std_array, mat_o, kv_o)

class Taste_it:
    def __init__(self, nums, alpha=0.5):
        self.nums = nums
        self.alpha = alpha

    def cnt_two(self, observed=None, expected=None, k=None):
        if observed is None:
            _, observed = np.unique(self.nums, return_counts=True)
        if k is None:
            k = len(np.unique(self.nums))
        if expected is None:
            expected = np.array([self.nums.shape[0] / k] * k)
        stat = np.sum((observed - expected) ** 2 / expected)
        crt = stats.cnt_two.ppf(1 - self.alpha, k - 1)
        return stat <= crt
    
    def series(self, d=8):
        observed = np.array((d * d) * [0])
        nums = self.nums.copy()
        for i in range(self.nums.shape[0] // 2):
            q, r = int(nums[2 * i] * d), int(nums[2 * i + 1] * d)
            observed[q * d + r] += 1
        expected = np.array(d ** 2 * [self.nums.shape[0] / (2 * d ** 2)])
        return self.cnt_two(observed, expected, d * d)
    
    def intervals(self, n=256, t=10, a=0.5, b=1):
        j, s, c = -1, 0, (t+1) * [0]
        while s < n:
            r = 0
            j += 1
            while (a <= self.nums[j] and self.nums[j] <= b) and j < self.nums.shape[0]:
                r += 1
                j += 1
            c[min(r, t)] += 1
            s += 1
        p = b - a
        expected = [n * p * (1.0 - p) ** r for r in range(t)] + [n * (1.0 - p) ** t]
        return self.cnt_two(np.array(c), np.array(expected), t)

