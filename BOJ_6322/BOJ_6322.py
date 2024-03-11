import sys
from math import sqrt as sq
def TRI(a, b, c):
    if a == -1:
        if c**2-b**2>0:return sq(c**2-b**2), 0
        else: return -1, 3
    elif b == -1:
        if c**2-a**2>0:return sq(c**2-a**2), 1
        else: return -1, 3
    elif c == -1: return sq(a**2+b**2), 2
def main():
    CNT, LOC = 0, {0:"a", 1:"b", 2:"c", 3:"Impossible."}
    while(True):
        CNT += 1
        A, B, C = map(int, sys.stdin.readline().split())
        if [A, B, C] == [0, 0, 0]: break
        ANS, SIDE = TRI(A, B, C)
        if SIDE == 0: A = ANS
        elif SIDE == 1: B = ANS
        elif SIDE == 2: C = ANS
        print(f"Triangle #{CNT}")
        print(f"{LOC[SIDE]} = {ANS:.3f}" if ANS >0 and A+B>C else f"{LOC[3]}")
        print()
if __name__ == "__main__":
    main()
