#!/usr/bin/python3
"""
Command interpreter
"""

import cmd
import models
from models.base_model import BaseModel
from datetime import datetime
import re
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

my_classes = {"BaseModel": BaseModel, "User": User, "State":
              State, "City": City, "Amenity": Amenity, "Place":
              Place, "Review": Review}


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
        If the class name is missing,
        print ** class name missing ** (ex: $ show)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ show MyModel)
        If the id is missing,
        print ** instance id missing ** (ex: $ show BaseModel)
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

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ all MyModel)
        """
        if line == "" or line is None:
            new_list = [str(obj) for key, obj in models.storage.all().items()]
            print(new_list)

        else:
            c_name = self.parseline(line)[0]

            if c_name not in my_classes:
                print("** class doesn't exist **")
            else:
                new_list = [str(value) for key, value in models.storage.all
                            ().items() if type(value).__name__ == c_name]
                print(new_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type
        If the class name is missing,
        print ** class name missing ** (ex: $ update)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ update MyModel)
        If the id is missing,
        print ** instance id missing ** (ex: $ update BaseModel)
        If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ update BaseModel 121212)
        If the attribute name is missing,
        print ** attribute name missing ** (ex: $ update BaseModel existing-id)
        If the value for the attribute name doesn’t exist,print
        ** value missing ** (ex: $ update BaseModel existing-id first_name)
        All other arguments should not be used (Ex: $ update BaseModel
        1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update
        BaseModel 1234-1234-1234 email "aibnb@mail.com")
        id, created_at and updated_at cant’ be updated.
        You can assume they won’t be passed in the update command
        Only “simple” arguments can be updated: string, integer and float.
        You can assume nobody will try to update list of ids or datetime
        """

        args = shlex.split(line)
        num_of_args = len(args)
        if num_of_args == 0:
            print('** class name missing **')
        elif args[0] not in my_classes:
            print("** class doesn't exist **")
        elif num_of_args == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            instance = models.storage.all().get(key)
            if instance is None:
                print('** no instance found **')
            elif num_of_args == 2:
                print('** attribute name missing **')
            elif num_of_args == 3:
                print('** value missing **')
            else:
                if args[3].isdigit():
                    args[3] = int(args[3])
                elif args[3].replace('.', '', 1).isdigit():
                    args[3] = float(args[3])

                setattr(instance, args[2], args[3])
                setattr(instance, 'updated_at', datetime.now())
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
