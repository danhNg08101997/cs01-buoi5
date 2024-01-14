# str: là chuỗi ký tự trong python, cho phép ta lấy ra từng ký tự bằng cách str(index)

title = 'techx'
print(title[1])

# Index: vị trí của ký tự trong chuỗi
# Len(Độ dài: Length): len(title)

print(len(title))

# Duyệt chuỗi: với while
print('------while------')
index = 0
while index < len(title):
    print(title[index])
    index += 1

# Duyệt chuỗi: với for
print('--------for---------')
for i in range(0, len(title)):
    print(title[i])

print('--------for string----------')
for c in title:
    print(c)

# Kiểm tra một chuỗi con có trong chuỗi lớn hay không

product_name = 'iphone 15 promax'
keyword = 'iphone'
if keyword in product_name:
    print('Có các sản phẩm iphone sau đây: ')
else:
    print('Không tìm thấy sản phẩm nào hết!')

# Xử lý cắt chuỗi
str_title = 'hello cybersoft'
print(str_title[:5])
print(str_title[6:])