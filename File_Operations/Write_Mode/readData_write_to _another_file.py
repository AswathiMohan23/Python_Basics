# read data from one file and print it in another file
# ======================================================

f = open('universe', 'r')
f1 = open('newFile', 'w')

for i in f:
    f1.write(i)