nums = [55, 44, 33, 22, 11]

# all
if all([i > 5 for i in nums]):
    print("All large that 5")


# any
if any([i % 2 == 0 for i in nums]):
    print("At last one is even")


# enumerate
for v in enumerate(nums):
    print(v)