# Max Over Kernel

# Cho truoc một num_list và hệ số k
num_list = [2,5,45,8,7,56,65,89,33,2,1,5]
k=3

# Xác định hệ số bắt đầu và hệ số kết thúc dùng slicing
start_idx= list(range(0, len(num_list)-k+1))
end_idx= list(range(k, len(num_list)+1))
'''print(len(num_list))
print(start_idx)
print(end_idx)'''

# Kiểm tra lệnh zip:
'''print(zip(start_idx, end_idx))
print(list(zip(start_idx, end_idx)))'''

# Hiểu rõ hơn về lệnh zip:
''' for start_idx, end_idx in zip(start_idx, end_idx):
    #print(start_idx, end_idx) '''
    

# Bài chính Max Over Kernel
result = []
for start_idx, end_idx in zip(start_idx, end_idx):
    temp = num_list[start_idx:end_idx]
    result.append(max(temp))
print("Ket qua: ")
print(result)