#!/usr/bin/env python3
import os
import subprocess
import signal

# List of guide files in the cycle. Add paths here to expand the book!
GUIDES = [
    os.path.expanduser("~/keyboard_shortcuts.txt"),
    os.path.expanduser("~/nvim_shortcuts.txt")
]

pid_file = "/tmp/guide_alacritty_pid"
idx_file = "/tmp/guide_alacritty_idx"

# Check if Alacritty is already running from this script
alacritty_pid = None
if os.path.exists(pid_file):
    with open(pid_file, "r") as f:
        try:
            alacritty_pid = int(f.read().strip())
        except ValueError:
            pass

# Check if process is active
is_running = False
if alacritty_pid:
    try:
        os.kill(alacritty_pid, 0)  # Signal 0 checks process existence
        is_running = True
    except OSError:
        pass

if not is_running:
    # First press: Spawn first guide
    proc = subprocess.Popen(["alacritty", "-t", "Shortcuts Guide", "-e", "nvim", GUIDES[0]])
    with open(pid_file, "w") as f:
        f.write(str(proc.pid))
    with open(idx_file, "w") as f:
        f.write("0")
else:
    # Read current index
    current_idx = 0
    if os.path.exists(idx_file):
        with open(idx_file, "r") as f:
            try:
                current_idx = int(f.read().strip())
            except ValueError:
                pass
    
    next_idx = current_idx + 1
    
    # Kill the existing guide window
    try:
        os.kill(alacritty_pid, signal.SIGTERM)
    except OSError:
        pass
        
    if next_idx < len(GUIDES):
        # Next press: Spawn next guide in cycle
        proc = subprocess.Popen(["alacritty", "-t", "Shortcuts Guide", "-e", "nvim", GUIDES[next_idx]])
        with open(pid_file, "w") as f:
            f.write(str(proc.pid))
        with open(idx_file, "w") as f:
            f.write(str(next_idx))
    else:
        # Final press: Cycle finished, clean up files
        if os.path.exists(pid_file):
            os.remove(pid_file)
        if os.path.exists(idx_file):
            os.remove(idx_file)
