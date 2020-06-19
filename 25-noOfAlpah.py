# PRINT NO OF ALPHABETS IN SORTED MANNER
# ABAABBCA => 4A3B1C 

s = input('ENTER A STRING :')
d = {}
res = ''
for ch in s:
    d[ch] = d.get(ch,0) + 1
for k,v in d.items():
    res = res + str(v) + k
print(res)

# ABAABBCA => A4B3C1
# output = output + k + str(v)