#init(input)
n = int(input()) #n:人數(int)
s = list(map(int, input().split())) #s:分數(list)

#排序並輸出
s.sort() #對分數小到大排序
print(*s) #* -> for all, 輸出s內所有的內容

#case判斷 -> best/worst/normal
#s(已sort) -> 第一個=min, 最後一個=max
#best case
if s[0] >= 60:#最低分及格 -> 全班都及格
    print('best case')
    print(s[0])
#worst case
elif s[-1] < 60: #最高分不及格 -> 全班都不及格
    print(s[-1])
    print('worst case')
#normal case
else: #有人及格有人不及格
    for i in range(len(s)):
        if s[i] >= 60: #ith 人為所有及格中最低分 -> i-1th不及格 且為不及格中的最高分 
            print(s[i-1])
            print(s[i])
            break #找到i即找到ans -> 迴圈結束