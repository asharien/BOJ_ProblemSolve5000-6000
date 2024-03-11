import sys
E, F, C = map(int, sys.stdin.readline().split())
TEMP = E+F
ANS = 0
while(True):
    ANS += TEMP//C
    TEMP = TEMP%C+TEMP//C
    if TEMP//C ==0:break
print(ANS)
