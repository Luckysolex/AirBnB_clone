#!/usr/bin/python3
"""This module defines a simple command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program at EOF"""
        print("")  # Print a newline before exiting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
