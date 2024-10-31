#Escriba un programa que pida dos números enteros y que calcule la división, 
#indicando si la división es exacta o no.
#
#Dividendo: 14
#Divisor: 5
#
#La división no es exacta.
#Cociente: 2
#Resto: 4
#Dividendo: 100
#Divisor: 10
#
#La división es exacta.
#Cociente: 10
#Resto: 0

import math


print(f""" 
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝                                                        
                                """) 
name = input("    Hello, please enter your full name:  ")

while True:

    print(f""" \n
        Welcome back Mr/Ms {name}, this is a program for calculate the divison of two numbers and kwon 
        if they have a remainder and a quotient\n
              """) 

    try :    
        
        numberOne = float(input("        Please enter the first number: "))
        numberTwo = float(input("        Please enter the second number: " ))

        
        
        if numberTwo == 0:
            print("        Division by zero ´0´ its not posible  ")

        quotient = numberOne // numberTwo  #cociente pero solo cn la parte entera
        remainder = numberOne % numberTwo  #resto
         
        if remainder != 0 :
           
            print("\n        The division is not exact")
            print(f"        Quotient: {round(quotient)}")
            print(f"        Remainder: {round(remainder)}")

        if remainder == 0:    
            print("\n        The division is exact")
            print(f"        Quotient: {round(quotient)}")
            print(f"        Remainder: {round(remainder)}")



        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        print("\n        Error: Please enter the correct data ")
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break