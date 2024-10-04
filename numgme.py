import random

top_num = input("enter number ")

# checking part
if top_num.isdigit():
    top_num = int(top_num)

    if top_num <= 0:
        print("please enter number larger than 0 next time ")
        quit()
else:
    print("please enter number next time ")
    quit()

randnum =  random.randint(0,top_num)

while True:
# checking part
    guess = input("enter guess number ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please enter number next time ")
        continue 

#logic part
    if guess == randnum:
        print("got it!")
        break
    elif guess > randnum:
        print("guess the smaller number ")
    else:
        print("guess the larger number ")