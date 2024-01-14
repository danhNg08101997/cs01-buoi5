# Viết chương trình nhập vào 1 chuỗi ký tự, in ra chuỗi đảo ngược ký tự đó
# input
chuoi_dau = str(input('Nhập chuỗi kí tự: '))
# output
chuoi_dao_nguoc = ''
# process
# Duyệt theo for
# for index in range(len(chuoi_dau)-1, -1, -1):
#     chuoi_dao_nguoc+=chuoi_dau[index]
#     print(index)

# Duyệt theo While
# i = len(chuoi_dau) - 1
# while i > -1:
#     chuoi_dao_nguoc += chuoi_dau[i]
#     print(i)
#     i -= 1

# Duyệt theo for str
# for c in chuoi_dau:
#     chuoi_dao_nguoc = c + chuoi_dao_nguoc
# print(chuoi_dao_nguoc)

# python syntax
chuoi_dao_nguoc = chuoi_dau[::-1]
print(chuoi_dao_nguoc)