ds_num = []

fr = open('num_input.csv')

flines = fr.readlines()

for line in flines:
    ds_num = ds_num + line.strip().split(',')
    
print(ds_num)

ds_num = [int(i) for i in ds_num if i != '']

print(ds_num)

s = 0

for val in ds_num:
    s = s+ val

print('tong s la: ',s)