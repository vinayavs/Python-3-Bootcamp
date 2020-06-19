# SORT ALPHABETS FOLLOWED BY DIGITS FOR GIVEN ALNUM STRING
# sorted() => always returns Lis & first digits and then alphabets
# But we need alphabets first

s = input('ENTER FIRST STRING  :')
# s = 'we3l2c5om9e'
alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
res = ' '.join(sorted(alphabets) + sorted(digits))
print(res)