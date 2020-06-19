# NO OF OCCURRENCES OF THE VOWLES FOR A GIVEN STRING
s = input('ENTER A STRING :')
v = {'a','e','i','o','u','A','E','I','O','U'}
d = {}
for ch in s:
    if ch in v:
        d[ch] = d.get(ch,0)+1
for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))