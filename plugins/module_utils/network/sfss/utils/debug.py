from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
filename = "./sfss_debug.txt"


def debug(key="Start ...", output=""):
    with open(filename, "a+", encoding='utf-8', errors='ignore') as debug_file:
        debug_file.write(str(key))
        debug_file.write("\n")
        debug_file.write(str(output))
        debug_file.write("\n")
