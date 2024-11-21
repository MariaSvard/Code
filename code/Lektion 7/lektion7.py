# import pyfiglet
# from colorama import init, Fore, Back, Style

# ascii_art = pyfiglet.figlet_format("Hello World")
# print(ascii_art)

# init()

# print(Fore.RED + "Den här texten är röd")
# print(Fore.GREEN + "Den här texten är grön")

# print(Back.RED + "Röd bakgrund" + Style.RESET_ALL)

# print(Fore.RED + "Warning: Error")

## Input validering ##

# user_input = input("Skriv något: ")
# print(user_input)

# while True:
#     user_input = input("Ange ett nummer: ")
#     if user_input.isdigit():
#         user_number = int(user_input)
#         print(f"Du angav: {user_number}")
#         break
#     else:
#         print("Ogiltig input")

## try except ##

# try:
#     user_input = input("Ange ett nummer: ")
#     user_number = int(user_input)
#     print(f"Du angav: {user_number}")
# except ValueError:
#     print("Ogiltig input")

## validera input mot en lista ##

# valid_options = ["ja", "nej", "kanske"]
# user_input = input("Vill du sova?:").lower()

# if user_input in valid_options:
#     print(f"Du valde {user_input}")
# else:
#     print("Jag förstår inte, försök igen")

## OOP ##

# class Car: #klassen ska ha stor bokstav
#     wheels = 4 # klassattribut, ska vara gemensamma för alla
#     def __init__(self, make, model, year): # kconstuctor
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def description(self):
#         return f"{self.year}, {self.make}, {self.model} "

# car1 = Car("Volvo", "240", 1985)
# car2 = Car("Honda", "Civic", 2017)

# print(car1.make)
# print(car1.model)
# print(car1.year)

# print(car2.make)
# print(car2.model)
# print(car2.year)

# print(car1.wheels)
# print(car2.wheels)

# class Car: #klassen ska ha stor bokstav
#     wheels = 4 # klassattribut, ska vara gemensamma för alla

#     def __init__(self, make, model, year): # kconstuctor
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def description(self):
#         return f"{self.year}, {self.make}, {self.model} "
    
# car1 = Car("Volvo", "240", 1985)
# print(car1.description())

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass # gör ingenting just nu

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"
    
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.speak())
# print(cat.speak())

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass # gör ingenting just nu

# class Dog(Animal):
#     def __init__(self, name, breed, color):
#         super().__init__(name) # används för att inte behöva upprepa, ersätter tidigare
#         self.breed = breed
#         self.color = color

#     def speak(self):
#         return f"{self.name} says Woof!"

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"My name is: {self.name}, I am {self.age} old"
    
# person1 = Person("Bobbo", 37)
# print(person1)

# class Person:
#     def __init__(self, name, age):
#           self.name = name
#           self.age = age

#     def __repr__(self):
#         return f"My name is: {self.name}, I am {self.age} old"
    
# person1 = Person("Bobbo", 37)
# print(person1)

