#imports:
from models import *
from database import *



def function_x():
    pass

def function_y():
    pass

def function_z():
    pass

def function_else():
    pass



def main():

    while True:

        user_input = input("Veuillez saisir 1: New User, 2: Transfert : >> ")

        if user_input == "X":
            
            function_x()


        elif user_input == "Y":

            function_y()

        
        elif user_input == "Z":

            function_z()
        

        else:

            function_else()

if __name__ == "__main__":
    main()