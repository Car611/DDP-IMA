str="Hello World"
Uppercase=0
Lowercase=0

for i in str:
    if i.isupper():
       Uppercase+=1
    elif i.islower():
       Lowercase+=1

print('Uppercase:%d, Lowercase:%d' % (Uppercase, Lowercase))