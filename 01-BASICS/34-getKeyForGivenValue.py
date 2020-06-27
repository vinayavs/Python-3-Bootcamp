# TO GET THE KEY FOR GIVEN VALUE
value = input('ENTER A VALUE :')
d = {10: 'A', 20: 'B', 30: 'B', 50: 'V'}
available = False
for k,v in d.items():
    if v == value:
        print('The Corresponding Key is :',k)
        available = True
if available == False:
    print('The Specified Value is not available')
    