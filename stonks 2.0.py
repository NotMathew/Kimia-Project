from time import *

item_price = {}
def manage():
    manage = True
    while manage == True:
        new_item = input("add item to shop:")
        if new_item in item_price:
            print("the item is already on shelves")
            user_prompt = input("would you like to add to stock:")
            if user_prompt.lower() == "yes":
                user_prompt = input("how many would you like to add:")
                item_price[new_item] += int(user_prompt)
                print(item_price)
                user_prompt = input("would you like to continue? ")
                if user_prompt.lower() == "yes":
                    manage = True
                else:
                    manage = False
            elif user_prompt.lower() == "no":
                manage = True
            else:
                print("invalid")
        elif new_item not in item_price:
            print("item not found")
            user_prompt = input("enter amount to add to shelves:")
            item_price[new_item] = int(user_prompt)
            print(item_price)
            user_prompt = input("would you like to continue? ")
            if user_prompt.lower() == "yes":
                manage = True
            else:
                manage = False

def buy():
    cart = {}
    shopping = True
    while shopping == True:
        bought_item = input("add item to cart:")
        if bought_item in item_price:
            user_prompt = int(input("how many would you like to buy:"))
            if user_prompt <= item_price[bought_item]:
                item_price[bought_item] -= user_prompt
                cart[bought_item] = int(user_prompt)
                print("successfully bought!")
                for item in cart:
                    print(item + " = " + str(cart[item]))
                user_prompt = input("would you like to buy anything else?")
                if user_prompt.lower() == "yes":
                    shopping = True
                elif user_prompt.lower() == "no":
                    shopping = False
            else:
                print("sorry, the number of items you are willing to buy is not available/valid")

def set_password():
        setting = True
        counter = 0
        password = open("password", "r")
        while setting == True:
            if counter < 3:
                user_input = input("enter current password")
                if user_input in password:
                    password.close()
                    password = open("password", "w")
                    user_promt = input("enter new password")
                    password.write(user_promt)
                    setting = False
                elif user_input not in password:
                    user_promt = input("wrong password, enter code:")
                    if user_promt == code:
                        password.close()
                        password = open("password", "w")
                        user_promt = input("enter new password")
                        password.write(user_promt)
                        setting = False
                    else:
                        print("incorrect")
                        setting = True
                        counter = + 1
            elif counter >= 3:
                print("sorry, you have reached the limit of tries")
                setting = False
        password.close()

def set_code():
    password = open("password","r")
    code = open("backup_code","r")
    setting = True
    while setting == True:
        user_promt = input("enter current password")
        if user_promt in password:
            user_promt = input("enter current code:")
            if user_promt in code:
                user_promt = input("enter new code:")
                code.close()
                code = open("backup_code", "w")
                code.write(user_promt)
                setting = False
            else:
                print("incorrect code")
        else:
            print("incorrect password")

// Mathew was here
// test

/**
Net
**/

password = open("password","r")
code = open("backup_code","r")
print(">manage")
print(">buy")
print(">security")
user_promt = input("")
if user_promt.lower() == 'manage':
    password_try = 0
    while password_try < 3:
        user_promt = input("enter password:")
        if user_promt in password:
            manage()
            break
        elif user_promt != password:
            user_promt = input("forgot password?")
            if user_promt.lower() == "yes":
                set_password()
            if user_promt.lower() == "no":
                password_try += 1
elif user_promt.lower() == "buy":
    buy()
elif user_promt.lower() == "security":
    print(">change password")
    print(">change code")

password.close()
code.close()
