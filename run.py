#!/opt/anaconda3/bin/python
# -*- coding: UTF-8 -*-

import json
from common import *

import os
import traceback

LANG_NAME = "lang_name"
COMPILER_PATH = "compiler_path"
BUILDER = "builder"
RUNNER = "runner"
COMPILER_PATH_JSON = "compiler_path.json"

ext_config = {
    "cpp": {
        LANG_NAME: "c++",
        COMPILER_PATH: "g++",
        BUILDER: lambda id, dir, compiler: (
            os.system(
                f"{compiler} -o {os.path.join(dir,id, id)}.tmp {os.path.join(dir,id, id)}.cpp  -std=c++17 -Wall") == 0
        ),
        RUNNER: lambda id, dir: (
            os.system(f"{os.path.join(dir,id, id)}.tmp") == 0
        )
    },
    "go": {
        LANG_NAME: "golang",
        COMPILER_PATH: "go",
        BUILDER: lambda id, dir, compiler: (
            os.system(
                f"{compiler} build -o {os.path.join(dir,id, id)}.tmp {os.path.join(dir,id,id)}.go") == 0
        ),
        RUNNER: lambda id, dir: (
            os.system(f"{os.path.join(dir,id,id)}.tmp") == 0
        ),
    }
}


def get_ext(id, dir):
    p = os.path.join(dir, id, id)
    for ext in ext_config.keys():
        pp = p+'.'+ext
        if os.path.exists(pp):
            return ext
    return ''


def build(id, dir, ext):
    compiler_path = ext_config[ext][COMPILER_PATH]
    if os.path.exists(COMPILER_PATH_JSON):
        with open(COMPILER_PATH_JSON, "r") as f:
            obj = json.load(f)
            assert type(obj) is dict
            if ext in obj:
                p = obj[ext]
                assert type(p) is str
                compiler_path = p
    return ext_config[ext][BUILDER](id, dir, compiler_path)


def run(id, dir, ext):
    return ext_config[ext][RUNNER](id, dir)


def main():
    id, dir = arg_id_dir()

    ext = get_ext(id, dir)

    if ext == '':
        cprint('Cannot find known extension file', red)
        return

    cprint(f'Found {ext} file', green)

    cprint('Building', green)

    if not build(id, dir, ext):
        cprint('Build failed', red)
        return

    cprint('Running', green)

    if not run(id, dir, ext):
        cprint('Run failed', red)
        return

    cprint('Finished', green)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint('Stopped', red)
    except Exception as e:
        cprint('Error', red)
        traceback.print_exc()
