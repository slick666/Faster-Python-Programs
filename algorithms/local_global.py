# file: local_global.py

"""Local vs. built-in.
"""

import sys

if sys.version_info.major < 3:
    range = xrange

GLOBAL = 1


def repeat(counter):
    """Using the GLOBAL value directly.
    """
    for count in range(counter):
        GLOBAL


def repeat_local(counter):
    """Making GLOBAL a local variable.
    """
    local = GLOBAL
    for count in range(counter):
        local


def test(counter):
    """Call both functions.
    """
    repeat(counter)
    repeat_local(counter)


if __name__ == '__main__':

    def do_profile():
        """Check the run times.
        """
        import cProfile
        profiler = cProfile.Profile()
        profiler.run('test(int(1e8))')
        profiler.print_stats()

    do_profile()
