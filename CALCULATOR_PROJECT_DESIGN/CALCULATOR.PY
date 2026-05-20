#SIMPLE CALCULATOR
#FUNCTIONS DEFINITION

#ADDITION FUNCTION
def addNumbers(Num1, Num2):
    Result = Num1 + Num2
    return Result

#SUBTRACTION FUNCTION
def subNumbers(Num1, Num2):
    Ans = Num1 - Num2
    return Ans

#MULTIPLICATION FUNCTION
def multNumbers(Num1, Num2):
    Product = Num1 * Num2
    return Product

#DIVISION FUNCTION
def divNumbers(Num1, Num2):
    if Num2 == 0:
        return -1
    else:
        return Num1 / Num2

#USER INPUTS
print("WELCOME TO CALCULATOR PROGRAM")
Number1 = float ( input("ENTER FIRST NUMBER: "))
Number2 = float ( input("ENTER SECOND NUMBER: "))
Operation = input ("SELECT WHICH OPERATION YOU WANT TO PERFOM \" +, -, x, / \": ")

#DECISION CONTROLS AND RELATIONAL CONTROLS
if Operation == "+":
    #FUNCTION CALL
   Res1 = addNumbers(Number1, Number2)
   print("YOU'RE SELECTED ADDITIONAL OPERATION\nSUM OF THIS TWO NUMBER IS:",Res1)

elif Operation == "-":
    #FUNCTION CALLING
    Res2 = subNumbers(Number1, Number2)
    print("YOU'RE SELECTED SUBTRACTION OPERATION\nDIFFERANCE OF TWO NUMBERS IS:",Res2)

elif Operation == "X":
    #FUNCTION CALLING
    Res3 = multNumbers(Number1, Number2)
    print("YOU'RE SELECTED MULTIPLICATION OPERATION\nPRODUCT OF TWO NUMBER IS:",Res3)

elif Operation == "/":
    #FUNCTION CALLING
    Res4 = divNumbers(Number1, Number2)
    if Res4 == -1:
        print("MATHEMATICAL ERROR CAN'T DIVIDE")

    else:
        print("YOU'RE SELECTED DIVISION OPERATION\nDIVISION OF TWO NUMBERS IS:",Res4)
else:
    print("OPERATION SYMBOL IS NOT RECOGNIZE")
