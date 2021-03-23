a = float(input('nhap a: '))
b = float(input('nhap b: '))

if a > 0 or a < 0:
    x = -b/a
    print('PT co nghiem la: ',x)
else:
    if b == 0:
        print('PT co vo so nghiem')
    else:
        print('PT vo nghiem')