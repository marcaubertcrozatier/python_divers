#!/usr/bin/python3
# -*-coding:Utf-8 -*

import math
import random

res = random.randrange(50)
pari = int(input("Ton pari : "))
mise = int(input("Ta mise : "))
print("Nombre à trouver : ", res)
if pari == res:
    gain = mise * 3
    print ("Gagné, dans le mille !! Vous remportez 3 fois la mise, soit ", gain, "$")
elif pari % 2 == res % 2:
    gain = math.ceil(mise + mise / 2)
    print ("Gagné à pair ou impair !!! Vous remportez 50%, soit ", gain, "$")
# print ("Gagné !!! Vous remportez ",gain)
else:
    print("Perdu... retente ta chance ;)")
