domSelector = "li > div > href"
items = domSelector.split('>')

for i in range (len(items)):
    items[i] = items[i].replace(" ","")

print(items[0])

previousItem = "doc"
for i in range (len(items)):
    print("Element e"+ str(i) + " = " + previousItem + ".queryAll(\"" + items[i] + "\")")
    previousItem = "e" + str(i)

