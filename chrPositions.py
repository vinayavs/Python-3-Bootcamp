# PRINT THE CHARACTERS OF GIVEN STRINGS BASED ON POSITION
# eye, me , 1boy =>  em1, yeb, eo, y
s1 = input('ENTER A STRING :')
s2 = input('ENTER A STRING :')
s3 = input('ENTER A STRING :')
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    output = ''
    if i < len(s1):
        output+=s1[i]
        i+=1
    if j < len(s2):
        output+=s2[j]
        j+=1
    if k < len(s3):
        output+=s3[k]
        k+=1
    print(output)