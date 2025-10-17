t = int(input())

for _ in range(t):
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))

    error = set()


    if line1[1] == line2[1] or line1[3] == line2[3] or line1[5] == line2[5]:
        error.add("A")

    if line1[1] == line1[3] or line1[3] == line1[5]:
        error.add("A")
    if line2[1] == line2[3] or line2[3] == line2[5]:
        error.add("A")


    if line1[6] != 1 or line2[6] != 0:
        error.add("B")

  
    if line2[1] != line1[6]:
        error.add("C")

   
    errors = sorted(list(error))

    if not errors:
        print("None")
    else:
        print(*errors, sep="")