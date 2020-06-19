# PRINT THE CHARACTERS BASED ON EVEN AND ODD INDEX FOR GIVEN STRING
s = input('ENTER A STRING TO REVERSE :')

i =0
print('CHARACTERS AT EVEN INDEX =>')
while i < len(s):
    print(s[i])
    i += 2
print('CHARACTERS AT ODD INDEX =>')
i = 1
while i < len(s):
    print(s[i])
    i += 2
# ALTERNATIVE
print('CHARACTERS AT EVEN INDEX =>')
print(s[::2])
print('CHARACTERS AT ODD INDEX =>')
print(s[1::2])