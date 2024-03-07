#!/usr/bin/python3
""" This is a command interpreter that sereves as a Frontend to the Airbnb backend """

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """ THis class helps us interacted with the AIrBNB backend project """

    prompt = "(hbnb) "
    class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

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

    def do_create(self, line):
        """ This function is called to create a new instance of a class
            Usage: create <className>
        """
        if len(line) == 0:
            print("** class name missing **")
            return

        if line not in self.class_list:
            print("** class doesn't exist **")
            return
        if line in self.class_list:
            new_obj = eval(line)()
            new_obj.save()
            print(new_obj.id)
            #except Exception:
            #print("** class doesn't exist **")

    def do_show(self, line):
        """ This function shows the content of a Class given its id
            Usage: show <className> <class_id>
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(arg) <= 1:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(arg[0], arg[1])
            obj_all = storage.all()
            #for k, v in obj_all.items():
            if key in obj_all.keys():
                print(str(obj_all[key]))
                return
            else:
                print("** no instance found **")
                return


    def do_destroy(self, line):
        """ This function deletes the content of a Class given its id
            Usage: destroy <className> <class_id>
        """
        all_obj = storage.all()
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(arg) <= 1:
            print("** instance id missing **")
            return
        else:
            #print(arg[0], arg[1])
            key = "{}.{}".format(arg[0],arg[1])
            if key not in all_obj.keys():
                print("** no instance found **")
                return
            if key in all_obj.keys():
                del all_obj[key]
                storage.save()

    def do_all(self, line):
        """ This function displays all instances available in storage
            Usage: all <className> or all 
        """
        args = line.split()
        if not line:
            print([str(val) for val in storage.all().values()])
            return
        if line not in self.class_list:
            print("** class doesn't exist **")
            return
        if line in self.class_list:
            obj1 = storage.all()
            for k, v in obj1.items():
                k2 = k.split(".")
                if k.split(".")[0] == line:
                    print(str(v))
            return


    def do_update(self, line):
        """ This function updates the content of an instance with a new value provided
            Usage: update <className> <class_id> <attribute name> "<attribute value>"
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(arg) <= 1:
            print("** instance id missing **")
            return
        if len(arg) <= 2:
            print("** attribute name missing **")
            return
        if len(arg) <= 3:
            print("** value missing **")
            return
        else:
            key = "{}.{}".format(arg[0],arg[1])
            obj_all = storage.all()
            if key in obj_all.keys():
                attr = arg[2]
                val = eval(arg[3])
                if attr in ['id', 'updated_at', 'crated_at']:
                    print("** sorry, you are not allowed to update that parameter **")
                    return
                setattr(obj_all[key], attr, val)
                storage.save()
            else:
                print("** no instance found **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
