# 학습으로 대체
set = [0] * 9
num = list(map(int, str(input())))  


for i in num:
    if i == 6 or i == 9:
        set[6] += 1  
    else:
        set[i] += 1


if set[6] % 2 == 0:
    set[6] = set[6] // 2
else:
    set[6] = (set[6] // 2) + 1

print(max(set))
