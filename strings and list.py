a=" wajahat "
# print(a[1])
# print(len(a))

# for x in 'banana':
#     print(x,end=" ")

txt="This is me free from all kinds of worries. Alhamdulillah"
# print("Alhamdulillah" in txt)
# if "freeq" in txt:
#     print("Yes free is present")
# else:
#     print("Nahi ha bhai")

print("wajahat" not in txt)
#
# print(a[2:5])
# print(a[:5])
# print(a[5:])
# print(a[-5:-2])

# print(a.strip()+"hogaya") #strip() removes space from start and end
# print(a.replace("j","r"))
# print(a.split("j"))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

thisList=['wajahat','ali','yemaho']

print(thisList)
print(type(thisList))
thisList1=list(('wajahat','ali','yemaho'))
print(thisList1)
if "wajahat" in thisList:
    print("Exist")


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)

# thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

thislist.pop(1)
print(thislist)

del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear() # del thislist will delete the complete the whole list
print(thislist)

thislist = ["apple", "banana", "cherry"]
[print(x+" hahaha") for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "apple" in x]
# newlist = [x for x in fruits if x!="apple" ]
# newlist = [x.upper() for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)