# NO OF OCCURRENCES FOR GIVEN STRING
s = input('ENTER A STRING :')
l = []
for ch in s:
    if ch not in l:
        l.append(ch)

# print(l)
for i in sorted(l):
    print('{} OCCURS {} TIMES'.format(i,s.count(i)))

# ALTERNATIVE
s1 = set(s)
for i in sorted(s1):
    print('{} occurs {} times'.format(i,s.count(i)))

# ALTERNATIVE
d = {}
for ch in s:
    d[ch] = d.get(ch,0) + 1
print(d)   
for k,v in sorted(d.items()):
    print('{} OCCURS {} TIMES'.format(k,v)) 
