#plots
start = '''
one morning you decide to go to the mall. there are two ways to get there,
taking a quicker shortcut through the woods or taking a longer shortcut by side street.
'''

crackhead = '''
...you run into a crackhead! he's been hiding in the woods and you have
infiltrated his safe space! he attempts to attack you! do you run or fight?
'''

mall = '''
... you're walking down the street to the mall, but then it starts raining. the
mall is a mile away, but you think the rain is gonna come down harder really soon.
do you make a mad dash for the mall or turn and go back home?
'''

lostwoods = '''
you fought the crackhead! it was indeed a battle, but he had a knife and stabbed
you. he stole your money and went off to buy some more crack, along with other
drugs.
THE END
'''

print(start)    #BEGINNING
done = False
find_crackhead = False

print("type 'woods' to go left or 'street' to go right.")
while not done:
    user_input = input()
    if user_input == "woods": #OPTION 1
        print("you decide to go through the woods by turning left and...")
        done = True
        find_crackhead = True
        print(crackhead)
    elif user_input == "street": #OPTION 2
        print("you choose to go by side streets by turning right and ...")
        done = True
        print(mall)
    else:
        print("try again")
        done = False

if find_crackhead == True: #OPTION 1 CONT'D
    while not done:
        print("type 'fight' to fight the crackhead or 'run' to run away from him.")
        user_input = input()
            if user_input == "fight": #OPTION 1 CHOICE A
                print("you decide to fight the crackhead and..." + lostwoods)
            elif user_input == 'run': #OPTION 1 CHOICE B
                print("you decide to run and..")
            else:
                print("try again")
                done = False
