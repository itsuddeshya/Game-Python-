print("comp turn : stone(s) paper(p) seasor(s) ")

import random
rnum = random.randint(1,3) 
if rnum == 1:
    comp = 'st'
elif rnum == 2:
    comp = 'p'
elif rnum == 3:
    comp = 's'

u = input("your turn stone(s) paper(p) seasor(s) ?  ")
print("comp choosed",comp)
print("you choosed",u)

if comp == u :
    print("tie")
elif comp == 'st':
    if u == 'p':
        print("you won")
    elif u == 's' :
        print("you loose")
elif comp == 'p':
    if u == 's':
        print("you won")
    elif u == 'st' :
        print("you loose")
if comp == 's':
    if u == 'st':
        print("you won")
    elif u == 'p' :
        print("you loose")

