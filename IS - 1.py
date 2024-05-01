#program to store string "helloworld" and performs logical operations
#like AND,OR XOR
#between each character of string and 127.
str1="Helloworld"
for ch in str1:
s1=(ord(ch)&127)
s2=(ord(ch)|127)
s3=(ord(ch)^127)
print(ch+" & 127 :"+chr(s1)+'\t'+
ch+" | 127 :"+chr(s2)+'\t'+
ch+" ^ 127 :"+chr(s3)+'\t')
