import argparse
from parser_arg import Pars_arg
from utils import make_write_file
from distribution import * 
from args import dist

dist_dct = {"st": st, "tr": tr, "ex": ex, "nr":nr, "gm": gm, "ln":ln, "ls": ls, "bi":bi}    

def main_1():
    parser = Pars_arg(description="Приведение к определенному  распределению", argument_default=argparse.SUPPRESS, allow_abbrev=False, add_help=False)
    parser.add_argument("-d", "--distribution", type=str, help="код распределения")
    parser.add_argument("-f", "--filename", type=str, help="имя файла")
    parser.add_argument("-p1", "-a", type=float, help="первый параметр")
    parser.add_argument("-p2", "-b", type=int, help="второй параметр")
    parser.add_argument("-p3", "-c", type=int, default=None, help="третий параметр")
    parser.add_argument("-h", "--help", action="help", help="выводит это сообщение")
    
    print (dist)
    
    args = parser.parse_args()
    
    make_write_file(dist_dct, args)
    
main_1()