import argparse
from parser_arg import Pars_arg
from generators import * 
from args import met, por
from utils import gen_write_file


gens_dct = {"lc": lc, "mt": mt, "add": add, "5p":fp, "lfsr": lfsr, "nfsr":nfsr, "rc4": rc4, "rsa":rsa, "bbs":bbs}


if __name__ == "__main__":
    parser = Pars_arg(description="Генераторы", argument_default=argparse.SUPPRESS, allow_abbrev=False, add_help=False)
   
    parser.add_argument("-g", "--generator", type=str, help="укажите генератор")
    parser.add_argument("-n", "--amount_of_numbers", type=int, default=10000, help="кол-во генерируемых чисел")
    parser.add_argument("-i", "--init", type=str, help="иниц. вектор генератора")
    parser.add_argument("-f", "--filename", type=str, default="random_sequence.dat", help="имя файла")
    parser.add_argument("-h", "--help", action="help", help="выводит это сообщение") 
    
    print(met)
    print(por)

    args = parser.parse_args(namespace=None)
    gen = gens_dct[args.generator](args.init.split(sep=","))
    
    gen_write_file(gen, args)
 
