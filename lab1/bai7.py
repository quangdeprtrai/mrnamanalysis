n = int(input('nhap so n: '))
print('nhap so n: ',n)

fw = open('out.txt', 'w')
fw.write('nhap so n: ' + str(n) + '\n')
for i in range(n):
    if i % 2 ==0:
        fw.write(str(i) + '\r\n')

fw.close()