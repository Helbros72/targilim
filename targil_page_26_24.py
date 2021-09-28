x = int(input("please enter a number"))
y = int(input("please enter a number"))
max_div = 1
i = 1
if x == y:
    print(x)
else:
    if x < y:
        min_num = x
    else:
        min_num = y
    while i <= min_num:
        if (x % i == 0) and (y % i == 0):
            max_div = i
        i = i + 1

print(max_div)