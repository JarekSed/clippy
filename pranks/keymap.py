import random
import string
import subprocess

def run_prank():
    """ Randomly swaps 2 keys on the keyboard.
    Return message saying what keys where swapped. """

    swap_command = 'xmodmap -e "keycode {code} = {key}"'
    get_command = 'xmodmap -pk | grep "({key})"'

    alphanum = string.lowercase + string.digits
    key1 = random.choice(alphanum)
    key2 = random.choice(alphanum)

    get_code1 = subprocess.Popen(get_command.format(key=key1), shell=True, stdout=subprocess.PIPE)
    get_code2 = subprocess.Popen(get_command.format(key=key2), shell=True, stdout=subprocess.PIPE)

    code1 = get_code1.stdout.read().split()[0]
    code2 = get_code2.stdout.read().split()[0]


    subprocess.Popen(swap_command.format(code=code2,key=key1), shell=True)
    subprocess.Popen(swap_command.format(code=code1,key=key2), shell=True)

    return True, 'swapping {key1} and {key2}'.format(key1=key1, key2=key2)
