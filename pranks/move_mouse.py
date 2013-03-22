import random
from Xlib import X, display

def run_prank():
    """ Moves the mouse to a random location on the screen.
        Returns a message saying the mouse was moved."""
    d = display.Display()
    num_screens = d.screen_count()
    s = d.screen(random.randrange(0, num_screens) )
    root = s.root
    root.warp_pointer(random.randrange(0, s.width_in_pixels), random.randrange(0, s.height_in_pixels) )
    d.sync()
    return (True, 'It looks like you are using a mouse. Let me help you move it')
