## Kapitel 7 ##

# moduler = fil som innehåller pythonkod, de kan innehålla funktioner, klasser och variabler
# importeras

# def greet(name):
#     return f"Hej {name}"

# def add(a, b):
#     return a + b

# PI = 3.14

## paket = samling av moduler

## Undantagshantering/Felhantering ##
# try & except

# result = 10 / 0
# print("Hej")
# All kod som kommer efter kommer inte köras

# finns sätt att fånga allmänna/generella fel och sätt för att fånga upp specifika fel
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Fel: Division med noll är inte tillåtet")
# else:
#     print(f"Resultat: {result}")
# finally: # körs alltid oavsett
#     print("Slut på try except")


# print("Hej")
# programmet körs vidare och kraschar inte

# för att ta reda på felet så testa att köra programmet

# kontrollera om en fil finns eller inte:
# try:
#     with open("example.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Fel: Filen finns inte!")
# else:
#     print(content)

    # man kan ha flera except om man får flera fel

## os-modulen ##
# ger oss olika inbyggda funktioner för att kunna hantera vårt operativsystem

# import os

# nuvarande katalog man arbetar i

# os.chdir('c:\\') # byter katalog

# os.mkdir('test_folder') # lägger till en fil
# os.rmdir('test_folder') # tar bort filen

# felhantering, finns filen?

# if os.path.exists("example.txt"):
#     print("Filen existerar")
#     os.remove('example.txt') # tar bort filen
# else:
#     print("Filen existerar inte")

# file_info = os.stat("bild.png") # kontrollera en fil, bild osv
# print(f"Filstorlek: {file_info.st_size}")

## Systemkommandon ##

# os.system('dir') # kontrollera alla filer och kataloger som finns i befintlig
# används endast i testmiljöer
# man kan skicka koder till andra för att luras eller ta bort saker hos andra

# filepath = os.path.join("math_script", "main.py") # lägga ihop en fil med katalog
# print(filepath)

# with open(filepath, "r") as file:
    #kod

# import os
# import platform # kontrollerar vilket os någon sitter på, och göra saker på sitt program

# if os.name == "nt":
#     print("Windows!")
#     os.system("dir")
# else:
#     print("Unix!")
#     os.system("ls")

# print(f"Plattform: {platform.system()}")

# from pathlib import Path # man kan skapa olika typr av paths i olika system