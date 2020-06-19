# REVERSE OF A GIVEN STRING
# welcome  -> emoclew
s = input('ENTER A STRING TO REVERSE :')
print(s[::-1])

# ALTERNATIVE - BY USING reversed()
r = reversed(s)
# print(type(r))  # <class reversed>
print(''.join(r))

# ALTERNATIVE
output = ''
i = len(s)-1   # for vinlabs, indexes are 0 1 2 3 4 5 6 so len('vinlabs')-1 = 6 
while i >= 0:
    output += s[i]
    i -= 1
print(output)

# ALTERNATIVE
r2 = reversed(s)
for i in r2:
    print(i,end='')