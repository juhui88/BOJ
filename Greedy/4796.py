import sys
input = sys.stdin.readline

i = 1
while(True):
    L,P,V = map(int,input().split())

    if L==0 and P == 0 and V == 0: # 종료 조건
        break

    
    camping = V // P * L 
    if(V % P > L):
        camping += L
    else:
        camping += V % P

    print("Case %d: %d" %(i,camping))

    i += 1