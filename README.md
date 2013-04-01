clippy
======

Clippy is a program that runs pranks on a linux system. 
This was made for April Fools 2013. 
It should be run from upstart or monit or something, so it will respawn when killed. 
After all, people might not realize how much they need it, and foolishly try to escape. 
It should be really easy to add new pranks, just drop a python file in pranks/ that has a run_prank() method.


This should really have better error checking and such, it was just quickly slapped together as a joke.
