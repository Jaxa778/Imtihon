nums = [8,1,2,2,3]
new_lst = []
for i in nums:
    count = 0
    for j in nums:
        if i > j:
            count+=1
    new_lst.append(count)
print(new_lst)
# print(f"nums[{i}] = {nums[i]} bo`lganda, undan {count}ta kichikroq raqam mavjud.")