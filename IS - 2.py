import math
plaintext="transposition technique using python"
key=8
ciphertext=['']*key
for colum in range(key):
pointer=colum
while pointer<len(plaintext):
ciphertext[colum]+=plaintext[pointer]
# print(ciphertext)
pointer+=key
cipher=' '.join(ciphertext)
print(cipher)
nC = math.ceil(len(cipher) / key)
print(nC )
nR = key
numOfShadedBoxes = (nC * nR) - len(cipher)
pt = [''] * nC
col=0
row=0
for sym in cipher:
pt[col]+=sym
col+=1
if (col == nC) or (col == nC - 1 and row >= nR- numOfShadedBoxes):
col=0
row=row+1
print(''.join(pt))
