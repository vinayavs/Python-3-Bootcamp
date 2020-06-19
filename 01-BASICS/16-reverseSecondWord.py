# REVERSE EVERY SECOND WORD OF GIVEN SENTENCE
# hi welcome to python  => hi emoclew to nohtyp
s = input('ENTER A SENTENCE :')
l = s.split()
l1 = []
i = 0
while i < len(l):
    if i%2 != 0:
        l1.append(l[i][::-1])
    else:
        l1.append(l[i])
    i+=1
res = ' '.join(l1)
print(res)

# ALTERNATIVE
# l = s.split()
# l1 = []
# for i in range(0, len(l)):
#     if i%2 != 0:
#         l1.append(l[i][::-1])
#     else:
#         l1.append(l[i])
# res = ' '.join(l1)
# print(res)