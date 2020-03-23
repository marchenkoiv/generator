import random
import string



def crword(lines):
    st = ''
    for g in range(random.randint(1,3)):
            st += random.choice(lines)
    for g in range (random.randint(0,3)):
        t = random.randint(0,100)
        if t == 0:
            st = st*2
        if t == 1 or t == 2:
            q = random.randint(0,len(st))
            st = st[q:random.randint(q, len(st))]
        if 2 < t < 100:
            q = random.randint(0,len(st))
            st = st[:q]+random.choice(string.ascii_letters + string.digits)+st[q+1:]
        if t == 100:
            q=random.randint(0,len(st))
            a = random.randint(33,57)
            st = st[:q]+chr(a)+st[q+1:]

    return st



def inputt():
    try:
        k = int(input())
    except (TypeError, ValueError):
        print ("You entered incorrect data! Enter again!")
        k = inputt()
    return k


with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
file.close()
f = open('voc.txt', 'w')
print("\nEnter number of functions")
n = inputt()
for k in range(n):
    str = crword(lines)
    str += '='
    str += crword(lines)
    str += "( "
    for m in range(random.randint(0,10)):
        r=random.randint(0,1)
        if r == 0:
            str += crword(lines)
        if r==1:
            for a in range(random.randint(0,22)):
                str += random.choice(string.digits)
        str += ','
    str = str[0:len(str)-1]
    str += " );"
    q=random.randint(0,len(str))
    str = str[:q]+random.choice(string.ascii_letters + string.digits)+str[q+1:]
    f.write(str+'\n')
f.close()