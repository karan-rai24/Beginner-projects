import random
score=0
ran=random.randint(1,100)
n=int(input('Guess the Number: '))
while n!=ran:
    if n<ran:
        print("Your guess is too small!")
        n=int(input('Try Again: '))
        score+=1
    elif n>ran:
        print('Your guess is too large!')
        n=int(input('Try Again: '))
        score+=1
else:
    print('You Guessed The Number in',score,'tries!')
