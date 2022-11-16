# A Project by Nathan, Mathew, Wilbert
# Imports
from time import sleep
import random

#Element Dictionary
M = ["Li","Na","K","Rb","Cs","Fr","Be","Mg","Ca","Sr","Ba","Ra","B","Al","Ga","In","Tl","Si","Ge","Sn","Pb","As","Sb","Bi","Te","Po",",At","Cu","Ag","Au","Uuu","Zn","Cd"
     "Hg","Uub","Sc","Y","La","Ac","Ti","Zr","Hf","Rf","V","Nb","Ta","Db","Cr","Mo","W","Sg","Mn","Tc","Re","Bh","Fe","Ru","Os","Hs","Co","Rh","Ir","Mt","Ni","Pd","Pt","Ds"]
Non_M = ["H","C","N","P","O","S","Se","F","Cl","Br","I","He","Ne","Ar","Kr","Xe","Rn"]
# M = Metal
# Non_M = Non-Metal
#Col = Column
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
print("Hello and welcome to the simple element simulation and dictionary")
sleep(1)
while running == True:
    user_input = input("Dictionary or Simulation?").lower()
    if user_input == "dictionary":
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
        print("Please type the number to start exploring the world of chemistry")
        user_input = input()
        if user_input == ("1"):
            print(Col_IA)
        elif user_input == ("2"):
            print(Col_IIA)
        elif user_input == ("3"):
            print(Col_IIIA)








#Correct it if it's wrong - Wilbert

M = ["Li","Na","K","Rb","Cs","Fr","Be","Mg","Ca","Sr","Ba","Ra","B","Al","Ga","In","Tl","Si","Ge","Sn","Pb","As","Sb","Bi","Te","Po",",At","Cu","Ag","Au","Uuu","Zn","Cd"
     "Hg","Uub","Sc","Y","La","Ac","Ti","Zr","Hf","Rf","V","Nb","Ta","Db","Cr","Mo","W","Sg","Mn","Tc","Re","Bh","Fe","Ru","Os","Hs","Co","Rh","Ir","Mt","Ni","Pd","Pt","Ds"]
Non_M = ["H","C","N","P","O","S","Se","F","Cl","Br","I","He","Ne","Ar","Kr","Xe","Rn"]
# M = Metal
# Non_M = Non-Metal
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

#print("Welcome to the limited periodic table bonding dictionary")
# sleep(2)
#print("Insert 2 atoms from column IA-VIIIB10")
# sleep(2)
#atom_1 = input("1st Atom = ")
#atom_2 = input("2nd Atom = ")

#if atom_1 in M and atom_2 in Non_M:
#    print("This is an Ion Bond")
#else:
#    print("Invalid atom")
