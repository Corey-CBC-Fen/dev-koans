#Network Chuck python learning 

#Robot barista

print("Hello welcome to Carbine C Coffee!!!\n")

name = input("What is your name?:\n")

if name == "RZA" or name == "Scooter" or name == "Loki":
    evil_status = input("Are you evil?\n")
    goodDeeds = int(input ("How many good deeds have you done today? \n"))
    if evil_status =="Yes" and goodDeeds < 4  :
      print("GET THE FUCK OUT OF HERE " + name +  "! NO MANGY HOUSE CATS ALLOWED!!")
      exit()
    else:
       print("\nHmmm...\nI guess you can order, I got my eyes on you\n")
else:
    print("Hello " + name + ", thank you so much for coming in today! \n\n")

menu = "Black Coffee, Espresso, Latte, Americano, Frappuccino, London Fog"

print(name + ", What would you like from our menu today? \nHere's what we're serving: \n"
      + menu)

order = input() 

price = 8

amount = input("How many would you like?\n")

#Fraps cost more if statement for that
if order == "Frappuccino":
   price = 13
elif order == "Black Coffee":
   price = 4
elif order == "Espresso":
   price = 5
elif order == "Latte":
   price = 9 
elif order == "Americano":
   price = 8
elif order == "London Fog":   # Poop pee fecal poopie 
   price = 42
else:
   print("Sorry, We dont have that here")
   price = 0
   exit()

print(price)

total = price * int(amount) #makes it an interger not a string so it can do math

print("Sounds good " + name + ", we'll have your " + amount +" "+ order + " ready for you in a moment!")

print("Thank you! Your total is: " + "$" + str(total))
