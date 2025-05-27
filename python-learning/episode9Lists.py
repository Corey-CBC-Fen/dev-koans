supplies = ["tent", "sleeping bags", "water", "rasberry pi",
"coffee", "knife", "ethernet cable", "flash drive",
"beard oil", "marshmallows",]


campSite = ["Crystal Lake", 404, 89,3, True]

supplies.extend(["toilet paper", "bidet"])

#supplies.clear()   #clear with blank paranthesis will bring up an empty list (u can have empty lists)

supplies.remove("tent") #can only do one at a time

#supplies.pop(0)
supplies.pop(0)

print(supplies)