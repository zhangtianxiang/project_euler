#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse
import os
import traceback

# colors
red = '\033[0;31m{}\033[0m'
green = '\033[0;32m{}\033[0m'

lang_config = {
    "cpp": {
        "name": "c++",
        "builder": lambda id, dir: (
            os.system(
                f"g++ -o {os.path.join(dir,id, id)}.tmp {os.path.join(dir,id, id)}.cpp  -std=c++17 -Wall") == 0
        ),
        "runner": lambda id, dir: (
            os.system(f"{os.path.join(dir,id, id)}.tmp") == 0
        )
    },
    "go": {
        "name": "golang",
        "builder": lambda id, dir: (
            os.system(
                f"go build -o {os.path.join(dir,id, id)}.tmp {os.path.join(dir,id,id)}.go") == 0
        ),
        "runner": lambda id, dir: (
            os.system(f"{os.path.join(dir,id,id)}.tmp") == 0
        ),
    }
}


def cprint(text, color):
    print(color.format(text))


def get_id_dir():
    parser = argparse.ArgumentParser()
    parser.add_argument(f'id', type=str)
    parser.add_argument(f'-dir', type=str, required=False,
                        default='./solutions')
    return parser.parse_args().id, parser.parse_args().dir


def get_lang(id, dir):
    p = os.path.join(dir, id, id)
    for suf in lang_config.keys():
        pp = p+'.'+suf
        if os.path.exists(pp):
            return suf
    return ''


def build(id, dir, lang):
    return lang_config[lang]["builder"](id, dir)


def run(id, dir, lang):
    return lang_config[lang]["runner"](id, dir)


def main():
    id, dir = get_id_dir()

    lang = get_lang(id, dir)

    if lang == '':
        cprint('\nCannot find', red)
        return

    cprint('Building', green)

    if not build(id, dir, lang):
        cprint('\nBuild failed', red)
        return

    cprint('Running', green)

    if not run(id, dir, lang):
        cprint('\nRun failed', red)
        return

    cprint('\nFinished', green)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint('\nStopped', red)
    except Exception as e:
        cprint('\nError', red)
        traceback.print_exc()
