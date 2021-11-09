from tkinter import *
from tkinter import scrolledtext

# Defines a root where the widgets are displayed and the title
root = Tk()
root.title("Enigma Simulator")
root.configure(background='#DCC489')

# Below are all buttons which are present on the interface itself

# 'Set' button is required to initialise the 3 different rotors to specific values
def button_set():
    
    # If the conditions hold, the rotors will be passed as the rotor settings and encryption/decryption will get allowed
    if (r1.get()!='' and r2.get()!='' and r3.get()!='') and (int(r1.get())>0 and int(r1.get())<27 and
         int(r2.get())>0 and int(r2.get())<27 and
         int(r3.get())>0 and int(r3.get())<27):
        enigma.rotor1=int(r1.get())
        enigma.rotor2=int(r2.get())
        enigma.rotor3=int(r3.get())
        enigma.rotors=[enigma.rotor1,enigma.rotor2,enigma.rotor3]
    
        str_output.delete("1.0", END)
        button_encrypt['state']=NORMAL
        button_decrypt['state']=NORMAL
        rotor_label['text']="The rotors are set my friend. ("+str(enigma.rotor1)+"/"+str(enigma.rotor2)+"/"+str(enigma.rotor3)+")"

    # If the conditions are not hold, the rotors will not be set and the user shall be asked to try again
    else:
        rotor_label['text']="Please make sure that the values are between 1 and 26."
        button_decrypt['state']=DISABLED
        button_encrypt['state']=DISABLED
        
# Purpose of this button is to encrypt() the input message and outputs at the end; the buttons get disabled
# And the user is asked to set rotors again to proceed encrypting/decrypting another message
def button_encrypt():
    s=str_input.get("1.0", END)
    str_output.delete("1.0", END)
    str_output.insert("1.0", encrypt(s))
    button_encrypt['state']=DISABLED
    button_decrypt['state']=DISABLED
    button_export['state']=NORMAL
    rotor_label['text']="Set the rotors again to continue. ("+str(enigma.rotor1)+"/"+str(enigma.rotor2)+"/"+str(enigma.rotor3)+")"

# Purpose of this button is decrypt a given message through the set rotors with decrypt()
# Equivalenty, the user is again asked to configure the rotors again to proceed
def button_decrypt():
    s=str_input.get("1.0", END)
    str_output.delete("1.0", END)
    str_output.insert("1.0", decrypt(s))
    button_decrypt['state']=DISABLED
    button_encrypt['state']=DISABLED

# To help the process of copying/pasting and remembering the rotor settings, the program is equipped with functionalities to import & export 'keys'
# These function will take the information contained in the 'key.txt' file and proceed them into correct boxes
def button_import():

    # Reads the corresponding file ('key.txt') and gathers information
    fileRead()
    str_input.delete("1.0", END)
    str_input.insert("1.0", enigma.input)

    r1.delete(0,END)
    r1.insert(0,str(enigma.rotor1))
    r2.delete(0,END)
    r2.insert(0,str(enigma.rotor2))
    r3.delete(0,END)
    r3.insert(0,str(enigma.rotor3))

    # Allows the user to proceed decrypting the message    
    str_output.delete("1.0", END)
    button_decrypt['state']=NORMAL
    rotor_label['text']="The rotors are set my friend. ("+str(enigma.rotor1)+"/"+str(enigma.rotor2)+"/"+str(enigma.rotor3)+")"

# Simply exports a text file named 'key.txt' where information is saved concerning the rotor settings and the encrypted message
def button_export():
    enigma.output=str_output.get("1.0",END)
    fileCreate()

# r1, r2 and r3 and simple text boxes where the user should use to configure values of each rotor in that corresponding order
r1 = Entry(root , width=5, borderwidth=1, bg='#FFEFD1')
r1.grid(row=1, column=0, columnspan=1, padx=10, pady=10)

r2 = Entry(root , width=5, borderwidth=1, bg='#FFEFD1')
r2.grid(row=1, column=1, columnspan=1, padx=10, pady=10)

r3 = Entry(root , width=5, borderwidth=1, bg='#FFEFD1')
r3.grid(row=1, column=2, columnspan=1, padx=10, pady=10)

# The next two are a bit more sophisticated text boxes which allow scrolling thus easier navigation through longer texts
# And its sole purpose is for the user to write and respectively read a message
str_input = scrolledtext.ScrolledText(root, wrap=WORD, width=50, height=10)
str_input.grid(row=3, column=0, columnspan=4, padx=10, pady=15)

str_output = scrolledtext.ScrolledText(root, wrap=WORD, width=50, height=10)
str_output.grid(row=5, column=0, columnspan=4, padx=10, pady=15)

# This is welcome gesture where it asks the user to write inside the 'simple text boxes' from above values for the rotors
rotor_label= Label(root, text="Choose the value of the 3 rotors (Please make it between 1-26)",bg='#DCC489', font=('Arial',11))
rotor_label.grid(row=0, columnspan=5)

