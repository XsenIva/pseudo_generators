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
    new_num =