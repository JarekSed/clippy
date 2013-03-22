import random
import subprocess

def run_prank():
    """ Randomly switches focus to a window.
    Return message saying that focus was switched"""

    list_windows_command = 'wmctrl -l | cut -d " " -f 5-'
    focus_window_command = 'wmctrl -a {window_id}'

    list_proc = subprocess.Popen(list_windows_command, shell=True, stdout=subprocess.PIPE)
    if list_proc.wait():
        return False, "Failed to list windows"
    windows = list_proc.stdout.read().split('\n')
    window_to_focus = random.choice(windows)
    switch_proc = subprocess.Popen(focus_window_command.format(window_id=window_to_focus), shell=True, stdout=subprocess.PIPE)
    if switch_proc.wait():
        return False, "Failed to list windows"
    return True, 'It looks like you are managing some windows. Let me help youfocus on {window_id}'.format(window_id=window_to_focus)


