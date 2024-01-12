#!/usr/bin/python3
"""
Module for console
"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb)"
    __classes = {
        "BaseModel"
    }

    def do_quit(self, arg):
        """
        Quit command to quit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Handles End Of File character.
        """
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel.
        """
        argurment1 = parse(arg)
        if len(argurmentl) == 0:
            print("** class name missing **")
        elif argurmentl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argurmentl[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name.
        """
        pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name.
        """
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
