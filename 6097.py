h,w=map(int,input().split())
grid=[[0 for j in range(w)] for i in range(h)]

n=int(input())
for i in range(n) :
    l,d,x,y=map(int,input().split())
    x = x-1 #(1,1)이 리스트에선 (2,2)이므로 1씩 빼줌
    y = y-1
    for j in range(l):
        if d == False: # 가로
            grid[x][y+j] = 1
        else:
            grid[x+j][y] = 1


for i in range(h):
  for j in range(w): 
    print(grid[i][j], end=' ')  #공백을 두고 한 줄로 출력
  print()  
