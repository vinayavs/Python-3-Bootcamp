# PRINT SUM OF VALUES FOR GIVEN DICTIONARY
# input => d = {'A':10, 'B':20, 'C':30}
d = eval(input('ENTER A DICT :'))
sum = 0
for k,v in d.items():
    sum += v
print(sum)

# for item in d.items():
#     sum = sum + item[1]
# print(sum)

# ALTERNATIVE
# print(sum(d.values()))

