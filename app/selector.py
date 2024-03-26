#!/usr/bin/env python3

import fnmatch
import os
import subprocess
import time
from random import choice
from random import randint
from subprocess import PIPE
from subprocess import run
from time import sleep


def find(patterns, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
    return result


def asciiquarium(timeout=60):
    os.system('clear')
    return run("asciiquarium", timeout=timeout)


def cmatrix(timeout=60):
    os.system('clear')
    colors = ["green", "red", "blue", "white", "yellow", "cyan", "magenta", "black"]
    return run(["cmatrix", "-b", "-C", choice(colors)], timeout=timeout)


def cbonsai(timeout=60):
    os.system('clear')
    return run(["cbonsai", "-i", "-l"], timeout=timeout)


def lavat(timeout=60):
    os.system('clear')
    color = choice(["red", "blue", "yellow", "green", "cyan", "magenta"])
    return run(["lavat", "-c", color], timeout=timeout)


def pipes(timeout=60):
    os.system('clear')
    return run(["pipes.sh"], timeout=timeout)


def cowfortune(timeout=60):
    os.system('clear')
    start_time = time.time()
    end_time = start_time + timeout

    run(["cowfortune"], timeout=timeout)

    while True:
        sleep(1)
        if end_time < time.time():
            return


def bmon(timeout=60):
    os.system('clear')
    return run(["bmon", "--show-all"], timeout=timeout)


def htop(timeout=60):
    os.system('clear')
    return run(["htop"], timeout=timeout)


def code(timeout=60):
    os.system('clear')
    start_time = time.time()
    end_time = start_time + timeout

    filelist = find(['*.c', '*.h', '*.pl', '*.sh', '*.bash', '*.java', '*.cpp', '*.py'], '/usr/local/src')
    file = choice(filelist)

    pygmentize = run(["pygmentize", file], stdout=PIPE, encoding="UTF-8", timeout=timeout)

    for s in pygmentize.stdout:
        print(s, end="")
        sleep(0.01)
        if end_time < time.time():
            return


def jp2a(timeout=60):
    os.system('clear')
    start_time = time.time()
    end_time = start_time + timeout

    filelist = find(["*.jpg", "*.jpeg", "*.png"], "/usr")

    while True:
        file = choice(filelist)
        run(["jp2a", "--colors", "--clear", "--term-fit", file])
        sleep(10)
        if end_time < time.time():
            return


def world_map(timeout=60):
    os.system('clear')
    run(["jp2a", "--colors", "--clear", "--term-fit", "/app/world_map.jpg"])
    sleep(10)


def random_process(timeout=60):
    plist = [
        asciiquarium,
        cbonsai,
        cmatrix,
        cowfortune,
        lavat,
        pipes,
        code,
        jp2a,
        world_map,
    ]
    return choice(plist)(timeout=timeout)


sleep(1.0)
timeout_bounds = [10, 60]

while True:
    try:
        random_process(timeout=randint(*timeout_bounds))
    except subprocess.TimeoutExpired:
        pass
