import sys,string

n = int(input())

M = [ int(v) for v in input().split()]

n = len(M)

cnt = 0

for i in range(0,n-2) :

    for j in range(i+1, n-1):

        for k in range(j+1, n):

            if M[i] > M[j] > M[k] :

                cnt += 1

print(cnt)
