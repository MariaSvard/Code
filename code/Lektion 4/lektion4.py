#if-satser:

# x = 10
# if x > 5:
#     print("x is greater than 5")

# x = 10 
# if x > 15: #Ingenting skrivs ut
#     print("x is greater than 5")

# elif-sats (else if):

# if condition1: # om den är true körs den

# elif: condition2: # om den är false körs den

# x = 10
# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print("x is greater than 5")

# else sats:

# x = 3
# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than 5")


#inbedded if-satser, inbäddade, nestad:

# x = 20
# if x > 10:
#     print("Above ten, ")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")

# and, or och not:

# x = 7
# y = 10
# if x > 5 and y < 15:
#     print("Both conditions are true")


# x = 7
# y = 20
# if x > 5 and y < 15:  # båda behöver vara true för att koden evalueras
#     print("Both conditions are true")

# x = 7
# y = 9
# if x > 5 or y < 15:
#     print("Both conditions are true")

# definera ett antal funktioner, short circut avaluation, conditional check
# kollar om något av dem är sant eller falskt beroende på vad man gör

# def check_a():
#     print("Kontrollerar a")
#     return False
# def check_b():
#     print("Kontrollerar b")
#     return True
# if check_a() and check_b():
#     print("Båda är sanna")
# else:
#     print("Minst en är falsk")

# results = värde_sant if villkor else värde_falskt  # går att skriva på en rad men undvik det

# x = 5
# parity = "even" if x % 2 == 0 else "odd"
# print(f"Number är {parity}")  # Inte jättebra kod att skriva då det är svårt att förstå när man läser
# det är inte lätt att se vad som kommer hända med koden eller varför

# jämföra flera värden samtidigt i ett villkor
# a = b = c = 10

# if a == b == c:  # lika stort som ==
#     print("Alla är lika")

# pass, uttalande, skriver inte ut något:

# x = 10
# if x > 0:
#     print("x is positive")
# else:
#     pass

# x = -0
# if x > 0:
#     print("x is positive")
# else:
#     pass

# Errorhandling, felhantering, svårt att hantera annars:

# number = input("Type a number")

# if number.isdigit():
#     number = int(number) # heltal
#     print(f"You typed a number {number}")
# else:
#     print("That's not a number")

# kombinera olika i samma uttryck:

# x = 5
# y = 10
# z = 15

# if (x < y and y < z) or x == z: # Inte lättläslig kod, undvik
#     print("True")

# funktioner och if-satser:

# def max_value(a, b):
#     if a > b:
#         return a
#     else:
#         return b
    
# biggest = max_value(10, 20)
# print(f"The biggest value is {biggest}")

# def max_value(a, b): # def när man skriver en funktion
#     if a > b:
#         return a
#     else:
#         return b
    
# biggest = max_value(15, 1)
# print(f"The biggest value is {biggest}")

# loopar

# for variabel in iterable: # Variabel kan vara vadsomhelst, men det måste vara läsbart
#     print(variabel)

# fruits = ["apple", "banana", "cherry"] # variabel som heter vad som helst
# for fruit in fruits: # för varje frukt så printar den
#     print(fruit)

# frukter = ("äpple", "banan", "körsbär") # variabel som heter vad som helst
# for frukt in frukter: # för varje frukt så printar den
#     print(frukt) # tuple

# tuple unpacking = få ut ett värde ur en variabel, tilldela en variabel till tuple

# person = ("Alice", 30, "Stockholm")
# name, age, city = person
# print(name)
# print(age)
# print(city)

# people = [("Alice", 30, "Stockholm"), ("Bob", 25, "Göteborg"),("Charlie", 35, "Malmö")]
# for name, age, city in people:
#     print(f"Namn: {name}, Ålder: {age}, stad: {city}")

# person = {"name": "Alice", "age": 30, "city": "Stockholm"} # dictionary 
# for key, value in person.items():
#     print(f"{key}: {value}")

# person = {"name": "Alice", "age": 30, "city": "Stockholm"} # dictionary 
# for key, value in person.items():
#     print(f"{key}:")

# text = "Hello" # varje bokstav är ett element
# for bokstav in text:
#     print(bokstav)

# frukter = {"äpple", "banan", "körsbär"}
# for frukt in frukter:
#     print(frukt)

# for siffra in range (5):
#     print(siffra)

# for siffra in range(2, 10, 2):
#     print(siffra)

# for siffra in range(3):
#     for nummer in range(2):
#         print(f"siffra: {siffra}, nummer: {nummer}")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0: # delbart med 2 och lika med 0
#         continue
#     print(i)

# while condition: True

# x = 0
# while x < 5:
#     print(x)
#     x += 1

# while True: # ctrl c för att avbryta
#     print("This is running forever")
#     break