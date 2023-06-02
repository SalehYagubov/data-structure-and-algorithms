# in operatörü ile listin içindeki herhansı bir elementin olub olmadıgını yoxlaya bilerin
#evvelce shoppinglist adında bir list yaradaq
shoppingList = ['Milk','Cheese','Butter']
print(shoppingList)
#indi ise Milkin shoppingListin içinde olub olmadığına baxaq

print('Milk' in shoppingList)
#eger termınalda True çıxırsa demelı elementlerden birı Milkdir deyılse False çıxmalıdı.öRNEK:  
print('Bread' in shoppingList)

########ACCESSİNG and Traversing elements
#asagıdakı ornekde listın içindekı strınglere "+"" elave edıb tekrar yazdırdıq
shoppingList = ['Milk','Cheese','Butter']
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])


total = []
while(True):
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total.append(value)
    average = sum(total)/len(total)

print('Average:',average)