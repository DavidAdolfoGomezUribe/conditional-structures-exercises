#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:
#
# 	edad < 45	edad ≥ 45
#IMC < 22.0	bajo	medio
#IMC ≥ 22.0	medio	alto
#El índice de masa corporal es el cuociente entre el peso del individuo en kilos 
# y el cuadrado de su estatura en metros.
#
#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

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
        Welcome back Mr/Ms {name}, this is a program for calculate the IMC risk.
              """) 

    try :    


        age = float(input("        Enter your age: "))         
        height = float(input("        Height (in Meters): "))
        mass = float(input("        Mass (in Kg) : "))
        
        tIMC =  mass / math.pow(height,2)

        if age >= 1 and height >= 1 and mass >= 1 :
            if age < 45:
                if tIMC < 22:
                    print(f"        For your IMC {round(tIMC,2)} you have Low risk chance")
                else:
                    print(f"        For your IMC {round(tIMC,2)} you have Medium risk chance")
            
            else:
                if tIMC < 22:
                    print(f"        For your IMC {round(tIMC,2)} you have Medium risk chance")
                else:
                    print(f"        For your IMC {round(tIMC,2)} you have High risk chance")
            



        else:
            print("\n        Only positive numbers")
        
      #  if not (aSide + bSide > cSide and aSide + cSide > bSide and bSide + cSide > aSide):
       #     raise ValueError("") #posiblemente lo use mas tarde
       
         
        
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        print("\n        Error: Enter the correct data ")
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break