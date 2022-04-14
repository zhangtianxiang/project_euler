# -*- coding: UTF-8 -*-

import argparse

# colors
red = '\033[0;31m{}\033[0m'
green = '\033[0;32m{}\033[0m'


def cprint(text, color):
    print(color.format(text))


def arg_id_dir():
    parser = argparse.ArgumentParser()
    parser.add_argument(f'id', type=str)
    parser.add_argument(f'-dir', type=str, required=False,
                        default='./solutions')
    return parser.parse_args().id, parser.parse_args().dir
