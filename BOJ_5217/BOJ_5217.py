import sys
ANS, NUM = {}, []
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    NUM.append(N)
    ANS[N] = []
    for i in range(1, (N//2)+1):
        if i != N-i:
            TEMP = str(i)+str(" ")+str(N-i)
            ANS[N].append(TEMP)
for i in NUM:
    print(f"Pairs for {i}: {', '.join(ANS[i])}")
