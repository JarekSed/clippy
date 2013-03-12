#!/usr/bin/env python2

import gtk,gobject
import egg.trayicon

import glob, imp
from os.path import join, basename, splitext

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

        #TODO: this runs every prank, for testing. This should randommly select
        # and run only one.
        for name, prank in self.pranks.iteritems():
            res,msg = prank.run_prank()
            print "ouput of", name +":", res,msg


def main():
    pranks = Pranks()
    tray = egg.trayicon.TrayIcon("TrayIcon")
    box = gtk.EventBox()
    label = gtk.Label("clippy goes here")
    box.add(label)
    tray.add(box)
    tray.show_all()

    box.connect("button-press-event", pranks.run_random_prank)

    gobject.timeout_add(30*1000, pranks.run_random_prank)

    gtk.main()

if __name__ == '__main__':
    main()
