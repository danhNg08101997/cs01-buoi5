# Viết chương trình nhập vào một chuỗi và in ra cho biết chuỗi đó có phải là chuỗi đối xứng không
# ví dụ: level - là chuỗi đối xứng, drink - không phải chuỗi đối xứng

# input
chuoi_dau = str(input('Nhập chuỗi: '))
# output
ket_qua =''
# process
# Cách 1: so sánh chuỗi ban đầu với chuỗi đảo ngược của chuỗi đó
# chuoi_dao_nguoc = ''
# for c in chuoi_dau:
#     chuoi_dao_nguoc = c + chuoi_dao_nguoc

# if(chuoi_dau == chuoi_dao_nguoc):
#     ket_qua = f'{chuoi_dau} là chuỗi đảo đối xứng'
# else:
#     ket_qua = f'{chuoi_dau} không phải là chuỗi đối xứng'

# print(ket_qua)

# Cách 2: so sánh ký tự trên chuỗi
flag = True
len_str = len(chuoi_dau)
for index in range(0, len_str//2):
    if chuoi_dau[index] != chuoi_dau[len_str - 1 - index]:
        flag = False
        break

if flag:
    ket_qua = f'{chuoi_dau} là chuỗi đảo đối xứng'
else:
    ket_qua = f'{chuoi_dau} không phải là chuỗi đối xứng'

print(ket_qua)