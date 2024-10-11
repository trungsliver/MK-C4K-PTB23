# Toán tử số học
    # Các phép toán cơ bản: + - * /
    # Chia lấy dư: %
print('7 % 3 =', 7%3)       # Output: 7 % 3 = 1
    # Chia lấy nguyên: //
print('7 // 3 =', 7//3)     # Output: 7 // 3 = 2
    # Lũy thừa: ** (thực hiện từ phải -> trái)
print('2**2**3 = 2**(2**3) = 2**8 =', 2**2**3)

# Toán tử số học với string
    # Phép nối: +
print('Đức' + ' ' + 'Minh') # Output: Đức Minh
    # Phép lặp lại: *
print('hi'*3)               # Output: hihihi
print('Nhật' * 0)

# Toán tử quan hệ: => True/False
    # So sánh bằng: ==
print(5 == 5)           # Output: True
print(5 == 3)           # Output: False
    # So sánh khác: !=
print(5 != 3)           # Output: True
print(5 != 5)           # Output: False
    # So sánh lớn/nhỏ hơn: >, <, >=, <=
print(5 >= 5)           # Output: True
print(5 < 3)            # Output: False

# Toán tử logic: and - or - not
    # Ví dụ: Trà sữa - Gà rán

# Câu điều kiện
    # Dạng thiếu:
age = int(input('Hãy nhập tuổi của bạn: '))
if age >= 18:
    print('Bạn đã đủ 18 tuổi')

    # Dạng đủ:
n = int(input('Nhập 1 số nguyên bất kì: '))
if n % 5 == 0:
    print(n, 'chia hết cho 5')
else:
    print(n, 'không chia hết cho 5')

    # Dạng đa nhánh:
        # [8, 10]: Giỏi, [6.5, 8): Khá, [5, 6.5): TB, [0, 5): Yếu
score = float(input('Hãy nhập điểm của bạn: '))
if 8 <= score <= 10:
    print('Xếp loại: Giỏi')
elif 6.5 <= score < 8:
    print('Xếp loại: Khá')
elif 5 <= score < 6.5:
    print('Xếp loại: Trung Bình')
elif 0 <= score < 5:
    print('Xếp loại: Yếu')
else:
    print('Bạn đã nhập sai điểm')

# =============== LUYỆN TẬP ===================
# Bài 1: Nhập 1 số nguyên n từ bàn phím.
    # Nếu n là số chẵn thì in ra "Đây là số chẵn"
    # Nếu n là số lẻ thì in ra "Đây là số lẻ"
n = int(input('Nhập 1 số nguyên bất kỳ: '))
if n % 2 == 0:
    print('Đây là số chẵn')
else:
    print('Đây là số lẻ')

# Bài 2: Nhập điểm số của bạn từ bàn phím.
# Yêu cầu: Xếp loại học lực học sinh. Biết rằng:
    # [8, 10]: Giỏi, [6.5, 8): Khá, [5, 6.5): TB, [0, 5): Yếu
score = float(input('Hãy nhập điểm của bạn: '))

if score < 0 or score > 10:
    print('Bạn đã nhập sai điểm')
else:
    if score >= 8:
        print('Xếp loại: Giỏi')
    elif score >= 6.5:
        print('Xếp loại: Khá')
    elif score >= 5:
        print('Xếp loại: Trung Bình')
    else:
        print('Xếp loại: Yếu')

# Bài 3: Viết chương trình nhập số điểm của 3 bạn học sinh, in ra màn hình bạn có điểm thấp nhất và bạn có điểm cao nhất.
score1 = float(input('Nhập điểm bạn thứ 1: '))
score2 = float(input('Nhập điểm bạn thứ 2: '))
score3 = float(input('Nhập điểm bạn thứ 3: '))
    # Cách 1:
if score1 >= score2 and score1 >= score3:
    print('Bạn số 1 có điểm cao nhất')
elif score2 >= score1 and score2 >= score3:
    print('Bạn số 2 có điểm cao nhất')
elif score3 >= score1 and score3 >= score2:
    print('Bạn số 3 có điểm cao nhất')
    # Cách 2:
print('Điểm cao nhất là:', max(score1, score2, score3))