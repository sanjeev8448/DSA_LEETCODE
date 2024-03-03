from collections import Counter
my_hashmap = [4,3,1,1,3,3,2]
# my_hashmap.sort()
my_hashmap= Counter(my_hashmap)
print(my_hashmap)
k = 1
for key ,val in reversed(my_hashmap.items()):
    if k > 0:
        my_hashmap[key] -= 1
        k -= 1
    print(key)
# res = []
# for val in (sorted(my_hashmap.values())):
#     # print(val)
#     if k > 0:
#         my_hashmap[val] -= 1
#         k -= 1
# print(my_hashmap)

# res = 0
# for key,val in my_hashmap.items():
#     if val > 0:
#         res += 1
# print(res)
        # res.append(val)
# print(res)
 


