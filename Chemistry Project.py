M = ["Li","Na","K","Rb","Cs","Fr","Be","Mg","Ca","Sr","Ba","Ra","B","Al","Ga","In","Tl","Si","Ge","Sn","Pb","As","Sb","Bi","Te","Po",",At"]
Non_M = ["H","C","N","P","O","S","Se","F","Cl","Br","I","He","Ne","Ar","Kr","Xe","Rn"]

Col_IA = ["H","li","Na","K","Rb","Cs","Fr"]
Col_IIA = ["Be","Mg","Ca","Sr","Ba","Ra"]
Col_IIIB = ["B","Al","Ga","In","Tl"]
Col_IVB = ["C","Si","Ge","Sn","Pb"]
Col_VB = ["N","P","As","Sb","Bi"]
Col_VIB = ["O","S","Se","Te","Po"]
Col_VIIB = ["F","Cl","Br","I","At"]
Col_VIIIB = ["He","Ne","Ar","Kr","Xe","Rn"]

from time import sleep
print("Welcome to the limited periodic table bonding dictionary")
# sleep(2)
print("Insert 2 atoms from column IA-VIIA")
# sleep(2)
atom_1 = input("1st Atom = ")
atom_2 = input("2nd Atom = ")

if atom_1 in M and atom_2 in Non_M:
    print("This is an Ion Bond")
else:
    print("Invalid atom")