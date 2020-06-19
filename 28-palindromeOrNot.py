# CHECK GIVE STRING IS PALINDROME OR NOT
# PALINDROME - a word, phrase, or sequence that reads the same backward as forward
# madam, nursesrun, level, eye, malayalam
s = input('ENTER A STRING :') 

if s == s[::-1]:
    print('IT IS A PALINDROME')
else:
    print('IT IS NOT A PALINDROME')