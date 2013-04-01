#!/usr/bin/python2.7

import gtk,gobject
import egg.trayicon
import random

import signal

import pynotify

import glob, imp
import os.path
from os.path import join, basename, splitext

clippy_image = os.path.abspath(os.path.curdir) + "/clippy.png"
clippy_icon = os.path.abspath(os.path.curdir) + "/clippy_small_transparent.png"

class Pranks:
    """ This class is responsible for loading, selecting, and running pranks. """

    def importprankModulesIn(self, directory):
        """Dyanmically load all python modules in the pranks directory.
        Returns a dict of names to modules. """
        modules = {}
        for path in glob.glob(join(directory,'[!_]*.py')): # list .py files not starting with '_'
            name, ext = splitext(basename(path))
            modules[name] = imp.load_source(name, path)
        return modules

    def __init__(self, prank_dir="pranks"):
        self.pranks = self.importprankModulesIn(prank_dir)

    def run_random_prank(self, sender=None, event=None):
        """ Selects a random prank, and runs it. The prank must support
        the prank interface (run_prank(), returning tuple of
        (status,message)"""

        name = random.choice(self.pranks.keys())
        res,msg = self.pranks[name].run_prank()

        self.send_msg(msg)

    def send_msg(self, msg):
        n = pynotify.Notification("Alert!", msg, clippy_image)
        n.show()


def main():
    pynotify.init("Clippy")

    pranks = Pranks()

    statusicon = gtk.StatusIcon()
    statusicon.set_from_file(clippy_icon)
    statusicon.set_visible(True)

    statusicon.connect("button-press-event", pranks.run_random_prank)
    #commented for testing purposes
    #gobject.timeout_add(30*1000, pranks.run_random_prank)

    gtk.main()

if __name__ == '__main__':
    main()
