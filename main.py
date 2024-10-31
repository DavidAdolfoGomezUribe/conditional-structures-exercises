#Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido 
#exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente,
#la diferencia es de más o menos un cuarto de día.
#Para evitar que las estaciones se desfasen con el calendario, el calendario juliano
#introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados bisiestos),
#para tomar en consideración los cuatro cuartos de día acumulados.
#
#Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente 3/400 de día.
#
#Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario,
#en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400.
#
#Escriba un programa que indique si un año es bisiesto o no,
#teniendo en cuenta cuál era el calendario vigente en ese año:
#
#Ingrese un anno: 1988
#1988 es bisiesto
#Ingrese un anno: 2011
#2011 no es bisiesto
#Ingrese un anno: 1700
#1700 no es bisiesto
#Ingrese un anno: 1500
#1500 es bisiesto
#Ingrese un anno: 2400
#2400 es bisiesto

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
        Welcome back Mr/Ms {name}, this is a program for calculate if the year is leap year  or not
        also, the program considerate the following data:
            * Before the year 1582  the leap years are all years that can be divisible by 4
            * After the year 1582:
                - Leap years are divisible by 4.
                - If divisible by 100, they must also be divisible by 400 to be leap years.\n
              """) 

    try :    
        
        aYear = int(input("        Please enter the number: "))

        if aYear >= 1582 :
            if (aYear % 4 == 0 and (aYear % 100 != 0 or aYear % 400 == 0) ):
                print ("        It´s a leap year")
            
            else :
                print ("        It is not a leap year")


        if aYear < 1582 :     
            if aYear % 4 == 0 :
                print ("        It´s a leap year")
            
            else :
                print ("        It is not a leap year")




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