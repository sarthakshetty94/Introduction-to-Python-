import random
a=["rock","paper","scissor"]
while(True):                                                #Infinite Loop
    r=random.randrange(0,3)                                 #Selects a random number from 0-3
    c=a[r]                                                  
    O=input("Select your option from rock, paper, scissor") #Asks for an input
    if(O==c):                                               #Tie condition
        print("Tie")
    elif(O==a[0])&(c==a[2]):                                #Condition when the User chooses Rock and the Computer chooses Scissor
        print("You win`")
    elif(O==a[1])&(c==a[0]):                                #Condition when the User chooses Paper and the computer chooses Rock
        print("You win")
    elif(O==a[2])&(c==a[1]):                                #Condition when the User chooses Scissor and the computer chooses Paper
        print("You win")
    else:
        print("You lose")                                   #Unless the above condition, Rest is lose.
    print("The computer chose",c)
