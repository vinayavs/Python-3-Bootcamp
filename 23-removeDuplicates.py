# REMOVE DUPLICATES FOR GIVEN STRING
# bassoon => bason
s = input('ENTER A STRING :')
res = ''
for ch in s:
    if ch not in res:
        res += ch
print(res)

# ALTERNATIVE
print(''.join(set(s))) # order not guarenteed