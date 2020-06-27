# TO GET VALUE FOR GIVEN KEY
k = int(input('ENTER A KEY VALUE :'))
d = {10: 'A', 20: 'B', 30: 'B', 50: 'V'}

if k in d:
    print('The corresponding values is :',d.get(k))
#     print('The corresponding values is :',d[k])
else:
    print('Specified key is not avaialbe')