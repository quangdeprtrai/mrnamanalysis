while True:
    KhW = int(input('nhap so KhW: '))
    if KhW >= 0:
        break
s = 0

def over(n):
    if(n == 0):
        return n
    else:
        return (2000 + n * 100) + over(n - 1)
if KhW <= 100:
    s = KhW * 2000
else:
    s = 100 * 2000 + over(KhW - 100)

print('so tien dien: ',s)




