# Viết chương trình nhập vào số n, tính giai thừa n! = n * (n-1) *...*1

print("------------Ứng dụng tính giai thừa bằng for---------------")

# Input
n = int(input("Enter n: "))
# Output
giai_thua = 1
bieu_thuc = ''
# Process
for so_hang in range (n, 0, -1):
    giai_thua *= so_hang
    bieu_thuc += str(so_hang)

print(f'{bieu_thuc}: {giai_thua}')