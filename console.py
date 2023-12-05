#!/usr/bin/python3
"""
Command interpreter
"""

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
