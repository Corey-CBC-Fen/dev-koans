print("Hello welcome to Carbine C Merch Table!!!\n")

name = input("What is your name?:\n")

print("Hello " + name + ", thank you so much for coming in today! \n\n")

menu = "CDs, Posters, T-shirts, Bundle Deal!"

print(name + ", What would you like today? \nHere's what we got: \n"
      + menu)

order = input() 

price = 6

amount = input("How many would you like?\n")

#Not everything costs $6 but posters are 
if order == "CDs":
   price = 12
elif order == "T-shirts":
   price = 20
elif order == "Bundle Deal!":
   price = 35
elif order == "Posters":
   price = 6
else:
   print("Sorry, We dont have that here")
   price = 0
   exit()

print(price)

total = price * int(amount) #makes it an interger not a string so it can do math

print("Sounds good " + name + ", we'll have your " + amount +" "+ order + " ready for you in a moment!")

print("Thank you! Your total is: " + "$" + str(total))