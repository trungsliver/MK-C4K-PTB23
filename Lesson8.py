# Danh sách - Array / List
# 4 thao tác: CRUD: Create - Read - Update - Delete

# Create - Khởi tạo danh sách
    # Danh sách rỗng - không có phần tử
arr = []
    # Danh sách có sẵn phần tử
arrHS = ['Tú', 'Lâm', 'Hoàng', 'Huy', 'Bách', 'Minh', 'Bảo']
    # len() - trả về độ dài / số lượng phần tử của danh sách
# print(len(arr))
# print(len(arrHS))

# Read - Duyệt, hiện phần tử danh sách
    # Hiện phần tử bằng chỉ số index (bắt đầu từ 0)
print(arrHS[4])     # Output: 'Bách'
    # Hiện phần tử cuối cùng (index = -1)
print(arrHS[6])     # Output: 'Bảo'
print(arrHS[-1])    # Output: 'Bảo'

    # Duyệt và hiện tất cả phần tử danh sách
        # Cách 1: Dùng cả index và value
for i in range(len(arrHS)):
    print(f'[{i}] {arrHS[i]}')

        # Cách 2: Chỉ dùng value
for item in arrHS:
    print(item)

        # Cách 3: Dùng hàm có sẵn
for index, value in enumerate(arrHS):
    print(f'[{index}] {value}')

        # Cách 4: để test
print(arrHS)