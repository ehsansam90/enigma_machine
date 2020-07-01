import pickle

f = open('./today_routor.enigma','rb')
r1,r2,r3 = pickle.load(f)
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def reflector(x):
    return alphabet[len(alphabet) - alphabet.find(x) - 1]

def enigma_char_(c):
    reflected = reflector(r3[alphabet.find(r2[alphabet.find(r1[alphabet.find(c)])])])
    return alphabet[r1.find(alphabet[r2.find(alphabet[r3.find(reflected)])])]

def rotate_rotor():
    global r1,r2,r3
    r1=r1[1:]+r1[0]
    if state % 26 ==0:
        r2=r2[1:]+r2[0]
    if state %(26*26) ==0:
        r3=r3[1:]+r3[0]


plain = input("Enter your sentence: ")
cipher =''
state = 0

for c in plain:
    if c.isspace() == True:
        cipher += ' '
    else:
        cipher += enigma_char_(c)
        rotate_rotor()
        state += 1


print('This is Enigma coded: ',cipher)
print(enigma_char_('w'))