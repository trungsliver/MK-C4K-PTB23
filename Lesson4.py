# Bài 1: Nhập số điện bạn sử dụng (kWh)
# Tính tiền điện theo dữ liệu sau và hiển thị ra màn hình
# Bậc 1:    0kWh - 50kWh           giá 1.8k VND
# Bậc 2:    51kWh - 100kWh         giá 2k VND
# Bậc 3:    101kWh - 200kWh        giá 2.3k VND
# Bậc 4:    trên 201kWh            giá 3k VND
            #  Bài làm
# Nhập số điện bạn sử dụng (kWh)
kWh = float(input('Nhập số điện đã sử dụng: '))

# Khai báo biến cash để tính tiền
cash = 0

# Tính tiền theo bậc
if kWh < 0:                     # Nhập sai
    print('Nhập sai dữ liệu')
else:                           # Nhập đúng
    if 0 <= kWh <= 50:          # Bậc 1
        cash = kWh * 1.8
    elif 50 < kWh <= 100:       # Bậc 2
        cash = 50 * 1.8 + (kWh - 50) * 2
    elif 100 < kWh <= 200:      # Bậc 3
        cash = 50 * 1.8 + 50 * 2 + (kWh - 100) * 2.3
    else:                       # Bậc 4
        cash = 50 * 1.8 + 50 * 2 + 100 * 2.3 + (kWh - 200) * 3
    
# Hiển thị kết quả
print(f'Tiền điện bạn phải trả là: {cash}k VND')

# Câu 1: Nhập một số từ bàn phím và in ra số đó.
# Câu 2: Viết chương trình kiểm tra nhập vào 1 số và kiểm tra số đó là chẵn hay lẻ.
# Câu 3: Viết chương trình tính tổng, hiệu, tích, thương của hai số nhập từ bàn phím.
# Câu 4: Viết chương trình nhập vào 1 số và kiểm tra số đó có phải số nguyên tố hay không. (nâng cao)
# Câu 5: Viết chương trình chuyển đổi từ USD sang VND (số tiền được nhập từ bàn phím).
# Câu 6: Viết chương trình nhập số điểm của 3 bạn học sinh, in ra màn hình bạn có điểm thấp nhất và bạn có điểm cao nhất.


