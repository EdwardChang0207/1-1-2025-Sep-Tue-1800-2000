#init(input)
i = input() #'xxxxxx'(字串可以用Index找到某個字元)
A = sum([int(j) for j in i[::2]]) #串列取值[start(init:0):end(init:len(list)):interval(init:1)]
B = sum([int(j) for j in i[1::2]])
print(abs(A-B)) #abs -> 取絕對值