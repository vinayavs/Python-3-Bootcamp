# REVERSE CONTENT OF EACH WORD
# hi welcome => ih emoclew
s = input('ENTER STRINGS :')

l = s.split()
l1 = []
for word in l:
    l1.append(word[::-1])
res = ' '.join(l1)
print(res)