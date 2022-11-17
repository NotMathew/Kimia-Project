# A Project by Nathan, Mathew, Wilbert
# Imports
from time import sleep
import random

def slow_typing(sentence):
    for x in sentence:
        print(x, end="")
        sleep(.25)


# Whats up nathon
# Element Dictionary
M = ["Li","Na","K","Rb","Cs","Fr","Be","Mg","Ca","Sr","Ba","Ra","B","Al","Ga","In","Tl","Uut","Si","Ge","Sn","Pb","As","Sb","Bi","Te","Po",",At","Cu","Ag","Au","Zn","Cd"
     "Hg","Cn","Sc","Y","La","Ac","Ti","Zr","Hf","Rf","V","Nb","Ta","Db","Cr","Mo","W","Sg","Mn","Tc","Re","Bh","Fe","Ru","Os","Hs","Co","Rh","Ir","Mt","Ni","Pd","Pt","Ds"]
Non_M = ["H","C","N","P","O","S","Se","F","Cl","Br","I","He","Ne","Ar","Kr","Xe","Rn"]
electronegitivity = {"H":"2.1","Li":"1.0","Be":'1.5',"B":'2.0',"C":'2.5',"N": '3.0',"O":'3.5',"F":'4.0',"Na":'0.9',"Mg":'1.2',"Al":'1.5',
                     "Si":'1.8',"P":'2.1', "S":'2.5', "Cl":'3.0',"K":'0.8',"Ca":'1.0',"Sc":'1.3',"Ti":'1.5',"V":'1.6',"Cr":'1.6',"Mn":'1.5',"Fe":'1.8',
                     "Co":'1.8',"Ni":'1.8',"Cu":'1.9',"Zn":'1.6',"Ga":'1.6',"Ge":'1.8',"As":'2.0',"Se":'2.4',"Br":'2.8',"Kr":'3.0',
                     "Rb":'0.8',"Sr":'1.0',"Y":'1.2',"Zr":'1.4',"Nb":'1.6',"Mo":'1.8',"Tc":'1.9',"Ru":'2.2',"Rh":'2.2',
                     "Pd":'2.2',"Ag":'1.9',"Cd":'1.7',"In":'1.7',"Sn":'1.8',"Sb":'1.9',"Te":'2.1',"I":'2.5',"Xe":'2.6',
                     "Cs":'0.7',"Ba":'0.9',"La":'1.1',"Hf":'1.3',"Ta":'1.5',"W":'1.7',"Re":'1.9',"Os":'2.2',"Ir":'2.2',
                     "Pt":'2.2',"Au":'2.4',"Hg":'1.9',"Tl":'1.8',"Pb":'1.8',
                     "Bi":'1.9',"Po":'2.0',"At":'2.2',"Rn":'2.4',"Fr":'0.7',"Ra":'0.7',"Ac":'1.1'}
# Electronegativity is in buku paket kimia page 73
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
Col_IB = ["Cu","Ag","Au"]
Col_IIB = ["Zn","Cd","Hg","Cn"]
Col_IIIB = ["Sc","Y","La","Ac"]
Col_IVB = ["Ti","Zr","Hf","Rf"]
Col_VB = ["V","Nb","Ta","Db"]
Col_VIB = ["Cr","Mo","W","Sg"]
Col_VIIB = ["Mn","Tc","Re","Bh"]
Col_VIIIB8 = ["Fe","Ru","Os","Hs"]
Col_VIIIB9 = ["Co","Rh","Ir"]
Col_VIIIB10 = ["Ni","Pd","Pt"]

running = True
print("A Project By Nathan, Mathew, Wilbert")
sleep(1)
print("Hello and welcome to the simple element Dictionary or Simulation")
sleep(1)
while running == True:
    print("Dictionary or Simulation?")
    user_input = input("").lower()
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
            elif user_input == "home":
                break

    elif user_input == "simulation":
        simulation_running = True
        print("Welcome to the limited periodic table bonding simulation")
        while simulation_running == True:
            # Simulation
            sleep(1)
            print("Insert 2 atoms from column IA - VIIIA or IB - VIIIB10")
            sleep(1)
            atom_1 = input("1st Atom = ")
            atom_2 = input("2nd Atom = ")
            electro_atom_1 = float(electronegitivity[atom_1])
            electro_atom_2 = float(electronegitivity[atom_2])
            if atom_1 in M and atom_2 in Non_M and (electro_atom_1 - electro_atom_2 >= 1.7 or electro_atom_2 - electro_atom_1 >= 1.7) or atom_1 in Non_M and atom_2 in M and (electro_atom_1 - electro_atom_2 >= 1.7 or electro_atom_2 - electro_atom_1 >= 1.7):
                print("This is an Ion Bond")
                sleep(1)
                print("It occurs between a Metalic atom and a Non Metalic atom")
                sleep(1)
                print("You typed " + atom_1 + " and " + atom_2)
                sleep(1)
                print("This bond involves giving and taking between the electrons of those atoms")
                sleep(1)
                print("The difference in electronegativity between the two atoms are more or equal to 1.7")
                sleep(1)
                print(atom_1 +" = " + electronegitivity[atom_1] + ", " + atom_2 + " = " + electronegitivity[atom_2])
            elif atom_1 in Non_M and atom_2 in Non_M and (electro_atom_1 - electro_atom_2 < 1.7 or electro_atom_2 - electro_atom_1 < 1.7):
                print("This is a Covalent Bond")
                sleep(1)
                print("It occurs between two Non Metalic atoms")
                sleep(1)
                print("You typed " + atom_1 + " and " + atom_2)
                sleep(1)
                print("This bond involves the sharing of electrons between the atoms")
                sleep(1)
                print("The difference in electronegativity between the two atoms are less than 1.7")
                sleep(1)
                print(atom_1 +" = " + electronegitivity[atom_1] + ", " + atom_2 + " = " + electronegitivity[atom_2])
            elif atom_1 in M and atom_2 in M:
                print("This is a Metalic Bond")
                sleep(1)
                print("It occurs between two Metalic atoms")
                sleep(1)
                print("You typed " + atom_1 + " and " + atom_2)
                sleep(1)
                print("This bond involves the sharing of electrons between many metalic atoms")
                sleep(1)
                print("The metal is held together by strong forces of attraction between delocalized electrons and positive ions")
            else:
                 print("Invalid atom or input")

    elif user_input == "exit":
        # exiting the project
        print("Thank you for using this limited dictionary and simulation")
        sleep(1)
        print("We hope you enjoyed our project")
        sleep(1)
        slow_typing("~Nathan, Mathew and Wilbert")
        exit()

