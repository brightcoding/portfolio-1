mylist = []
t = True
print(' ')
More = input("Lets create a list! type in anything you want to include in the list. Press enter to start, and type * when you are finished.")
print(' ')
while t == True:
    if More == "#":
        t = False
        print(' ')
        print("The list has been created:")
        del mylist[(len(mylist)-1)]
        print(' ')
        print(mylist)
    else:
        More = input("What do you want to add to your list? type here -->")
        m = More.lower()
        mylist.append(m)
        print(' ')
        print("This is what your list looks like now")
        print(' ')
        print(mylist)

def bubblesorting():
    s = len(mylist)-1
    while 0 <= s:
        for i in range(s):
            if mylist[i] < mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i], mylist[i+1]
            else:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
        s = s-1
bubblesorting()
print(' ')
print("lets alphabetize it")
print(' ')
print(mylist)
print(' ')
