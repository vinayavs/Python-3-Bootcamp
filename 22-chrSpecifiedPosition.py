# PRINT THE CHARACTERS ALONG WITH NEXT SPECIFIED POSITION OF THE STRING
# a4c0b1  => aeccbc
s = input('ENTER A STRING :')
res = ''
for ch in s:
    if ch.isalpha():
        res += ch
        x = ch
    else:
        d = int(ch)
        res = res + chr(ord(x)+d)
print(res)