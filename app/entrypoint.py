#!/usr/bin/env python3

from subprocess import run
from random import randint

session = randint(1, 2**32)
command = "/app/selector.py"

run(["tmux", "new-session", "-d", "-s", str(session), command])
run(["tmux", "split-window", "-v", "-t", f"{session}:0.0", command])
run(["tmux", "split-window", "-h", "-t", f"{session}:0.0", command])
run(["tmux", "split-window", "-h", "-t", f"{session}:0.2", command])
run(["tmux", "attach-session", "-t", f"{session}"])
