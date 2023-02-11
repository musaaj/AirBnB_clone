#!/usr/bin/python3
"""console provides a an intereactive console to work
with objects. The modules supports creating, updating,
displaying and destroying objects. It can also work non
intereactive.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
import models
from helper.line_parser import parse_line



class HBNBCommand(cmd.Cmd):
    """ creates a command line interpreter and handle
    parsing and executing commands
    """
    prompt = '(hbnb) '
    classes = {
              'BaseModel': BaseModel,
              'User': User,
              'State': State,
              'City': City,
              'Amenity': Amenity
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

    def do_show(self, line):
        """show an instance of a class of class name
        """
        line = parse_line(line)
        if not line:
            print('** class name missing **')
            return False
        if len(line) < 2:
            print('** instance id missing **')
            return False
        class_name, id = line
        if class_name not in self.classes:
            print('** class doesn\'t exist **')
            return False
        obj = models.storage.get('{}.{}'.format(class_name,id))
        if not obj:
            print('** no instance found **')
        else:
            print(obj)

    def do_destroy(self, line):
        """delete an instance of class name"""
        line = parse_line(line)
        length = len(line)
        if not line:
            print('** class name missing **')
            return False
        if length < 2:
            print('** instance id missing **')
            return False
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return False
        if not models.storage.destroy(
                  '{}.{}'.format(line[0], line[1])
                ):
            print('** no instance found **')

    def do_all(self, line):
        """prints all objects in storage based
        or not based on a class name
        """
        if not line:
            objects = [
                      str(obj)
                      for key, obj
                      in models.storage.all().items()
                    ]
            print(objects)
            return False
        if line not in self.classes:
            print('** class doesn\'t exist **')
            return False
        objects = [
                  str(obj) for key, obj in
                  models.storage.all().items()
                  if obj.__class__.__name__ == line
                ]
        print(objects)

    def do_update(self, line):
        not_to_be_updated = [
                  'id',
                  'created_at',
                  'updated_at'
                ]
        obj = None
        if not line:
            print('** class name missing **')
            return False
        line = parse_line(line)
        length = len(line)
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return False
        if length < 2:
            print('** instance id missing **')
            return False
        obj = models.storage.get(
                  '{}.{}'.format(line[0], line[1])
                )
        if not obj:
            print('** no instance found **')
            return False
        if length < 3:
            print('** attribute name missing **')
            return False
        if length < 4:
            print('** value missing **')
            return False
        if line[2] not in not_to_be_updated:
            obj.__setattr__(line[2], line[3])
            obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
