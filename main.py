#Escriba un programa que simule una calculadora básica, este puede realizar 
# peración de suma, resta, multiplicación y división.
#
#El programa debe recibir como entrada 2 números reales y un operador,
#  que puede ser +, -, * o /.
#
#La salida del programa debe ser el resultado de la operación.
#
#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5
#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1
#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20
#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5
#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1


import math
from time import localtime


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
        Welcome back Mr/Ms {name}, this is a program for calculate your age:
              """) 

    try :    
        
        print("        Enter your Enter your birth date ")
        day   = int (input("        Day : "))
        month   = int (input("        Month : "))
        year   = int (input("        Year : "))


        

        t = localtime()
        
        aDay = t.tm_mday 
        aMon = t.tm_mon
        aYear = t.tm_year
        
        if day <= 31 and day >= 1 and month <= 12 and month >= 1 :

            actualDayAge = aDay - day
            actualMonAge = aMon - month
            actualYearAge = aYear - year
            print(f"\n        Your actual age is: {actualYearAge} years with {actualMonAge} month with {actualDayAge} days")
        
        else : 
            print("\n        Data time error, put again the correct data")

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