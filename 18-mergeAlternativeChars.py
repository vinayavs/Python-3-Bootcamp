# MERGE ALTERNATIVE CHARACTERS OF 2 STRINGS 
s1 = input('ENTER FIRST STRING  :')
s2 = input('ENTER SECOND STRING  :')
i,j = 0,0
res = ''
while i < len(s1) or j < len(s2):
    if i < len(s1):
        res = res + s1[i]
        i = i+1
    if j < len(s2):
        res = res + s2[j]
        j = j+1
print(res)

# OR IF LENGTH OF BOTH GIVEN SRINGS ARE SAME    
# while i < len(s1) or i < len(s2):
#     output = output + s1[i] + s2[i]
#     i = i+1
# output    