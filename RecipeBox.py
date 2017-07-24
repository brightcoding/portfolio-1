chicken_Salad_Ingrediants = {
'poached chicken': '4 cups (diced)',
'stalk celery': '1 (cut into 1/4-inch dice)',
'scallions': '4 (trimmed and thinly sliced)',
'tarragon': '1 1/2 teaspoons (finely chopped)',
'parsley': '2 tablespoons (finely chopped)',
'mayonnaise': '1 cup',
'lemon juice': '2 teaspoons',
'Dijon mustard': '1 teaspoon',
'kosher salt': '2 teaspoons',
'Freshly ground black pepper': "To your liking"
}
chicken_Salad_Instructions = [
"In a mixing bowl, toss together the chicken, celery, scallions and herbs. Set aside. In a small bowl, whisk together the mayonnaise, lemon juice, mustard, salt and pepper to taste. Add to the chicken and mix gently until combined. Refrigerate until ready to serve."
]
poached_Chicken_Ingrediants = {
'parsley':'10 sprigs',
'fresh thyme':'2 sprigs',
'small onion':'1 (halved)',
'small carrot': '1 (halved)',
'stalk celery':'1 (halved)',
'chicken breast halves':'3 pounds (on the bone and fat trimmed)',
'chicken broth': '5 to 6 cups'
}
poached_Chicken_Instructions = [
"Put the parsley, thyme, onion, carrot, celery, and chicken breasts in a medium saucepan. Cover with the broth, and bring just to a boil. Lower the heat to very low and cover. Poach the chicken for 20 minutes or until firm to the touch. Remove the pan from the heat, uncover, cool the chicken in the liquid for 30 minutes. Transfer the chicken to a cutting board and reserve the liquid. Bone and skin the chicken and cut the meat into 1 inch cubes. Discard the bones and skin. Strain the broth and store, covered, in the refrigerator for 3 days or freeze for later use. Remove any fat from the surface of the broth before using. "
]

PC = [poached_Chicken_Ingrediants, poached_Chicken_Instructions]
S = [chicken_Salad_Ingrediants, chicken_Salad_Instructions]
Together = {
'Poached_Chicken': PC,
'Salad': S
}

Cook_Book = {'Recipe1':Together}
#print(Cook_Book)

def Poached ():
    print(" ")
    print("Okay, First we need these ingredients...")
    print(" ")
    for i in poached_Chicken_Ingrediants:
        print (i,":", poached_Chicken_Ingrediants[i])
    input()
    print("Next, lets see the instruction")
    print(" ")
    print(poached_Chicken_Instructions)
    print(" ")

def Salad ():
    print(' ')
    print ("Let us do the Salad now!")
    input()
    print(" ")
    print("These are the ingredients you will need")
    print(" ")
    for i in chicken_Salad_Ingrediants:
        print(i, ":", chicken_Salad_Ingrediants[i])
    input()
    print("Here are the instructions")
    print(" ")
    print(chicken_Salad_Instructions)
    print(" ")

def CallRecipe ():
    print(' ')
    print(' ')
    print("Lets Make a Chicken Salad Today!")
    input()
    print("First, we would have to make poached chicken. Do you already know how to make poached chicken? If you know how to make poached chicken, type yes. If not, type no, and we will teach you how"
    )
    Q1 = input()
    if Q1 == "yes":
        Salad()
    if Q1 == "no":
        Poached()
        input()
        print("Now we can make the Salad")
        input()
        Salad()
        input()
    print("You are done! enjoy!")
CallRecipe()
