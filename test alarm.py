from time import *
x= 0
z=10
h= str
m= str
s= str
x= str
list_h= []
list_m= []
list_s= []

def test():
    while True:
        x = input('entrer votre alarme sous format HH:MM:SS : ')
        h = x[0:2]
        m = x[3:5]
        s = x[6:8]
        print ('votre arlarme est bien regler pour ' + x +' Y/N :') 
        y = input()
        if y == "Y":
            print("good")
            print(h)
            list_h.append(h)
            hs= list_h[-1] 
            list_h[-1]= hs * 3600
            print(h + ' = ' + list_h[-1])
            print(m)
            ms = m * 1
            print(m + ' = ' + ms)
            print(s)
            break
        elif y == "N":
            continue
test()
