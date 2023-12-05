import random
import math
import matplotlib.pyplot as plt

N = 100


def randomisegen(r):
    if random.uniform(0, 1) >= r:
        return 1
    else:
        return 0


def gridcalc_old(A):
    B = [[0 for j in range(N + 2)] for i in range(N + 2)]
    for i in range(1, N):
        for j in range(1, N):
            if A[i + 1][j] == 2:
                B[i][j] = 2
            elif A[i][j] == 2:
                B[i][j] = 2
            else:
                B[i][j] = 0
            if A[i + 1][j + 1] == 2 and A[i][j + 1] == 2 and A[i - 1][j + 1] == 2 and A[i + 1][j] == 0:
                # if A[i + 2][j] == 0 and A[i - 2][j] == 0 and A[i + 1][j] == 0 and A[i - 1][j] == 0:
                B[i][j] = randomisegen(0.5)
            if A[i + 1][j - 1] == 2 and A[i][j - 1] == 2 and A[i - 1][j - 1] == 2 and A[i + 1][j] == 0:
                B[i][j] = randomisegen(0.5)
            if (A[i][j - 1] == 1 or A[i][j + 1] == 1) and A[i][j] != 2:
                B[i][j] = randomisegen(0.5)
            # if (A[i - 1][j + 1] == 1 or A[i + 1][j + 1] == 1) and A[i][j] != 2:
            #     B[i][j] = randomisegen(0.05)
            if A[i][j] == 1:
                B[i][j] = 1
    for i in range(1, N):
        for j in range(1, N):
            A[i][j] = B[i][j]


def gridcalc(A):
    B = [[0 for j in range(N + 2)] for i in range(N + 2)]
    for i in range(1, N):
        for j in range(1, N):
            if A[i + 1][j] == 2:
                B[i][j] = 2
            if A[i][j] == 1:
                B[i][j] = 1
            if A[i][j + 1] == 2:
                B[i][j] = randomisegen(0.5) * 2
            if A[i][j - 1] == 2:
                B[i][j] = randomisegen(0.5) * 2
            if A[i][j] == 2:
                B[i][j] = 2
    for i in range(1, N):
        for j in range(1, N):
            A[i][j] = B[i][j]


A = [[0 for j in range(N + 2)] for i in range(N + 2)]
for i in range(N + 2):
    for j in range(N + 2):
        if i == 0 or i == N+1 or j == 0 or j == N+1:
            A[i][j] = -1
A[N][int(N/2)] = 2

plt.figure(1)
plt.subplot(111)
plt.imshow(A, interpolation="nearest", origin="upper")
plt.colorbar()
for i in range(random.randint(30, N)):
    gridcalc_old(A)
    plt.imshow(A, interpolation="nearest", origin="upper")
    plt.pause(0.05)

plt.imshow(A, interpolation="nearest", origin="upper")
plt.show()
