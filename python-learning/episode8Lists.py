supplies = ["tent", "sleeping bags", "water", "rasberry pi",
"coffee", "knife", "ethernet cable", "flash drive",
"beard oil", "marshmallows",]


campSite = ["Crystal Lake", 404, 89,3, True]  #we have a string, interger, float and boolean

#supplies.append("toilet paper") #append only does one extend  can do multiple
#supplies.append("bidet")

#supplies.extend(["toilet paper", "bidet"]) #these are called methods 

#supplies = supplies + ["toilet paper", "bidet"]  #this does same thing as the method above 

supplies.insert(0, "bidet")    #0 is the index (the order of our list (they always start at 0))

supplies.insert(-1, "toilet paper")
print(supplies)
