N = int(input().strip())
if N % 2 == 1 or N>= 6 and N<= 20:
    print("weird")
elif N >= 2 or N <= 2 or N>= 20:
    print("not weird")