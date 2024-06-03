import numpy as np
import json
import os
from gen_plot import plot_distribution, pdf, Taste_it

if __name__ == "__main__":
    txt_files = []
    for file in os.listdir("../tasks"):
        if file.endswith(".dat"):
            txt_files.append(file)
    for file in txt_files:
      with open(f"../tasks/{file}", 'r') as open_f:
        nums = np.array(json.load(open_f))/1024
        mean = nums.mean()
        std = nums.std()
        plot_distribution(nums, file, mean, std)
        test = Taste_it(nums)
        print(test.intervals())
    pdf.close()

