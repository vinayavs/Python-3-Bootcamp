# REVERSE ORDER OF THE WORDS, LAST WORD BECOMES 1ST, 1ST BECOMES LAST
# hi welcome  => welcome hi
s = input('ENTER WORDS :')
l = s.split()
res = ' '.join(l[::-1])
print(res)