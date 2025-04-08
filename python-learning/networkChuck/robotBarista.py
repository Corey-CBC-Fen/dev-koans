#Network Chuck python learning 

#Robot barista

print("Hello welcome to Carbine C Coffee!!!\n")

name = input("What is your name?:\n")

if name == "RZA":
    print("GET THE FUCK OUT OF HERE YOU GINGER! NO MANGY HOUSE CATS ALLOWED!!")
    exit()
else:
    print("Hello " + name + ", thank you so much for coming in today! \n\n")

menu = "Black Coffee, Espresso, Latte, Americano"

print(name + ", What would you like from our menu today? \nHere's what we're serving: \n"
      + menu)

order = input() 

price = 8

amount = input("How many would you like?\n")


total = price * int(amount) #makes it an interger not a string so it can do math

print("Sounds good " + name + ", we'll have your " + amount +" "+ order + " ready for you in a moment!")

print("Thank you! Your total is: " + "$" + str(total))
