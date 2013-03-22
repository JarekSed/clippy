import random

def run_prank():
    """ Return message saying something absurd and funny. """
    messages = [
        "You look like you have a hard drive. Now running `dd if=/dev/null of=/dev/sda...",
        "It looks like your CPU is using energy. To conserver power, I'll now slow the clock speed down 10%",
        "You appear to be using an unsupported bootloader. Installing MSBoot from MSDN and configuring Boot.ini",
        "Your motherboard appears to be abnormally hot. Shut down immediately to avoid fire.",
        "ERROR: PC LOAD LETTER",
    ]
    return True, random.choice(messages)
