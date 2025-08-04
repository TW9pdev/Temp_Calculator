temp = 0
choix = 0
choix2 = 0
langue = 0

while langue not in [1, 2]:
    try:
        langue = int(input("Choose your language, enter 1 for english and 2 for french: "))
        if langue == 1:
            print("Welcome in to Temp_Calculator !")
        else:
            print("Bienvenue dans le Temp_Calculator !")
    except ValueError:
        print("Enter 1 for english or 2 for french / Entre 1 pour mettre en anglais et 2 pour mettre en français")

if langue == 2:
    while True:
        try:
            temp = int(input("Entre la température que tu souhaites convertir (seulement le chifre/nombre): "))
            break
        except ValueError:
            print("Veuillez Entrer un nombre")
            

    while choix not in [1, 2, 3]:
        try:
            choix = int(input("Entre 1 pour des degrès Celcius, 2 pour Fahrenheit et 3 pour les Kelvins: "))

            if choix == 1:
                print("Tu as choisis les degrès Celcius")
            elif choix == 2:
                print("Tu as choisis les degrès Fahrenheit")
            else:
                print("Tu as choisis les degrès Kelvins")
        except ValueError:
            print("Veuillez Entrer un nombre")
            
    while choix2 not in [1, 2, 3]:
        try:
            choix2 = int(input("En quoi veux-tu convertir ? Entre 1 pour des degrès Celcius, 2 pour Fahrenheit et 3 pour les Kelvins: "))

            if choix2 == 1:
                print("Tu as choisis les degrès Celcius")
            elif choix2 == 2:
                print("Tu as choisis les degrès Fahrenheit")
            else:
                print("Tu as choisis les degrès Kelvins")
        except ValueError:
            print("Veuillez Entrer un nombre")
            

    if choix == 1 and choix2 == 1:
        print(f"{temp}°C donne {temp}°C !")

    if choix == 1 and choix2 == 2:
        print(f"{temp}°C donne", (temp * 9 / 5) + 32, "°F !")
        
    if choix == 1 and choix2 == 3:
        print(f"{temp}°C donne", temp + 273.15,"K !")

    if choix == 2 and choix2 == 1:
        print(f"{temp}°F donne", (temp - 32) * 5 / 9,"°C !")

    if choix == 2 and choix2 == 2:
        print(f"{temp}°F donne {temp}°F !")
        
    if choix == 2 and choix2 == 3:
        print(f"{temp}°F donne", (temp - 32) / 1.8 + 273.15,"K !")
        
    if choix == 3 and choix2 == 1:
        print(f"{temp}K donne", temp - 273.15,"°C !")

    if choix == 3 and choix2 == 2:
        print(f"{temp}K donne", (temp - 273.15) * 9 / 5 + 32, "°F !")
        
    if choix == 3 and choix2 == 3:
        print(f"{temp}°K donne {temp}K !")
        
    print()

    print("Merci d'avoir utilisé 'Temp_Calculator' !")
    
if langue == 1:
    while True:
        try:
            temp = int(input("Enter the temperature you want to convert (only digit or number): "))
            break
        except ValueError:
            print("Please enter a number")
            

    while choix not in [1, 2, 3]:
        try:
            choix = int(input("Enter 1 for degrees Celsius, 2 for Fahrenheit and 3 for Kelvins: "))

            if choix == 1:
                print("You choose degrees Celcius")
            elif choix == 2:
                print("You choose degrees Fahrenheit")
            else:
                print("You choose degrees Kelvins")
        except ValueError:
            print("Please enter a number")
            
    while choix2 not in [1, 2, 3]:
        try:
            choix2 = int(input("What do you want to convert to? Enter 1 for degrees Celsius, 2 for Fahrenheit, and 3 for Kelvin: "))

            if choix2 == 1:
                print("You choose degrees Celcius")
            elif choix2 == 2:
                print("You choose degrees Fahrenheit")
            else:
                print("You choose degrees Kelvins")
        except ValueError:
            print("Please enter a number")
            

    if choix == 1 and choix2 == 1:
        print(f"{temp}°C equal {temp}°C !")

    if choix == 1 and choix2 == 2:
        print(f"{temp}°C equal", (temp * 9 / 5) + 32, "°F !")
        
    if choix == 1 and choix2 == 3:
        print(f"{temp}°C equal", temp + 273.15,"K !")

    if choix == 2 and choix2 == 1:
        print(f"{temp}°F equal", (temp - 32) * 5 / 9,"°C !")

    if choix == 2 and choix2 == 2:
        print(f"{temp}°F equal {temp}°F !")
        
    if choix == 2 and choix2 == 3:
        print(f"{temp}°F equal", (temp - 32) / 1.8 + 273.15,"K !")
        
    if choix == 3 and choix2 == 1:
        print(f"{temp}K equal", temp - 273.15,"°C !")

    if choix == 3 and choix2 == 2:
        print(f"{temp}K equal", (temp - 273.15) * 9 / 5 + 32, "°F !")
        
    if choix == 3 and choix2 == 3:
        print(f"{temp}°K equal {temp}K !")
        
    print()

    print("Thanks for use 'Temp_Calculator' !")

