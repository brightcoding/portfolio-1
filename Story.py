start = '''You are walking your dog Coco and she has to go pee but you have to
get to work or you are going to be late for the 5th time and if you are late
on the 5th time you get fired'''
print(start)
user_input = input('''type home to go to your house and change into your work
attire or type wait to keep walking your dog''')
if user_input =="home":
    print('''you go home and your dog pees on the floor before you leave. Coco
    is now stained. since you were running late, you had to get on a later bus
    where you see your old teacher from high school and she tells you that there
    is a job opening at a startup technology company in which she is the co-
    founder. she proceeds to offer you the job.''')
    user_input2 = input("Do you accept the job?")
    if user_input2 == "yes":
        print("you have accepted the job and began to work right away")
        print("the end")
    if user_input2 == "no":
        print("your boss fires you because you are late. Now you have no job")
        print("the end")
if user_input == "wait":
    print('''you wait for your dog to pee and you get back home, change, and get
    to work a minute before you are late. You come back home and your dog just
    got groomed and you set up for your family to come and they see that your
    place is nice and that you are able to take care of yourself and they said
    that they will give you some money''')
    print("the end")
