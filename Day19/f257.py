# import sys
# for i in sys.stdin:
#     n = int(i)
#     k = int(input())
#     g = [[0] * n for _ in range(n)]

#     for i in range(k):
#         y, x = map(int, input().split())
        
        
#         if g[x][y] != 'x':
#             for dx , dy in [(-1,0) , (1,0) , (0,-1) , (0,1),(1,1),(-1,-1),(1,-1),(-1,1)]:
#                 nx , ny = x + dx , y + dy

#                 if 0 <= nx < n and 0 <= ny < n and g[nx][ny] != 'x':
#                     g[nx][ny] += 1
#         g[x][y] = 'x'
        
#     for row in g:
#         for char in row:
#             print(char, end="")
#         print()

input()