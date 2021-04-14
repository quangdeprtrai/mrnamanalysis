import thuvienham as lib
ds_num = []

fr = open('num_input.csv')

flines = fr.readlines()

for line in flines:
    ds_num = ds_num + line.strip().split(',')

ds_num = [int(i) for i in ds_num if i != '']

count = 0
tmp = []

fw = open('prime.txt', 'w')
for i in ds_num:
    if count == 5:
        count = 0
        fw.write(str(tmp) + '\n')
        tmp = []
    if lib.isPrime(i) == True:
        tmp.append(i)
        count += 1
    