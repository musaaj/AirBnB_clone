#!/usr/bin/python3
"""console provides a an intereactive console to work
with objects. The modules supports creating, updating,
displaying and destroying objects. It can also work non
intereactive.
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ creates a command line interpreter and handle
    parsing and executing commands
    """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, line):
        """quit the interpreter"""
        exit()

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
