# Angelo Andrade
# 10-6-24
# string_file_list_chpt8.py

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # Guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])