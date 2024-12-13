# Strings - Chuỗi / xâu ký tự
name = 'Quang Huy'

# Độ dài string
print('Độ dài strings:', len(name))    
# Ký tự thứ n trong string
print('Ký tự đầu tiên:', name[0])
print('Ký tự cuối cùng:', name[-1])

# # Duyệt strings
#     # Cách 1: Dùng cả index và value
# for i in range(len(name)):
#     print(name[i], end = ' ')
#     # Cách 2: Chỉ dùng value
# for item in name:
#     print(item, end = ' ')

# Xâu con
str1 = 'QuangHuyVipPro'
str2 = 'VipPro'
str3 = 'DepTrai'

    # Kiểm tra xâu con: hàm in => True/False
print(str2 in str1)             # Output: True
print(str3 in str1)             # Output: False

    # Tìm vị trí xâu con: hàm find() => index
print(str1.find('QuangHuy'))    # Output: 0
print(str1.find(str2))          # Output: 8
print(str1.find(str3))          # Output: -1

# Slicing - cắt chuỗi
name = 'HuyXauSo'
    # Cắt từ đầu strings
print(name[:3])         # Output: Huy
    # Cắt đến cuối strings
print(name[3:])         # Output: XauSo
    # Cắt ở giữa
print(name[3:6])         # Output: Xau

# Xóa khoảng trắng ở đầu và cuối chuỗi - strip()
name = '   Huy Quần Hoa     '
name2 = name.strip()
print(name)
print(name2)

# Thay thế strings - replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ
song2 = song.replace('doo', 'huy')
print(song2)
    # Thay thế với số lượng chỉ định
song3 = song.replace('doo', 'QuangHuy', 3)
print(song3)

# Kết hợp chuỗi - join()
arr = ['r','o','n','a','l','d','o']
str1 = ' '.join(arr)
str2 = ''.join(arr)
str3 = '-'.join(arr)
print(str1)         # Output: r o n a l d o
print(str2)         # Output: ronaldo
print(str3)         # Output: r-o-n-a-l-d-o

# Tách chuỗi - split()
a = '1 2 3 4 5 6 7 8 9'
arr1 = a.split()    # tách theo dấu cách
print(arr1)

b = 'a,s,d,f,g,h,j,k,l'
arr2 = b.split(',')  # tách theo dấu phẩy   
print(arr2)

# Chuyển đổi kiểu dữ liệu trong danh sách
    # Các phần tử đều có DataType là strings
arr = ['1', '2', '3', '4', '5']

    # Cách 1:
arr1 = []
for item in arr:
    x = int(item)
    arr1.append(x)
print(arr1)
    # cách 2:
arr2 = [int(item) for item in arr]
print(arr2)

num_list = [10, 5, 1, 2, 6, 4, 9, 3, 7, 8]
# Tính tổng phần tử danh sách
    # Cách cũ:
sum_all = 0
for item in num_list:
    sum_all += item
print(sum_all)
    # Cách mới
sum_all2 = sum(item for item in num_list)
print(sum_all2)

# Tính tổng phần tử chẵn của danh sách
    # Cách cũ:
sum_even = 0
for item in num_list:
    if item % 2 == 0:
        sum_even += item
print(sum_even)
    # Cách mới
sum_even2 = sum(item for item in num_list if item%2==0)

# Đếm số lượng phần tử chẵn của danh sách
    # Cách cũ
count = 0
for item in num_list:
    if item % 2 == 0:
        count += 1
print(count)
    # cách mới:
num2 = [item for item in num_list if item%2==0]
print(len(num2))

count2 = sum(1 for item in num_list if item%2==0)
print(count2)

# -------------------------Luyện tập-----------------------
# Bài 1: Nhập 2 thông tin: họ, tên. In ra màn hình tên đầy đủ
ho = input('Nhập họ của bạn: ')
ten = input('Nhập tên của bạn: ')
arr = [ho, ten]
full_name = ' '.join(arr)
print(full_name)

# Bài 2: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (01/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình
date1 = input('Nhập chuỗi dạng dd/mm/yyyy: ')
            # Cách 1: dùng slpit()
x = date1.split('/')
day = x[0]
month = x[1]
year = x[2]
print("Ngày:", day, '\nTháng:', month, '\nNăm:', year)
            # Cách 2: dùng replace()
date2 = date1.replace('/', ' tháng ', 1)
date3 = date2.replace('/', ' năm ')
print(date3)

# Bài 3: Nhập vào thông tin dạng username:password
    # kiểm tra xem thông tin vừa nhập có trùng với thông tin có sẵn
    # YC2: bắt người dùng nhập đến khi nào trùng username và password thì kết thúc
username = 'admin'
password = '123456'

info = input('Nhập thông tin dạng "username:password": ')

while (':' not in info):
    print('Nhập sai định dạng, vui lòng nhập lại.')
    info = input('Nhập thông tin dạng "username:password": ')

info_split = info.split(':')
while (info_split[0] != username or info_split[1] != password):
    print('Nhập sai thông tin đăng nhập.')
    info = input('Nhập thông tin dạng "username:password": ')
    info_split = info.split(':')

print('Đăng nhập thành công!')