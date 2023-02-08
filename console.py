#!/usr/bin/python3
"""console provides a an intereactive console to work
with objects. The modules supports creating, updating,
displaying and destroying objects. It can also work non
intereactive.
"""
import cmd
import sys


def parse(ls):
    """make a one line string from a list of strings

    Description:
        The functions is meant to work only with
        sys.argv. It concanates arguments passed
        excluding the program name

    Args:
        ls: argv

    Return: string
    """
    return ''.join(ls[1:])


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
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(parse(sys.argv))
    else:
        HBNBCommand().cmdloop()
