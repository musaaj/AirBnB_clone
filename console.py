#!/usr/bin/python3
"""console provides a an intereactive console to work
with objects. The modules supports creating, updating,
displaying and destroying objects. It can also work non
intereactive.
"""
import cmd
from models.base_model import BaseModel
import models
from helper.line_parser import parse_line



class HBNBCommand(cmd.Cmd):
    """ creates a command line interpreter and handle
    parsing and executing commands
    """
    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel
            }

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit programm"""
        exit()

    def do_EOF(self, line):
        """Do nothing when command is not given"""
        return True
    def precmd(self, line):
        return line
    
    def do_create(self, class_name):
        """create an instance of a class

        Args
            class_name: builtin class name, eg BaseModel
        """
        if not class_name:
            print('** class name missing **')
            return False
        if class_name in self.classes:
            obj = self.classes[class_name]()
            obj.save()
        else:
            print('** class doesn\'t exist **')

    def do_show(self, args):
        """show an instance of a class of class name
        """
        args = parse_line(args)
        if not args:
            print('** class name missing **')
            return False
        if len(args) < 2:
            print('** instance id missing **')
            return False
        class_name, id = args
        if class_name not in self.classes:
            print('** class doesn\'t exist **')
            return False
        obj = models.storage.get('{}.{}'.format(class_name,id))
        if not obj:
            print('** no instance found **')
        else:
            print(obj)
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
