import os
s=input("Please enter a message: ")
rotor1=int(input("Please enter rotor 1 position (any intiger): "))
rotor2=int(input("Please enter rotor 2 position (any intiger): "))
rotor3=int(input("Please enter rotor 2 position (any intiger): "))
rotors=rotor1+rotor2*(rotor1+rotor3)+rotor3*211546145

q=str(input("Do you want to decipher a message? (Y/N) "))

def rotate_character(c, start, end, amount):
    if c>=start and c<=end:
        window_width = ord(end)-ord(start)+1
        c_num = ord(c)
        c_num -= ord(start)
        c_num += amount
        c_num %=window_width
        c_num += ord(start)
        c = chr(c_num)
        rotor_change
        return c
    else:
        return c

def rotor_change():
    if rotor1>0 and rotor1<27:
        rotor+=1
    if rotor+1>27:
        rotor1=1
        if rotor2>0 and rotor2<27:
            rotor2+=1
        else:
            rotor2=1

def encrypt(s):
    result = ''
    amount=rotors
    for c in s:
        c = rotate_character(c, 'A', 'Z', amount)
        c = rotate_character(c, 'a', 'z', amount)
        c= rotate_character(c, '0', '9', amount)
        result +=c
    return result

def decrypt(s):
    global rotors
    rotors=-rotors
    return encrypt(s)

if q.lower() == 'y':
    print("The encrypted messages states as follows:",decrypt(s))
if q.lower() == 'n':
    print("Your encrypted messages states as follows:",encrypt(s))

#os.system('pause')


