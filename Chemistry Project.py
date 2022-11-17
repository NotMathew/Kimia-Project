# A Project by Nathan, Mathew, Wilbert
# Imports
from time import sleep
import random

# Element Dictionary
M = ["Li","Na","K","Rb","Cs","Fr","Be","Mg","Ca","Sr","Ba","Ra","B","Al","Ga","In","Tl","Si","Ge","Sn","Pb","As","Sb","Bi","Te","Po",",At","Cu","Ag","Au","Uuu","Zn","Cd"
     "Hg","Uub","Sc","Y","La","Ac","Ti","Zr","Hf","Rf","V","Nb","Ta","Db","Cr","Mo","W","Sg","Mn","Tc","Re","Bh","Fe","Ru","Os","Hs","Co","Rh","Ir","Mt","Ni","Pd","Pt","Ds"]
Non_M = ["H","C","N","P","O","S","Se","F","Cl","Br","I","He","Ne","Ar","Kr","Xe","Rn"]
# M = Metal
# Non_M = Non-Metal
# Col = Column
Col_IA = ["H","li","Na","K","Rb","Cs","Fr"]
Col_IIA = ["Be","Mg","Ca","Sr","Ba","Ra"]
Col_IIIA = ["B","Al","Ga","In","Tl"]
Col_IVA = ["C","Si","Ge","Sn","Pb"]
Col_VA = ["N","P","As","Sb","Bi"]
Col_VIA = ["O","S","Se","Te","Po"]
Col_VIIA = ["F","Cl","Br","I","At"]
Col_VIIIA = ["He","Ne","Ar","Kr","Xe","Rn"]
Col_IB = ["Cu","Ag","Au","Uuu"]
Col_IIB = ["Zn","Cd","Hg","Uub"]
Col_IIIB = ["Sc","Y","La","Ac"]
Col_IVB = ["Ti","Zr","Hf","Rf"]
Col_VB = ["V","Nb","Ta","Db"]
Col_VIB = ["Cr","Mo","W","Sg"]
Col_VIIB = ["Mn","Tc","Re","Bh"]
Col_VIIIB8 = ["Fe","Ru","Os","Hs"]
Col_VIIIB9 = ["Co","Rh","Ir","Mt"]
Col_VIIIB10 = ["Ni","Pd","Pt","Ds"]

running = True
print("A Project By Nathan, Mathew, Wilbert")
sleep(1)
print("Hello and welcome to the simple element Dictionary or Simulation")
sleep(1)
while running == True:
    user_input = input("Dictionary or Simulation?").lower()
    if user_input == "dictionary":
        dictionary_running = True

        # Dictionary
        # Write Col instead of Gol, we want it in English
        print("1. Col_IA                            9.  Col_IB")
        print("2. Col_IIA                           10. Col_IIB")
        print("3. Col_IIIA                          11. Col_IIIB")
        print("4. Col_IVA                           12. Col_IVB")
        print("5. Col_VA                            13. Col_VB")
        print("6. Col_VIA                           14. Col_VIB")
        print("7. Col_VIIA                          15. Col_VIIB")
        print("8. Col_VIIIA                         16. Col_VIIIB8")
        print("                                     17. Col_VIIIB9")
        print("                                     18. Col_VIIIB10")
        while dictionary_running == True:
            print("Type a number to explore the dictionary of element columns")
            user_input = input()
            if user_input == ("1"):
                print(Col_IA)
            elif user_input == ("2"):
                print(Col_IIA)
            elif user_input == ("3"):
                print(Col_IIIA)
            elif user_input == ("4"):
                print(Col_VIA)
            elif user_input == ("5"):
                print(Col_VA)
            elif user_input == ("6"):
                print(Col_VIA)
            elif user_input == ("7"):
                print(Col_VIIA)
            elif user_input == ("8"):
                print(Col_VIIIA)
            elif user_input == ("9"):
                print(Col_IB)
            elif user_input == ("10"):
                print(Col_IIB)
            elif user_input == ("11"):
                print(Col_IIIB)
            elif user_input == ("12"):
                print(Col_IVB)
            elif user_input == ("13"):
                print(Col_VB)
            elif user_input == ("14"):
                print(Col_VIB)
            elif user_input == ("15"):
                print(Col_VIIB)
            elif user_input == ("16"):
                print(Col_VIIIB8)
            elif user_input == ("17"):
                print(Col_VIIIB9)
            elif user_input == ("18"):
                print(Col_VIIIB10)

    elif user_input == "simulation":
        simulation_running = True
        while simulation_running == True:

            # Simulation
            print("Welcome to the limited periodic table bonding simulation")
            sleep(1)
            print("Insert 2 atoms from column IA - VIIIA or IB - VIIIB10")
            sleep(1)
            atom_1 = input("1st Atom = ")
            atom_2 = input("2nd Atom = ")
            if atom_1 in M and atom_2 in Non_M or atom_1 in Non_M and atom_2 in M:
                print("This is an Ion Bond")
                sleep(1)
                print("Why you may ask?")
            elif atom_1 in Non_M and atom_2 in Non_M:
                print("This is a Covalent Bond")
            elif atom_1 in M and atom_2 in M:
                print("This is a Metalic Bond")
            else:
                 print("Invalid atom or input")
