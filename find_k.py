S,K=map(int,input().split())
N=list(map(int,input().split()))
s=[]
for i in range(0,len(N)):
  if N[i]==K:
    s.append(N[i])
print(len(s)-1)
