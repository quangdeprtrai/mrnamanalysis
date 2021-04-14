import thuvienham as lib

n = int(input('nhap so tu nhien: '))

s = 0

for i in range(n + 1):
    if(lib.isPrime(i) == True):
        print(i)
        s = s + i
print(s)