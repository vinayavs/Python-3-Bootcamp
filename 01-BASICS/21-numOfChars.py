# PRINT NO OF REPEATED NUMBER WITH CHAR
# aaabbccccz  => 3a2b4c1z
s = input('ENTER A STING :')
pre = s[0]
cnt = 1
i = 1
res = ''
while i < len(s):
    if pre == s[i]:
        cnt = cnt+1
    else:
        res = res + str(cnt) + pre
        pre = s[i]
        cnt = 1
    if i == len(s)-1:
        res = res + str(cnt) + pre
    i += 1    
print(res)
