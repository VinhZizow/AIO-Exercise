# Cho một list các số nguyên num_list và một sliding window có kích thước size k di chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải lớn hơn hoặc bằng 1. Ví dụ:
# Input: num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] với k=3
# Output: [5, 5, 5, 5, 10, 12, 33, 33]


def max_kernel(num_list, k):
    start_indexs = list(range(0, len(num_list)-k+1))
    end_indexs = list(range(k, len(num_list)+1))

    result = []

    for start_index, end_index in zip(start_indexs, end_indexs):
        sub_list = num_list[start_index: end_index]
        result.append(max(sub_list))

    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
