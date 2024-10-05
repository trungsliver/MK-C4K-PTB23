# Câu lệnh hiển thị ra màn hình
print('Hello world')

# Đây là 1 comment - ghi chú - ctrl /

# Declare variables - Khai báo biến
class1 = 'MK-C4K-PTB23'
teacher = 'Bùi Đức Trung'

# Input - nhập dữ liệu từ bàn phím
name = input('Hãy nhập tên của bạn: ')
age = input('Hãy nhập tuổi của bạn: ')

# Các cách hiển thị ra màn hình
    # Cách 1: Dùng dấu +
print('Họ tên: ' + name)
    # Cách 2: Dùng dấu ,
print('Tuổi:', age)
    # Cách 3: Dùng f - truyền dữ liệu v+ào string
print('Tôi tên là ' + name + ' đang ' + age + ' tuổi')
print('Tôi tên là', name, 'hiện đang', age, 'tuổi')
print(f'Tôi tên là {name} hiện đang {age} tuổi')
    # Cách 4: Hiển thị trên nhiều dòng
print('''
Em là búp măng non
Đức Minh là Loopy
Quang Huy là fan anime
''')

# Các phép toán cơ bản: + - * /
print('1 + 1 =', 1+1) 