print("By Nathan, Mathew, and Willbert")
print("1. Gol_IA                            9.  Gol_IB")
print("2. Gol_IIA                           10. Gol_IIB")
print("3. Gol_IIIB                          11. Gol_IIIA")
print("4. Gol_IVB                           12. Gol_IVA")
print("5. Gol_VB                            13. Gol_VA")
print("6. Gol_VIB                           14. Gol_VIA")
print("7. Gol_VIIB                          15. Gol_VIIA")
print("8. Gol_VIIIB                         16. Gol_VIIIA")
print("Please select what golongan do you want to explore:")
input1 = input()
input1_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]


M = ["Li","Na","K","Rb","Cs","Fr","Be","Mg","Ca","Sr","Ba","Ra","B","Al","Ga","In","Tl","Si","Ge","Sn","Pb","As","Sb","Bi","Te","Po",",At"]
Non_M = ["H","C","N","P","O","S","Se","F","Cl","Br","I","He","Ne","Ar","Kr","Xe","Rn"]
# Net, di line 1 dan 2 itu atom apaan?
# Metal dan Non-Metal?

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
