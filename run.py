#!/opt/anaconda3/bin/python
# -*- coding: UTF-8 -*-

from common import *

import os
import traceback


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
    id, dir = arg_id_dir()

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
