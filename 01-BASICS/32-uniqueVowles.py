# DISPLAY NO OF UNIQUE VOWLES FOR THE GIVEN WORD
word = input('ENTER A WORD :')
vowles = ['a','e','i','o','u']
res = []
# for ch in word:
#     if ch in vowles:
#         if ch not in res:
#             res.append(ch)
# print(res)
# print('THE NO OF UNIQUER VOWLES ARE :',len(res))

# ALTERNATIVE
# for ch in vowles:
#     if ch in word:
#         res.append(ch)
# print(res)
# print('THE NO OF UNIQUER VOWLES ARE :',len(res))

# ALTERNATIVE - LIST COMPREHENSION
result = [ch for ch in vowles if ch in word]
print(result)
print('THE NO OF UNIQUER VOWLES ARE :',len(result))