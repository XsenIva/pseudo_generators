import argparse
import tqdm
import json
from parser_arg import Pars_arg
from generators import * 


gens_dct = {"lc": lc, "mt": mt, "add": add, "5p":fp, "lfsr": lfsr, "nfsr":nfsr, "rc4": rc4, "rsa":rsa, "bbs":bbs}

if __name__ == "__main__":
    parser = Pars_arg(description="Генераторы", argument_default=argparse.SUPPRESS, allow_abbrev=False, add_help=False)
   
    parser.add_argument("-g", "--generator", type=str, help="укажите генератор")
    parser.add_argument("-n", "--amount_of_numbers", type=int, default=10000, help="кол-во генерируемых чисел")
    parser.add_argument("-i", "--init", type=str, help="иниц. вектор генератора")
    parser.add_argument("-f", "--filename", type=str, default="random_sequence.dat", help="имя файла")
    parser.add_argument("-h", "--help", action="help", help="выводит это сообщение") 
    
    args = parser.parse_args(namespace=None)
    gen = gens_dct[args.generator](args.init.split(sep=","))
    
    
    print("--------Генерирую")
    ans = [next(gen) % 1024 for _ in tqdm.tqdm(range(args.amount_of_numbers))]
    with open(args.filename, 'w') as fw:
        json.dump(ans, fw)
    print("--------Файл .dat готов")

