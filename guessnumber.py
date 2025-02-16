import random 
value = random.randint(0,10)
print("You get 4 tries!")
i =1
while i<=4 :
    guess = int(input("enter a number: "))
    if(guess == value):
        print("Congratulations!")
        i=5
    elif(guess>value):
        print("try again! guessed too high")
    elif(guess<value):
        print("try again! guessed too low")
    if(i==4):
        print("Better Luck Next Time!")
    i= i+1