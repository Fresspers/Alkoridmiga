from random import *
a1 = 0
f = open("BD/BD1.txt","w")
f.write("Штат Аризона, граничит с Мексикой.")
f.close
for i in range(20):
    f = open(f"{i}", "w")
    f.write(f"{randint(0,100)}")
    f.close