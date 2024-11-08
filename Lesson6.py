# Vòng lặp hữu hạn - vòng lặp for

# Hàm range()
    # range(start, end, step)
        # start: số bắt đầu (không bắt buộc, mặc định = 0)
        # end: số kết thúc (bắt buộc)
        # step: số bước nhảy (không bắt buộc, mặc định = 1)
print('for i in range(1, 11, 2):')
for i in range(1, 11, 2):           # Output: 1 3 5 7 9
    print(i, end = ' ')

    # range(start, end):
print('\nfor i in range(1, 5):')
for i in range(1, 5):               # Output: 1 2 3 4 
    print(i, end = ' ')

    # range(end):
print('\nfor i in range(6):')
for i in range(6):                  # Output: 0 1 2 3 4 5 
    print(i, end = ' ')

# Ví dụ:
# range(5, 10):         5 6 7 8 9
# range(2, 7, 2):       2 4 6
# range(4):             0 1 2 3
# range(10, 15, 2):     10 12 14
# range(5, 20, 3):      5 8 11 14 17
# range(8, 13):         8 9 10 11 12
# range(7, 15, 2):      7 9 11 13 
# range(2, 8, 3):       2 5 

# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]
a = int(input('\nNhập a: '))
b = int(input('Nhập b: '))
print(f'Các số trong khoảng [{a}, {b}] là:')
for i in range(a, b+1):
    print(i, end = ' ')

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b] nếu b >= a
# In ra các số nguyên trong khoảng [b, a] nếu a > b
a = int(input('\nNhập a: '))
b = int(input('Nhập b: '))

if b >= a:
    print(f'Các số trong khoảng [{a}, {b}] là:')
    for i in range(a, b+1):
        print(i, end = ' ')
else:
    print(f'Các số trong khoảng [{b}, {a}] là:')
    for i in range(b, a+1):
        print(i, end = ' ')

# Sử dụng random - ngẫu nhiên
    # Khai báo thư viện
import random
    # Cú pháp sử dụng: [Tên thư viện].[Tên hàm]
rd = random.randint(2, 9)
print('Số ngẫu nhiên:', rd)

# Bài tập: in ra bảng cửu chương từ số vừa random
print('Bảng cửu chương', rd)
for i in range(1, 11):
    print(f'{rd} x {i} = {rd * i}')

# In ra bảng cửu chương từ 3 đến 6
# Thứ tự sử dụng biến đếm: i, j, k
for i in range(3, 7):
    print('\nBảng cửu chương', i)
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')