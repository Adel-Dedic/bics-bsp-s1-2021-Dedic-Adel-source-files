import os
s=input("Please enter a string: ")
rotor1=int(input("Please enter rotor 1 position (1-26): "))
rotor2=int(input("Please enter rotor 2 position (1-26): "))

q=str(input("Do you want to decipher a message? (Y/N) "))

def rotate_character(c, start, end):
    if c>=start and c<=end:
        window_width = ord(end)-ord(start)+1
        c_num = ord(c)
        c_num -= ord(start)
        c_num += rotor1
        c_num -= rotor2*2
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
    for c in s:
        c = rotate_character(c, 'A', 'Z')
        c = rotate_character(c, 'a', 'z')
        c= rotate_character(c, '0', '9')
        result +=c
    return result

def decrypt(s):
    global rotor1
    global rotor2
    rotor1=-rotor1
    rotor2=-rotor2
    return encrypt(s)

if q.lower() == 'y':
    print("The encrypted messages states as follows:",decrypt(s))
else:
    print("Your encrypted messages states as follows:",encrypt(s))

os.system('pause')
