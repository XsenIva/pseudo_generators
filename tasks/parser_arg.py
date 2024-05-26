import argparse
import textwrap
import os
import sys


class Pars_arg(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        super(Pars_arg, self).__init__(*args, **kwargs)
        self.program = {key: kwargs[key] for key in kwargs }
        self.options = []

    def add_argument(self, *args, **kwargs):
        super(Pars_arg, self).add_argument(*args, **kwargs)
        option = {}
        option["flags"] = [ item for item in args ]
        for key in kwargs:
            option[key] = kwargs[key]
        self.options.append(option)

    def print_help(self):
        wrapper = textwrap.TextWrapper(width=80)

        if "usage" in self.program:
            print("Usage: %s" % self.program["usage"])
        else:
            usage = []
            for option in self.options:
                usage += [ "[%s %s]" % (item, option["metavar"]) if "metavar" in option else "[%s %s]" % (item, option["dest"].upper()) if "dest" in option else "[%s]" % item for item in option["flags"] ]
            wrapper.initial_indent = "Usage: %s " % os.path.basename(sys.argv[0])
            wrapper.subsequent_indent = len(wrapper.initial_indent) * " "
            res = str.join(" ", usage)
            res = wrapper.fill(res)
            print(res)
        print()

        if "description" in self.program:
            print(self.program["description"])
            print()

        print("аргументы:")
        maxlen = 0
        for option in self.options:
            option["flags2"] = str.join(", ", [ "%s %s" % (item, option["metavar"]) if "metavar" in option else "%s %s" % (item, option["dest"].upper()) if "dest" in option else item for item in option["flags"] ])
            if len(option["flags2"]) > maxlen:
                maxlen = len(option["flags2"])
        for option in self.options:
            template = "  %-" + str(maxlen) + "s  "
            wrapper.initial_indent = template % option["flags2"]
            wrapper.subsequent_indent = len(wrapper.initial_indent) * " "
            if "help" in option and "default" in option:
                res = option["help"]
                res += " (по умолчанию: '%s')" % option["default"] if isinstance(option["default"], str) else " (по умолчанию: %s)" % str(option["default"])
                res = wrapper.fill(res)
            elif "help" in option:
                res = option["help"]
                res = wrapper.fill(res)
            elif "default" in option:
                res = "По умолчанию: '%s'" % option["default"] if isinstance(option["default"], str) else "Default: %s" % str(option["default"])
                res = wrapper.fill(res)
            else:
                res = wrapper.initial_indent
            print(res)
           
    