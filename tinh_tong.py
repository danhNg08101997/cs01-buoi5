#  Viết chương trình nhập vào số n, tính tổng từ 1 -> n sử dụng for-loop

print("------------------Ứng dụng tính tổng sử dụng for------------------------")

# Input
n = int(input("Nhập số n: "))
# Output
sum =  0
# Process
for so_hang in range(1, n + 1):
    sum += so_hang

print(sum)