#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.
#
#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
#
#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.
#Ingrese a: 3.9
#Ingrese b: 6.0
#Ingrese c: 1.2
#No es un triangulo valido.
#Ingrese a: 1.9
#Ingrese b: 2
#Ingrese c: 2
#El triangulo es isoceles.
#Ingrese a: 3.0
#Ingrese b: 5.0
#Ingrese c: 4.0
#El triangulo es escaleno.

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
        Welcome back Mr/Ms {name}, this is a program for calculate the triangle type based in his sides.
              """) 

    try :    
                
        aSide = float(input("        Side A : "))
        bSide = float(input("        Side B : "))
        cSide = float(input("        Side C : "))

        if not (aSide + bSide > cSide and aSide + cSide > bSide and bSide + cSide > aSide):
            raise ValueError("") #posiblemente lo use mas tarde
         
        if aSide == bSide and bSide == cSide :
            print("        The triangle is equilateral")

        if aSide == bSide  or aSide == cSide or cSide == bSide :
            print("        The triangle is isosceles")    
        
        else:
            print("        The triangle is scalene")    

        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        print("\n        Error: Its not a valid triangle ")
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break