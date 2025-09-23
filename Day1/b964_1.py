score = []
p = int(input())
s = input().split()
for i in s:
    score.append(int(i))
score.sort()
print(*score)#[1,2,3]

if score[-1] < 60:
    print(score[-1])
    print('worst case')
    
elif score[0] >= 60:
    print('best case')
    print(score[0])

else:
    for i in range(len(score)):
        if score[i] >= 60:
            print(score[i-1])
            print(score[i])
            break