import random

def run_prank():
    """ Return message saying something absurd and funny. """
    messages = [
        "You look like you have a hard drive. Now running `dd if=/dev/null of=/dev/sda...",
        "It looks like your CPU is using energy. To conserver power, I'll now slow the clock speed down 10%",
        "You appear to be using an unsupported bootloader. Installing MSBoot from MSDN and configuring Boot.ini",
        "Your motherboard appears to be abnormally hot. Shut down immediately to avoid fire.",
        "ERROR: PC LOAD LETTER",
        "You appear to have custom vim settings in ~/.vimrc. Let me remove them for you.",
        "You appear to have custom bash settings in ~/.bashrc. Let me remove them for you.",
        "You appear to have a login shell. Login shells have been determined dangerous, let me change that to /bin/false for you.",
        "Executable named 'halt' detected in $PATH. Due to security reasons, it has been disabled.",
		"Emailing stream of profanities to root@nbcs for your convenience.",
		"Thank you for signing up for Cat Facts. You will now receive fun daily facts about CATS!",
		"It appears you are trying to migrate away from solaris. Shutting down all solaris systems now.",
		"To terminate this program, text HALT to 46645 now.",
        "Have you called your mother recently?",
        "Executing 'dd if=/dev/urandom of=/dev/mem' now.",
        "Replacing every third bit of /dev/sda1 with 0.",
        "MAIN SCREEN TURN ON",
        "YOU HAVE NO CHANCE TO SURVIVE MAKE YOUR TIME",
        "Launching all zig. For great justice.",

    ]
    return True, random.choice(messages)
