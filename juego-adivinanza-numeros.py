
import random

def juego_adivinanza():
    # generar un numero del 1 al 100
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    
    print("Bienvenido")
    print("adivina el numero")
    print(" intenta adivinar")
    
    while not adivinado:
        adivinanza = input("introdusca un nuemro del 1 al 100: ") 
        
        if adivinanza.isdigit(): # si es nuemro
            adivinanza = int(adivinanza) # casteando a int
            intentos += 1
            
            if adivinanza < numero_secreto:
                print(f"el nuemro secreto es mayor al:  {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"el nuemro secreto es mayor al:  {adivinanza}")
            else:
                print(f"Ganaste en {intentos} intentos")
                adivinado = True
        else:
            print("ingrese numero valido")    
                   
juego_adivinanza()

print("Cerramos")    
            