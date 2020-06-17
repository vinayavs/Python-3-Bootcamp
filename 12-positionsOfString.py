# DISPLAY ALL POSITIONS OF SUBSTRING FOR GIVEN STRING
s=input("Enter main string:")
subs=input("Enter sub string:")
flag = True
pos = 0
l = len(s)
while True:
    pos = s.find(subs, pos, l)
    if pos == -1:
        # print('Break executed')
        break
    print("Position Found at :",pos)
    flag = True
    pos += len(subs)
if flag == False:
    print('Position Not Found')
# Alternative
# s=input("Enter main string:")
# subs=input("Enter sub string:")
# i = s.find(subs)
# if i == -1:
#     print("Position Not Found :")
# while i != -1:
#     print('{} present at index: {}'.format(subs,i))
#     i = s.find(subs,i+len(subs),len(s))  # Search the remaining string