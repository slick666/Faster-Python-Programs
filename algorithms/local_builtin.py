"""Local vs. built-in.
"""

import sys

if sys.version_info.major < 3:
    range = xrange


def repeat(counter):
    """Using the built-in `True` in a loop.
    """
    for count in range(counter):
        True


def repeat_local(counter):
    """Making `True` a local variable.
    """
    true = True
    for count in range(counter):
        true


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
