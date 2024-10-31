#Palabra más larga
#Escriba un programa que pida al usuario dos palabras, 
#y que indique cuál de ellas es la más larga y por cuántas letras lo es.
#
#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.
#Palabra 1: sol
#Palabra 2: paralelepipedo
#La palabra paralelepipedo tiene 11 letras mas que sol
#Palabra 1: plancha
#Palabra 2: lapices
#Las dos palabras tienen el mismo largo

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
        Welcome back Mr/Ms {name}, this is a program for calculate the length of 2 words and how to kwon
        which one have more letters \n
              """) 

    try :    
        
        wordOne = str(input("        Please enter the first word: "))
        wordTwo = str(input("        Please enter the second second: " ))

        nWordOne = len(wordOne)
        nWordTwo = len(wordTwo)
        
        if nWordOne > nWordTwo :
            words = nWordOne - nWordTwo
            print(f"        The word {wordOne} have {words} more letters than the word {wordTwo}")
        
        if nWordOne < nWordTwo :
            words =  nWordTwo - nWordOne 
            print(f"        The word {wordTwo} have {words} more letters than the word {wordOne}")

        if nWordOne == nWordTwo :
            print(f"        Both words have se same length")



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