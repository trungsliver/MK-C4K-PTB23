# Khai báo biến: [Tên biến] = [Giá trị]
a = 'loopy'         # Khai báo 1 biến
x, y, z = 1, 2, 3   # Khai báo nhiều biến 1 lúc

# Variables - Biến số: 
    # Dùng để lưu trữ dữ liệu
    # Có thể thay đổi trong khi lập trình

# Data Types - Kiểu dữ liệu
    # String: chuỗi ký tự / xâu ký tự
name = 'Minh Nhật'
    # Interger (int): số nguyên
age = 2
    # Float: số thực
pi = 3.14
    # Boolean / Bool: logic, chỉ gồm 2 giá trị True/False - Đúng/Sai
male = False

# Kiểm tra kiểu dữ liệu - type()
# print('Kiểu dữ liệu của name:', type(name))
# print('Kiểu dữ liệu của age:', type(age))
# print('Kiểu dữ liệu của pi:', type(pi))
# print('Kiểu dữ liệu của male:', type(male))

# Xác định kiểu dữ liệu khi nhập (ép kiểu)
# teacher = str(input('Hãy nhập tên giáo viên của bạn: '))
# age2 = int(input('Hãy nhập tuổi: '))
# point = float(input('Hãy nhập điểm: '))
# loopy = bool(input('Bạn có phải loopy không: '))
# print(type(teacher), type(age2), type(point), type(loopy))

# =========== BÀI TẬP ==========
# Bài 1: Chuyển đổi USD sang VND
    # Nhập số lượng USD muốn chuyển đổi
usd = float(input('Nhập số USD muốn đổi: '))
    # Đổi USD sang VND, tỉ giá: 1 USD = 25000 VND
vnd = usd * 25000
    # Hiển thị số tiền VND ra màn hình
print(f'{usd} USD = {int(vnd)} VND' )

# Bài 2: Nhập chiều dài, chiều rộng HCN.
# Tính chu vi, diện tích HCN và hiển thị ra màn hình
    # Bước 1: Nhập chiều dài, chiều rộng HCN
cd = float(input('Nhập chiều dài HCN: '))
cr = float(input('Nhập chiều rộng HCN: '))
    # Bước 2: Tính chu vi, diện tích HCN
cvi = (cd + cr) * 2
dtich = cd * cr
    # Bước 3: Hiển thị kết quả
print('Chu vi HCN:', cvi)
print('Diện tích HCN:', dtich)

# Bài 3: Nhập chiều dài, chiều rộng hình vuông.
# Tính chu vi, diện tích hình vuông và hiển thị ra màn hình
    # Bước 1: Nhập chiều cạnh
a = float(input('Nhập chiều dài cạnh hình vuông: '))
    # Bước 2: Tính chu vi, diện tích HCN
cvi = a * 4
dtich = a * a
    # Bước 3: Hiển thị kết quả
print('Chu vi hình vuông:', cvi)
print('Diện tích hình vuông:', dtich)