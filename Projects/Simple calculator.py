a=int(input('Enter fisrt number: '))
b=int(input('Enter second number: '))
o=input('Enter the operator: ')
if o=='+':
    print (a+b)
elif o=='-':
    print (a-b)
elif o=='*':
    print (a*b)
elif o=='/':
    print (a/b)
elif o=='**':
    print (a**b)
else:
    print('Enter a valid input.')
