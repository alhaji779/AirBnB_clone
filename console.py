#!/usr/bin/python3
""" This is a command interpreter that sereves as a Frontend to the Airbnb backend """

import cmd

class HBNBCommand(cmd.Cmd):
    """ THis class helps us interacted with the AIrBNB backend project """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ function to quit the program
            Usage: quit
        """
        return True

    def do_EOF(self, line):
        """ function to handle EOF i.e. Control D """
        return True

    def emptyline(self):
        """ Do nothing when an empty line is entered """
        print()
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