# Simple 'title' labels for the two more sophisticated text boxes to mark more visibly which one's porpuse is
input_label= Label(root, text="Insert your message: ", bg='#DCC489')
input_label.place(x=10,y=52)

output_label= Label(root, text="The result: ", bg='#DCC489')
output_label.place(x=10,y=245)

# The last label is a notice explaining purpose of the 'Import/Export' button have
notice_label = Label(root, text="*These buttons will create and read only a text file named 'key.txt'", bg='#DCC489', font=('Arial',7))
notice_label.place(x=30,y=559)

button_set = Button(root, text="Set", padx=10, pady=0, command=button_set, bg='#B88933')
button_set.grid(row=1,column=3)

# The rest are buttons created for respectul porpuse as indicated with their names and this way they get included into the interface
button_encrypt = Button(root, text="Encrypt", padx=63, pady=10, command=button_encrypt,bg='#B88933', state=DISABLED)
button_encrypt.grid(row=6, column=0, columnspan=2)

button_decrypt = Button(root, text="Decrypt", padx=63, pady=10, command=button_decrypt,bg='#B88933', state=DISABLED)
button_decrypt.grid(row=6, column=2, columnspan=2)

button_export = Button(root, text="Export A Key*", padx=50, pady=10, command=button_export,bg='#B88933', state=DISABLED)
button_export.grid(row=7, column=0, columnspan=2, pady=20)

button_import = Button(root, text="Import A Key*", padx=50, pady=10, command=button_import,bg='#B88933')
button_import.grid(row=7, column=2, columnspan=2, pady=20)


# The most important information is stored into this class named 'Enigma()' and it allows to access more freely its components and navigate through the program itself
class Enigma():
    def __init__(self,rotor1,rotor2,rotor3,rotors,input, output):
        self.rotor1=rotor1
        self.rotor2=rotor2
        self.rotor3=rotor3
        self.rotors=rotors
        self.input=input
        self.output=output

# Using the class, we configure its initial values which will get modified as soon as user starts using the program
enigma=Enigma(0,0,0,[0,0,0],'','')

# This allows to 'rotate' a character based on steps (in this case through permutation with help of the rotors)
# It makes sure it says between certain boundaries thanks to the ordinal of characters.
# i.e. capital letters stay capital and so do small letters and numbers included
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

# As it was true for the real Enigma, rotor_change() allows the rotors to be dynamic and change as the program computates the encrypted message
# It increments rotor 1 by a value of 1 till the value of 26, as soon as rotor 1 reaches the value 26 than rotor 2 increments by 1 and so on
# To make sure it works properly, it utilizes a number of if statements to assure that the values of each rotor is between 1 and 26
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
    
# This function is called when the user is intending to encrypt a message
# It takes every character containing in the message and proceeds to 'rotate' following its conditions and what kind of character it is. i.e. capital letter
# As the program runs and computates the message, rotor_change() is being called each time a character is processed to increment the respectful rotors
# As a result, it returns the initial message BUT uniquely decrypted based on the initial rotor settings
def encrypt(s):
    result=''
    for c in s:
        c = rotate_character(c, 'A', 'Z')
        c = rotate_character(c, 'a', 'z')
        c = rotate_character(c, '0', '9')

        result +=c
        rotor_change()

    return result

# To decrypt the message, the main idea is to 'back track' the same steps taken upon encrypting the message
# In this case, we invert the rotors and simply recall the encrypt(..) function
def decrypt(s):
    enigma.rotor1=-enigma.rotor1
    enigma.rotor2=-enigma.rotor2
    enigma.rotor3=-enigma.rotor3
    return encrypt(s)

# For Import function, it's necessary to read the information stored onto the 'key.txt' files to import it into the program
# The message included into the text file is stored as enigma.input and the rotor settings to their respectful tag (enigma.rotorX)
def fileRead():
    f=open('key.txt','r')
    for s in f.readlines()[5:]:
        enigma.input+=s
    f=open('key.txt','r')
    enigma.rotor1=int(f.readlines()[1])
    f=open('key.txt','r')
    enigma.rotor2=int(f.readlines()[2])
    f=open('key.txt','r')
    enigma.rotor3=int(f.readlines()[3])

# For Export function, the information stored while computing the message is transfered to a NEW text file (of if a file named 'key.txt' already exist then it gets replaced)
# The text file is fairly readable by a human but it cannot be understood without the program to decrypt it with
def fileCreate():
    f = open('key.txt','w')
    f.write('------- Rotors settings -------\n')
    for s in enigma.rotors:
            f.write(str(s)+'\n')
    f.write('------- The Encrypted Message -------\n')
    f.write(enigma.output)
    f.close()

# This assures that the window cannot be resized and won't close on its own
root.resizable(False, False) 
root.mainloop()
