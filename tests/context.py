"""Module to provide context for the tests."""


class SysOverwrite:
    """For fake command line args (sys.argv)."""

    def __init__(self):
        self.argv = None

    def build_args(self, arg_string):
        self.argv = [None]
        self.argv.extend(arg_string.split())
