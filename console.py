#!/usr/bin/python3
import cmd

class AirBnBCmd(cmd.Cmd):
    prompt = '(AirBnB)'

    def do_quit(self, arg):
        exit()

    def help_quit(self):
        return 'quite the process'

if __name__ == '__main__':
    AirBnBCmd().cmdloop()
