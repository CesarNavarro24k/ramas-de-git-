import random 

numero = int(input("Cual crees que es el numero entre 1 y 10:"))

numero2 = random.randint(1,10)

if numero == numero2:
    print("Has adivinado el numero")
else:
    print(f"No has adivinado el numero, el numero era {numero2}")
