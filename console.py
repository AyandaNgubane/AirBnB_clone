#!/usr/bin/python3
"""
Command interpreter
"""

import cmd
import models
from models.base_model import BaseModel
from datetime import datetime
import re

my_classes = {"BaseModel" : BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """

    prompt = "(hbnb) "


    def do_quit(self, line):
        """
        to exit the program
        """
        
        return True

    def do_EOF(self, line):
        """
        to exit the program
        """

        return True

    def emptyline(self):
        """
        When an empty line is entered in response to the prompt,
        it won't repeat the last nonempty command entered.
        """

        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        If the class name is missing,
        print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ create MyModel)
        """

        c_name = self.parseline(line)[0]

        if c_name == "" or c_name is None:
            print("** class name missing **")

        elif c_name not in my_classes:
            print("** class doesn't exist **")

        else:
            new_instance = my_classes[c_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing ** (ex: $ show)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ show MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ show BaseModel 121212)
        """

        c_name = self.parseline(line)[0]
        i_id = self.parseline(line)[1]

        if c_name == "" or c_name is None:
            print("** class name missing **")

        elif c_name not in my_classes:
            print("** class doesn't exist **")

        elif i_id == "" or i_id is None:
            print('** instance id missing **')

        else:
            key = c_name + "." + i_id

            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        If the class name is missing,
        print ** class name missing ** (ex: $ destroy)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex:$ destroy MyModel)
        If the id is missing,
        print ** instance id missing ** (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """

        c_name = self.parseline(line)[0]
        i_id = self.parseline(line)[1]

        if c_name == "" or c_name is None:
            print("** class name missing **")

        elif c_name not in my_classes:
            print("** class doesn't exist **")

        elif i_id == "" or i_id is None:
            print('** instance id missing **')

        else:
            key = c_name + "." + i_id

            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()

            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
