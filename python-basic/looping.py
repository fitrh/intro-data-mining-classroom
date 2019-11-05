nums = [2, 3, 4, 5, 10]
sum = 0
count = 0
max = nums[0]
min = max
for i in nums:
    sum += i if (i % 2) == 0 else 0
    count += 1 if (i % 2) == 0 else 0
    max = i if i > max else max
    min = i if i < min else min
    print(i, sep=' ', end=' ' if i != nums[-1] else '\n')

avg = sum / count

print("Average\t:", avg)
print("Maximum\t:", max)
print("Minumum\t:", min)
