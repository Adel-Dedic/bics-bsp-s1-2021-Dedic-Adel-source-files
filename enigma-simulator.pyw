from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("Enigma Simulator")
root.configure(background='#DCC489')

def button_set():
    if r1.get()!='' and r2.get()!='' and r3.get()!='':
        enigma.rotor1=int(r1.get())
        enigma.rotor2=int(r2.get())
        enigma.rotor3=int(r3.get())
    str_output.delete("1.0", END)
    button_encrypt['state']=NORMAL
    button_decrypt['state']=NORMAL
    text3['text']="The rotors are set my friend. ("+str(enigma.rotor1)+"/"+str(enigma.rotor2)+"/"+str(enigma.rotor3)+")"
    

def button_encrypt():
    s=str_input.get("1.0", END)
    str_output.delete("1.0", END)
    str_output.insert("1.0", encrypt(s))
    button_encrypt['state']=DISABLED
    button_decrypt['state']=DISABLED
    text3['text']="Choose your rotors again."
    r1.delete(0,END)
    r2.delete(0,END)
    r3.delete(0,END)

def button_decrypt():
    s=str_input.get("1.0", END)
    str_output.delete("1.0", END)
    str_output.insert("1.0", decrypt(s))
    button_decrypt['state']=DISABLED
    button_encrypt['state']=DISABLED
    text3['text']="Choose the value of the 3 rotors (Please make it between 1-26)"
    r1.delete(0,END)
    r2.delete(0,END)
    r3.delete(0,END)

# Text Boxes for 3 different rotors

r1 = Entry(root , width=5, borderwidth=1, bg='#FFEFD1')
r1.grid(row=1, column=0, columnspan=1, padx=10, pady=10)

r2 = Entry(root , width=5, borderwidth=1, bg='#FFEFD1')
r2.grid(row=1, column=1, columnspan=1, padx=10, pady=10)

r3 = Entry(root , width=5, borderwidth=1, bg='#FFEFD1')
r3.grid(row=1, column=2, columnspan=1, padx=10, pady=10)

button_set = Button(root, text="Set", padx=10, pady=0, command=button_set, bg='#B88933')
button_set.grid(row=1,column=3)

str_input = scrolledtext.ScrolledText(root, wrap=WORD, width=50, height=5)
str_input.grid(row=3, column=0, columnspan=5, padx=10, pady=15)

text1= Label(root, text="Insert your message: ", bg='#DCC489')
text1.place(x=10,y=49)

str_output = scrolledtext.ScrolledText(root, wrap=WORD, width=50, height=5)
str_output.grid(row=5, column=0, columnspan=5, padx=10, pady=15)

text2= Label(root, text="The result: ", bg='#DCC489')
text2.place(x=10,y=165)

text3= Label(root, text="Choose the value of the 3 rotors (Please make it between 1-26)",bg='#DCC489')
text3.grid(row=0, columnspan=5)

button_encrypt = Button(root, text="Encrypt", padx=30, pady=10, command=button_encrypt,bg='#B88933')
button_encrypt.grid(row=6, column=0, columnspan=2, padx=10, pady=15)

button_decrypt = Button(root, text="Decrypt", padx=30, pady=10, command=button_decrypt,bg='#B88933')
button_decrypt.grid(row=6, column=2, columnspan=2, padx=10, pady=15)


class Enigma():
    def __init__(self,rotor1,rotor2,rotor3):
        self.rotor1=rotor1
        self.rotor2=rotor2
        self.rotor3=rotor3

enigma=Enigma(0,0,0)

def rotate_character(c, start, end):
    if c>=start and c<=end:
        window_width = ord(end)-ord(start)+1
        c_num = ord(c)
        c_num -= ord(start)
        c_num += enigma.rotor1
        c_num -= enigma.rotor2
        c_num += enigma.rotor3*2
        c_num %=window_width
        c_num += ord(start)
        c = chr(c_num)
        return c
    else:
        return c

def rotor_change():
    if enigma.rotor1>0:
        if enigma.rotor1<26:
            enigma.rotor1+=1
        elif enigma.rotor2<26:
            enigma.rotor1=1
            enigma.rotor2+=1
        elif enigma.rotor3<26:
            enigma.rotor1=1
            enigma.rotor2=1
            enigma.rotor3+=1
        else:
            enigma.rotor3=1
    if enigma.rotor1<0:
        if enigma.rotor1>-26:
            enigma.rotor1-=1
        elif enigma.rotor2>-26:
            enigma.rotor1=-1
            enigma.rotor2-=1
        elif enigma.rotor3>-26:
            enigma.rotor1=-1
            enigma.rotor2=-1
            enigma.rotor3-=1
        else:
            enigma.rotor3=-1
    else:
        return
    

def encrypt(s):
    result = ''
    for c in s:
        c = rotate_character(c, 'A', 'Z')
        c = rotate_character(c, 'a', 'z')
        c = rotate_character(c, '0', '9')
        result +=c
        rotor_change()
            
    return result

def decrypt(s):
    enigma.rotor1=-enigma.rotor1
    enigma.rotor2=-enigma.rotor2
    enigma.rotor3=-enigma.rotor3
    return encrypt(s)

root.mainloop()
