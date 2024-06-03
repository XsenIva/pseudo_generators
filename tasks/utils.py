import tqdm
import json
import numpy as np

def get_bit(num, num_bit):
    return (num & ( 1 << num_bit )) >> num_bit

def set_bit(num, num_bit, bit):
    mask = 1 << num_bit
    num &= ~mask
    if bit:
        return num | mask
    else:
        return num
    
def shift(num, s):
    new_num = 0
    bit = 0
    for i in range(s):
        new_num = set_bit(new_num, i, bit)
        bit = get_bit(num, i)
    new_num = set_bit(new_num, 0, bit)
    return new_num

def factor(x):
    y = 1
    for i in range(x):  y *= (i + 1)
    return y

def gen_write_file(gen, args):
    print("+-++-++-++-+_Генерирую_+-++-++-++-+")
    ans = [next(gen) % 1024 for _ in tqdm.tqdm(range(args.amount_of_numbers))]
    with open(args.filename, 'w') as fw:
        json.dump(ans, fw)
    print("+-++-++-++-+_Файл .dat готов_+-++-++-+")


def make_write_file(dist_dct, args):
    print("+-++-++-++-+_Генерирую_+-++-++-++-+")
    m = 1024
    with open(args.filename, 'r') as fr:
        nums = np.array(json.load(fr))
    if args.distribution == "gm":
        dist_nums = dist_dct[args.distribution](nums, args.p1, args.p2, args.p3, m)
    else:
        dist_nums = dist_dct[args.distribution](nums, args.p1, args.p2, m)
    np.savetxt(f"dist-{args.distribution}.dat", dist_nums, fmt='%1.4f')
    print("+-++-++-++-+_Файл .dat готов_+-++-++-+")