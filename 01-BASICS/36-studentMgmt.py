# STUDENT MANAGEMENT
n = int(input('ENTER TOTAL NUMBER OF STUDENTS :'))
d = {}
for i in range(n):
    name = input('ENER NAME FOR SUTDENT NO {} :'.format(i+1))
    marks = int(input('ENTER MARKS FOR STUDENT NO {} :'.format(i+1)))
    d[name] = marks
print('STUDENT DATA INSERTED')
print('*' * 30)
print('NAME','\t\t','MARKS')
print('*' * 30)
for k,v in d.items():
    print(k,'\t\t',v)
print('*' * 30)
print('SEARCH OPERATION STARTED.........')
while True:
    name = input('ENTER A STUDENT NAME :')
    marks = d.get(name,-1)
    if marks == -1:
        print('STUDENT NOT FOUND !!')
    else:
        print('Marks of {} are {}'.format(name,marks))
    option = input('WANT TO KNOW ANOTHER STUDENT DETAILS? (YES/NO) :')
    if option.upper() == 'NO':
        break
print('Thanks for using student app')