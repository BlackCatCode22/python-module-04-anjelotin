# Angelo Andrade
# 10-6-24
# exercise_7.1.py
# Opening and Reading a File


fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())

