#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
#
#Ingrese numero: 51
#Ingrese numero: 24
#24 51
#A continuación, escriba otro programa que haga lo mismo con tres números:
#
#Ingrese numero: 8
#Ingrese numero: 1
#Ingrese numero: 4
#1 4 8
#Finalmente, escriba un tercer programa que ordene cuatro números:
#
#Ingrese numero: 7
#Ingrese numero: 0
#Ingrese numero: 6
#Ingrese numero: 1
#0 1 6 7
#Recuerde que su programa debe entregar la solución correcta para cualquier combinación de números,
#no sólo para los ejemplos mostrados aquí.
#
#Hay más de una manera de resolver cada ejercicio.

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
        Welcome back Mr/Ms {name}, this is a program for calculate order of a certain amount of numbers \n
              """) 

    try :    
        
        
        select = int(input("        Select the amount of numbers that you want to order (2 , 3 or 4 numbers) : "))
        if select == 2 :
            numberOne  =  float(input("        Enter your first number : "))
            numberTwo  =  float(input("        Enter your second number : "))
            
            array = [numberOne , numberTwo]
            array.sort()
            print("        The order of the numbers is : ",", " .join(map(str,array))) #para eliminar los corchetes de un array y separar los elementos del array con comas, ademas trasnforma los elemntos de array en un str


    
        if select == 3 :
            numberOne  =  float(input("        Enter your first number : "))
            numberTwo  =  float(input("        Enter your second number : "))
            numberThree = float(input("        Enter your thirdth : "))
            
            array = [numberOne , numberTwo, numberThree]
            array.sort()
            print("        The order of the numbers is : ",", " .join(map(str,array)))
        
        if select == 4 :
            numberOne  =  float(input("        Enter your first number : "))
            numberTwo  =  float(input("        Enter your second number : "))
            numberThree = float(input("        Enter your thirdth : "))
            numberFour = float(input("        Enter your fourth : "))

            array = [numberOne , numberTwo, numberThree , numberFour]
            array.sort()
            print("        The order of the numbers is : ",", " .join(map(str,array)))

        if select != 2 and select != 3 and select != 4 :    
            print("\n        Error: Please enter the correct data ")    
        
        
        
        
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