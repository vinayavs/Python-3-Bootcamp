# REPLICATE AND SORT THE CHARACTERS BASED ON FOLLOWED DIGIT
# a2b3c1 (fixed format)=> aabbbc
s = input('ENTER FIRST STRING  :')
# s = 'a2b3c1'
res = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        res = res + x*int(ch)
print(''.join(sorted(res)))