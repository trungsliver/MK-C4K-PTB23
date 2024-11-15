# # Vòng lặp vô hạn - vòng lặp while

# # Hiện ra màn hình các số từ 0 đến 5
#     # Vòng lặp for
# for i in range(0,6):
#     print(i, end=' ')

#     # Vòng lặp while
# i = 0
# while i < 6:
#     print(i, end=' ')
#     i = i + 1       # i += 1

# # Bài 1: Nhập số nguyên n trong khoảng [0,100]
# # nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# n = int(input('Nhập số nguyên trong khoảng [0,100]: '))
# while n < 0 or n > 100:
#     print('Bạn đã nhập sai!')
#     n = int(input('\nNhập số nguyên trong khoảng [0,100]: '))
# print('Bạn đã nhập đúng!')

# # =============== ÔN TẬP ===============
# # Dạng 1: In / Hiển thị ra màn hình
#     # 1.1. In ra màn hình các số từ 0 đến n
# n = int(input('Nhập số nguyên n: '))
# for i in range(0, n+1):
#     print(i, end = ' ')

#     # 1.2. In ra các số nguyên trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# if a <= b:
#     for i in range(a, b+1):
#         print(i, end = ' ')
# else:
#     for i in range(b, a+1):
#         print(i, end = ' ')

#     # 1.3. In ra các số chẵn trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# for i in range(a, b+1):
#     if i % 2 == 0:
#         print(i, end = ' ')
    
#     # 1.4. In ra các số lẻ trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# for i in range(a, b+1):
#     if i % 2 != 0:
#         print(i, end = ' ')

# # Dạng 2: Tính tổng
#     # 2.1. Tính tổng các số trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# tong = 0    # Dùng để lưu giá trị tổng
# for i in range(a, b+1):
#     tong = tong + i     # tong += i
# print(f'Tổng các số trong khoảng [{a},{b}] là: {tong}')

#     # 2.2. Tính tổng các số chẵn trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# tong = 0    # Dùng để lưu giá trị tổng
# for i in range(a, b+1):
#     if i % 2 == 0:
#         tong = tong + i     # tong += i
# print(f'Tổng các số chẵn trong khoảng [{a},{b}] là: {tong}')

#     # 2.3. Tính tổng các số chia hết cho 5 trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# tong = 0    # Dùng để lưu giá trị tổng
# for i in range(a, b+1):
#     if i % 5 == 0:
#         tong = tong + i     # tong += i
# print(f'Tổng các số chia hết cho 5 trong khoảng [{a},{b}] là: {tong}')

# # Dạng 3: Đếm số lượng
#     # 3.1. Đếm số lượng các số trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# count = 0       # Biến dùng để đếm
# for i in range(a, b+1):
#     count = count + 1       # count += 1
# print(f'Số lượng các số trong khoảng [{a},{b}] là: {count}')

#     # 3.2. Đếm số lượng các số lẻ trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# count = 0       # Biến dùng để đếm
# for i in range(a, b+1):
#     if i % 2 != 0:
#         count = count + 1       # count += 1
# print(f'Số lượng các số lẻ trong khoảng [{a},{b}] là: {count}')

#     # 3.3. Đếm số lượng các số âm trong khoảng [a,b]
# a = int(input('Nhập số nguyên a: '))
# b = int(input('Nhập số nguyên b: '))
# count = 0       # Biến dùng để đếm
# for i in range(a, b+1):
#     if i < 0:
#         count = count + 1       # count += 1
# print(f'Số lượng các số âm trong khoảng [{a},{b}] là: {count}')

#  Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    #  Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

import random
number = random.randint(0,20)
print('Số bí mật:', number)
count = 1
n = int(input('Nhập dự đoán của bạn: '))
while n != number:
    if n < number:
        print('Đoán sai, hãy nhập số lớn hơn!')
    if n > number:
        print('Đoán sai, hãy nhập số nhỏ hơn!')
    n = int(input('\nNhập dự đoán của bạn: '))
    count = count + 1
print(f'Bạn đã đoán đúng sau {count} lần nhập !!!')