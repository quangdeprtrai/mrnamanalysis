import thuvienham as lib

x = int(input('nhap so tu nhien: '))

if(lib.isPrime(x) == True):
    print('x la so nguyen to')
else:
    print('x khong la so nguyen to')